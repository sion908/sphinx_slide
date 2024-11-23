import os
import socket
import qrcode
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
from PIL import Image
import argparse
import tempfile


def get_local_ip():
    """ローカルIPアドレスを取得する"""
    try:
        # ダミーのソケット接続を使用してローカルIPを取得
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def generate_qr_code(url):
    """URLからQRコードを生成し、一時ファイルとして保存"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QRコードをPIL Imageとして生成
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # 一時ファイルとして保存
    temp_dir = tempfile.gettempdir()
    qr_path = os.path.join(temp_dir, "server_qr.png")
    qr_image.save(qr_path)
    return qr_path


def start_server(directory, port=8000):
    """
    指定されたディレクトリをHTTPサーバーで公開し、QRコードを生成して表示

    Parameters:
    directory (str): 公開したいディレクトリのパス
    port (int): サーバーのポート番号（デフォルト: 8000）
    """
    # 作業ディレクトリを変更
    os.chdir(directory)

    # IPアドレスを取得
    ip_address = get_local_ip()
    server_url = f"http://{ip_address}:{port}/build/revealjs/index.html"

    # QRコードを生成
    qr_path = generate_qr_code(server_url)

    # サーバーの設定
    handler = SimpleHTTPRequestHandler
    server = HTTPServer(('0.0.0.0', port), handler)

    print('サーバーを起動しました。')
    print(f'ローカルアドレス: http://localhost:{port}')
    print(f'ネットワークアドレス: {server_url}')
    print(f'QRコード画像: {qr_path}')
    print('終了するには Ctrl+C を押してください')

    # QRコードを表示
    try:
        # プラットフォームに応じたデフォルトのイメージビューアでQRコードを開く
        webbrowser.open(qr_path)
    except:
        print("QRコード画像を自動で開けませんでした。手動でQRコード画像を確認してください。")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nサーバーを停止します')
        server.server_close()
        # 終了時に一時ファイルを削除
        try:
            os.remove(qr_path)
        except:
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='QRコード付きHTTPファイルサーバー')
    parser.add_argument('directory', nargs='?', default='.', help='公開するディレクトリのパス（デフォルト: カレントディレクトリ）')
    parser.add_argument('-p', '--port', type=int, default=8000, help='ポート番号（デフォルト: 8000）')

    args = parser.parse_args()
    start_server(args.directory, args.port)
