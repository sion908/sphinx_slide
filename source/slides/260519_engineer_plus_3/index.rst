======================================================================
ChatGPTを改めて知る
======================================================================

.. revealjs-slide::
    :conf: {"width":1920,"height":1080}

:author: sion908
:date: 2026/05/19
:event: エンジニアプラス＃3 〜 AI活用LT会〜

はじめに
================

.. qrcode::
    :class: center
    :width: 400

    https://slide.sion908.tech/

ここでスライドは公開しています  
そのうち消えているかもしれないですが...

.. raw:: html

   <p class="small-line">(ちなみに自分のポートフォリオもここから飛べます)</p>


アジェンダ
======================================================================
このプレゼンテーションでは、次のことを解説します。


.. revealjs-fragments::
    * おまえだれよ
    * ChatGPTのカスタマイズは3層ある
    * アプリ版ならではの体験
    * 実際にどう使っているか
    * まとめ


.. include:: whois.rst


2. ChatGPTのカスタマイズは3層ある
======================================================================


ChatGPTのカスタマイズは「3層」で整理できる
----------------------------------------------------------------

.. container:: flex

    .. container:: size-1

        **パーソナライズ**

        .. revealjs-fragments::
            * 自分を覚えさせる
            * 口調や返し方を固定する
            * "あなたは誰？"

    .. container:: size-1

        **Projects**

        .. revealjs-fragments::
            * 作業を分ける
            * 会話やファイルを整理する
            * "今なにをしてる？"

    .. container:: size-1

        **GPTs**

        .. revealjs-fragments::
            * 役割を作る
            * 専用のアシスタント
            * "相手に何をさせたい？"

.. revealjs-notes::
    この3層の違いを理解することが重要


パーソナライズ vs Projects
----------------------------------------------------------------

.. container:: flex

    .. container:: size-1

        **パーソナライズ**

        - 自分のこと
        - 全体に効く
        - 長期的な傾向

    .. container:: size-1

        **Projects**

        - 作業のこと
        - テーマごとに分ける
        - その時々の内容

.. revealjs-notes::
    パーソナライズ: 簡潔に答えて
    Projects: このテーマで話して


超重要な整理
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * ユーザー
            * ↓ パーソナライズ（自分設定）
            * ↓ Project（作業分離）
            * ↓ GPTs（専用AI）
            * ↓ 会話

    .. container:: size-1

        .. revealjs-fragments::
            * 自分を設定する
            * 作業を分ける
            * AIを役割化する

.. revealjs-notes::
    ChatGPTは"会話"ではなく"文脈"として分けた方が強い


3. アプリ版ならではの体験
======================================================================


アプリ版は「検索エンジン」より「常駐AI」に近い
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * 思いついたら喋る
            * 写真を撮る
            * URLを投げる
            * 音声で話す

    .. container:: size-2

        .. revealjs-fragments::
            * PCブラウザと使い方が違う
            * "チャット"から変わる
            * 文脈を伝えやすい

.. revealjs-notes::
    キーボードでAI使ってる時点で古いかもしれない


アプリ特有で重要なもの
----------------------------------------------------------------

.. container:: flex

    .. container:: size-1

        **Voice**

        .. revealjs-fragments::
            * 会話が続く
            * 割り込みができる
            * リアルタイムで応答
            * 自然な会話感

    .. container:: size-1

        **Camera**

        .. revealjs-fragments::
            * 書類を読む
            * ホワイトボードを見る
            * UIを確認する
            * 物を見る

    .. container:: size-1

        **Share Sheet**

        .. revealjs-fragments::
            * Webページを共有
            * PDFを共有
            * 画像を共有
            * 動画を共有

.. revealjs-notes::
    スマホだとかなり便利


音声会話 + 画面文脈
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * 画面を見ながら会話できる
            * 資料を見せながら話す
            * コードを見せながら話す
            * UIを見せながら話す

    .. container:: size-1

        .. figure:: _imgs/action_automate_iphone.jpeg
            :alt: action_automate_iphone
            :width: 400px


4. 実際にどう使っているか
======================================================================


日常での使い方
----------------------------------------------------------------

.. container:: flex

    .. container:: size-1

        .. revealjs-fragments::
            * メール作成
            * 要約
            * アイデア出し
            * 調べ物
            * 英語の翻訳・添削

    .. container:: size-2

        .. revealjs-fragments::
            * AIはChatGPTがメイン
            * MacアプリだとOpt+Spaceで即起動できてラク
            * スマホも"即起動"に寄せる（アクションボタン、オートメーション、プライベートモード）

    .. container:: size-1

        .. figure:: _imgs/action_automate_iphone.jpeg
            :alt: action_automate_iphone
            :width: 400px 


仕事での使い方
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * 文書作成
            * 資料作成
            * アイデア出し
            * 調べ物
            * 要約

    .. container:: size-1

        .. figure:: _imgs/antigravity.png
            :alt: antigravity
            :width: 70%
            :class: center


「文脈」を伝える重要性
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * 正しい情報を渡すと精度が上がる
            * 文脈を整理する
            * 仕様や要点をまとめる
            * サンプルや例を用意する

    .. container:: size-1

        .. figure:: _imgs/repo.png
            :alt: repo
            :width: 90%
            :class: center


5. まとめ
======================================================================

ChatGPTを使いこなすというより
"文脈を設計する" に近い
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        .. revealjs-fragments::
            * **ChatGPTのカスタマイズは3層ある**
            * **パーソナライズ：「あなたは誰？」**
            * **Projects：「今なにをしてる？」**
            * **GPTs：「相手に何をさせたい？」**

    .. container:: size-2

        .. revealjs-fragments::
            * エンジニア視点だけでなく、ユーザー視点も持つ
            * 文脈管理が鍵
            * これからのAIとの付き合い方


さいごに
----------------------------------------------------------------

ChatGPTを改めて知る。

エンジニアとしてではなく、ユーザーとして。

これからのAIとの付き合い方を一緒に考えていきましょう。
