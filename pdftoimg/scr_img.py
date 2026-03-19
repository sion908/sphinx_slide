# import os
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image
import os

# poppler/binを環境変数PATHに追加する
# poppler_dir = Path(__file__).parent.absolute() / "poppler/Library/bin"
# os.environ["PATH"] += os.pathsep + str(poppler_dir)

pdf_path = Path("./pdf/Nagasaki_Terroir_Marche.pdf")
image_dir = Path("./img")

# PDFファイルを画像に変換
pages = convert_from_path(pdf_path, dpi=150)

# 既存のJPEG画像を保存
if len(pages) > 1:
    for i, page in enumerate(pages):
        file_name = pdf_path.stem + "_{:02d}".format(i + 1) + ".jpeg"
        image_path = image_dir / file_name
        # JPEGで保存
        page.save(str(image_path), "JPEG")
else:
    file_name = pdf_path.stem + ".jpeg"
    image_path = image_dir / file_name
    # JPEGで保存
    pages[0].save(str(image_path), "JPEG")

# 2x2配置の画像を生成
def create_2x2_grid(image_files, output_path, target_size=512):
    """画像ファイルを2x2で配置した正方形画像を生成"""
    images = []
    
    # 画像を読み込み、512x512にリサイズ
    for img_file in image_files[6:10]:  # 最初の4枚を使用
        img = Image.open(img_file)
        # アスペクト比を維持しながら512x512にリサイズ
        img_resized = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
        images.append(img_resized)
    
    # 2x2グリッド用のキャンバスを作成 (1024x1024)
    canvas = Image.new('RGB', (target_size * 2, target_size * 2), 'white')
    
    # 画像を配置
    positions = [(0, 0), (target_size, 0), (0, target_size), (target_size, target_size)]
    for i, (img, pos) in enumerate(zip(images, positions)):
        canvas.paste(img, pos)
    
    # 保存
    canvas.save(output_path, "JPEG")
    print(f"2x2グリッド画像を保存: {output_path}")

# 既存のJPEG画像を取得して2x2グリッドを生成
jpeg_files = sorted(image_dir.glob("Nagasaki_Terroir_Marche_*.jpeg"))
if len(jpeg_files) >= 4:
    grid_output = image_dir / "Nagasaki_Terroir_Marche_2x2_grid_2.jpg"
    create_2x2_grid(jpeg_files, grid_output)
else:
    print(f"画像が4枚未満です: {len(jpeg_files)}枚")
