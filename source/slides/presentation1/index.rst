======================================================================
AI時代のコミュニティHP：Astro+Markdownがちょうどいい
======================================================================

.. revealjs-slide::
    :conf: {"width":1920,"height":1080}

:author: sion908
:date: 2026/02/22
:event: エンジニアプラス #1 〜 AI活用LT会〜

はじめに
================

.. qrcode::
    :class: center
    :width: 400

    https://slides.sion908.tech/

ここでスライドは公開しています  
そのうち消えているかもしれないですが...

.. raw:: html

   <p class="small-line">(ちなみに自分のポートフォリオもここから飛べます)</p>


アジェンダ
======================================================================
このプレゼンテーションでは、次のことを解説します。


.. revealjs-fragments::
    * おまえだれよ
    * 私的最近のAI事情
    * NaITeのHPをAstro + Markdownで作った話
    * まとめ


.. include:: whois.rst


1. 私的最近のAI事情
======================================================================


日常利用
--------

.. container:: flex

    .. container:: size-1

        .. figure:: _imgs/action_automate_iphone.jpeg
            :alt: action_automate_iphone
            :align: left
            :width: 400px 
 
    .. container:: size-3

        .. revealjs-fragments::
            * AIはChatGPTがメイン
            * MacアプリだとOpt+Spaceで即起動できてラク
            * スマホも“即起動”に寄せる（アクションボタン、オートメーション、プライベートモード）


コーディング周り
----------------------------------------------------------------

.. container:: flex

    .. container:: size-3

        .. revealjs-fragments::
            * Windsurf / Antigravity を触ってる（スキルはまだこれから）
            * 代わりにやってるのが“文脈管理”
                * `.git/info/exclude` で `memo/` を作って自分専用の素材置き場にする
                * 仕様メモ、URL要点、サンプルコード、実験コードを放り込む
                * 正しい情報を渡すことで精度をあげる

        .. figure:: _imgs/antigravity.png
            :alt: antigravity
            :width: 60%
            :class: center


    .. container:: size-1

        .. figure:: _imgs/repo.png
            :alt: repo
            :width: 90%
            :class: center


メイン：NaITeのHPをAstro + Markdownで作った話
======================================================================


* コミュニティHPは、作るより“更新が続くこと”の方が難しい
* イベント履歴や活動記録が積み上がらないと、外から見たときに伝わらない
* とりあえず簡単に何かやる方法はないのか



WPじゃなくAstro+Markdownにした理由
----------------------------------------------------------------

* UI操作が不要である
* 運用コストが軽い
    * プラグイン/セキュリティ等の“運用タスク”を減らしたい
    * サーバー代はゼロ
* AI時代は`文章がらく`なので、Markdown運用が噛み合う, IDEとの相性も良い
* 公開が簡単（GitHubに置いてpushでデプロイ、編集は基本Markdown）

運用でやること
----------------------------------------------------------------

.. container:: flex

    .. container:: size-2
 
        * イベントは src/content/events/ に YYYY-MM-DD-xxx.md を追加するだけ
        * content collections でスキーマを決めて項目抜けを防ぐ
        * 一覧は自動生成、pushしたらActionsでデプロイ

        .. qrcode::
            :class: center
            :width: 70%

            https://sion908.github.io/naite/

    .. container:: size-3

        .. figure:: _imgs/naite_repo.png
            :alt: NaITE github レポジトリ
            :class: center
            :width: 80%

