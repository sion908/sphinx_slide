:og:description: Pythonのloggingモジュールのinfo、warning、errorの適切な使い分けと実践方法を解説します。

.. meta::
    :description: Pythonのloggingモジュールのinfo、warning、errorの適切な使い分けと実践方法を解説します。

======================================================================
オープニングとloggerの適切な使い方
======================================================================

.. revealjs-slide::
  :theme: league
  :conf: {"width":1920,"height":1080}

:author: sion908
:date: 2026/05/15
:event: 5月15 NaITE LT会

アジェンダ
======================================================================
このプレゼンの概要です

- おまえだれよ
- 会の目的
- LT: loggerの話
  - info, warning, errorの適切な使い分け
  - printとの違い
  - 実務レベルでの出力先の違い
- まとめ

.. include:: whois.rst
.. include:: purpose.rst


LT: loggerの話
======================================================================

info, warning, error 適切に使えてるか？
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        **ログレベルの使い分け**

        .. code-block:: python

            import logging

            logger = logging.getLogger(__name__)

            logger.debug("デバッグ情報")      # 開発時のみ
            logger.info("正常な処理")         # 通常の動作記録
            logger.warning("警告")            # 将来問題になりうる
            logger.error("エラー")            # 重大だが処理継続
            logger.critical("致命的エラー")  # プログラム続行不能

    .. container:: size-2

        **よくある間違い**

        .. revealjs-fragments::
          * すべて `print()` で済ませてる
          * エラー時だけログ出力してる
          * debugレベルを本番で出力してる
          * ログにコンテキストが足りない

        .. revealjs-fragments::
          * **「なんか動かない」→ログがない**
          * **「いつエラーが起きた？」→タイムスタンプがない**
          * **「どのユーザー？」→ユーザーIDがない**


Pythonのprintとの違い
----------------------------------------------------------------

.. container:: flex

    .. container:: size-1

        **printの問題点**

        - 標準出力に固定
        - レベル管理がない
        - フォーマットが自由すぎる
        - 本番環境での制御が困難
        - ログローテーション未対応

    .. container:: size-1

        **loggerのメリット**

        - 出力先を柔軟に設定可能
        - レベル別の出力制御
        - 構造化されたフォーマット
        - ファイル、Syslog、クラウドなどに対応
        - ログローテーション自動化

    .. container:: size-1

        **実務での違い**

        .. code-block:: python

            # print: ただ出力するだけ
            print("ユーザー作成: tanaka")

            # logger: 構造化された情報
            logger.info(
                "ユーザー作成完了",
                extra={
                    "user_id": "12345",
                    "username": "tanaka",
                    "ip": "192.168.1.1"
                }
            )


実務レベルでの出力先の違い
----------------------------------------------------------------

.. container:: flex

    **開発環境**

    - コンソール出力（StreamHandler）
    - DEBUGレベルまで表示
    - 色付きで見やすく

    **本番環境**

    - ファイル出力（FileHandler, RotatingFileHandler）
    - INFOレベル以上
    - JSONフォーマットで解析容易
    - ログ集約サービスへ転送（Fluentd, CloudWatchなど）

.. container:: flex

    .. container:: size-2

        **設定例**

        .. code-block:: python

            # サイズベースのローテーション
            from logging.handlers import RotatingFileHandler

            handler = RotatingFileHandler(
                'app.log',
                maxBytes=10*1024*1024,  # 10MBでローテーション
                backupCount=5            # 5世代分保持
            )

            # 時間ベースのローテーション
            from logging.handlers import TimedRotatingFileHandler

            handler = TimedRotatingFileHandler(
                'app.log',
                when='midnight',  # 毎日深夜にローテーション
                backupCount=30    # 30日分保持
            )

    .. container:: size-2

        **ログ集約の重要性**

        - 複数サーバーのログを一箇所で管理
        - エラー検知とアラート
        - トラブルシューティングの効率化
        - ユーザー行動の分析


まとめ
======================================================================

.. container:: flex

    .. container:: size-2

        **会の目的**

        - AI時代でも知識は重要
        - AIの回答を判別する能力が必要
        - 勉強会を知識共有の場として活用

    .. container:: size-2

        **loggerのまとめ**

        - printではなくloggerを使おう
        - ログレベルを適切に使い分けよう
        - 実務では出力先とフォーマットを意識しよう
        - ログは「未来の自分」へのメッセージ


さいごに
----------------------------------------------------------------

次回のテーマについて、皆さんの意見をお聞かせください。

- React/Vue/Angularの深掘り？
- データ分析の実践？
- セキュリティ基礎？
- その他、興味のある分野？

よろしくお願いします！
