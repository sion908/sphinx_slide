:og:description: AI-DLCへの挑戦と挫折、そしてSpec駆動・Cross-Family分業へ至ったリアルな開発記録とJAWS-UG長崎リスタートの告知

.. meta::
    :description: AI-DLCへの挑戦と挫折、そしてSpec駆動・Cross-Family分業へ至ったリアルな開発記録とJAWS-UG長崎リスタートの告知

======================================================================
AI-DLCをわからないなりにやってみた話
======================================================================

.. revealjs-slide::
    :conf: {"width":1920,"height":1080}

:author: sion908
:date: 2026/10/23
:event: AWS Community Builders Meetup Kyushu 2026

はじめに
======================================================================

.. revealjs-notes::

    QRコードからスライドの閲覧案内

.. qrcode::
    :class: center
    :width: 400

    https://slide.sion908.tech/

ここでスライドは公開しています

.. raw:: html

   <p class="small-line">(ポートフォリオ: portfolio.sion908.tech)</p>


お前誰よ
======================================================================

紫苑（@sion908）

.. container:: flex

    .. container:: size-1

        .. figure:: ../shared/_image/avator.jpg
            :alt: 著者近影
            :align: center
            :width: 100%

    .. container:: size-2

        * 生息地 : 長崎
        * 会社 : ヒアートゥー株式会社
        * コミュニティ :

          * JAWS-UG長崎 運営
          * NaITE （長崎IT技術者コミュニティ）
          * UE長崎 (3DCG)

        * 趣味 : 3DCG, 写真
        * Xreal One Pro熱が再燃しました

    .. container:: size-1

        .. figure:: ../shared/_image/logo_heare_to.png
            :alt: ヒアートゥーアイコン
            :align: center
            :width: 60%

        .. figure:: ../shared/_image/jawsug-nagasaki-icon.png
            :alt: JAWS-UG長崎アイコン
            :align: center
            :width: 60%

        .. figure:: ../shared/_image/ue_nagasaki.png
            :alt: UE長崎ロゴ
            :align: center
            :width: 60%


1. AI-DLCをやってみた
======================================================================



背景：IoT系システムのAWSリプレイス
----------------------------------------------------------------------


* 対象 : ラズパイを用いたIoT系システム
* ミッション : PHP+SQLiteから、AWS全面サーバーレスへの刷新

  - Go Lambda + DynamoDB
  - AWS CDKで全IaC化
  - AWS IoT Core (MQTT) で現地Raspberry Piと双方向通信
  - AWS IoT Device Managementで、Raspberry Piのメンテ

* スタイル : 完全AI主導開発 (AI Native) でやりきる！


AI-DLC（AI主導ライフサイクル）とは？
----------------------------------------------------------------------

.. revealjs-notes::

    SDLCをAIエージェント群が自律推進するフレームワーク

* AI-DLC (AI-Driven Development Lifecycle)

  - 構想 → 設計 → 実装 → テスト をAIが自律進行
  - 監査ログ・品質ゲート・人間の承認ターンの厳格な管理

* 18ステージを突破！

  - 要件定義（FR/NFR 38項目）、ストーリー（23件）
  - システム境界契約（MQTTプロトコル定義等）
  - 「AIだけで完璧なエンタープライズ設計ができた！」…と歓喜


しかし、突如として訪れた「進行不能」
----------------------------------------------------------------------

.. revealjs-notes::

    環境トラブル（サブエージェント不全・フック凍結）で停止した話

.. container:: flex

    .. container:: size-2

        * トラブル1: サブエージェントが丸腰
          - サブエージェント、子エージェントに ``fs_write`` 等のツールが継承されないバグ (Kiro Issue #11150)
          - ファイル読み書きすらできず即座にタスク失敗！

        * トラブル2: フック機構の完全凍結
          - 人間が承認しても監査ログに記録されず、品質ゲートが開かない

        *  決断: フレームワークを脱出！
          - 優秀な18ステージの設計書を「 仕様の正本 」として凍結保存
          - ワークフローは捨て、 素の実装 へ移行

    .. container:: size-2

        .. figure:: _imgs/github_bug_subagent.png
          :alt: Kiro Issue #11150 サブエージェントのツール欠落バグ
          :align: center
          :width: 100%

        .. raw:: html

           <p class="small-line"><a href="https://github.com/kirodotdev/Kiro/issues/11150" target="_blank">Kiro Issue #11150: subagent tools missing</a></p>


「Bolt（垂直スライス）」で全機能完成！…のはずが
----------------------------------------------------------------------

.. revealjs-notes::

    Bolt単位では100点だったがシステム全体で崩壊した話

* Bolt（Walking Skeleton）方式を採用

  - UI → Cloud API → MQTT → ロッカー解錠までを縦断で1本ずつ貫通
  - Bolt 1〜7を完走し、各単体テストも全合格！🎉

* 全体批判的レビューで戦慄の事実が発覚…

  - APIに認可がない （誰でも全ロッカー解錠可能）
  - ハッシュ値をPINとして送ると解錠できる
  - Go Lambda用ハンドラがない （なぜか常駐HTTPサーバで実装）
  - DynamoDB永続化がなく、再起動で状態全ロスト


なぜ起きた？「Boltのエアポケット」
----------------------------------------------------------------------

.. revealjs-notes::

    スコープの押し付け合いとテストの罠

.. container:: flex

    .. container:: size-2

        * スコープの押し付け合い
          - Bolt 1「認証はBolt 2でやる」
          - Bolt 2「受取APIとの結合は後段で」
          - ➡️ Boltの狭間にある「システム横断の関心事」が丸ごと脱落

        * テストの前提データ注入の罠
          - テストが直接DBにハッシュをINSERTしていたため、入口〜出口の実データ連携欠落に気づけなかった

    .. container:: size-2

        .. admonition:: 教訓
            :class: warning

            「機能が通った（Bolt）」と
            「システムが動く（Spec）」は別物！


Spec駆動 × Cross-Family分業
----------------------------------------------------------------------

.. revealjs-notes::

    現在の安定プラクティス：ClaudeとGeminiの役割分担

.. container:: flex

    .. container:: size-2

    * Spec駆動
        - 測定可能な受入基準・境界・データフローを明文化
    * Cross-Family (異モデル) 分業
        - Kiro (Claude) : 計画・Spec策定・反証スタンスでの監査
        - agy (Gemini) : 高速・安価なコード実装・単体テスト
    * 同モデルの盲点を別ファミリのモデルが厳格に突く！

    .. container:: size-1

    .. figure:: _imgs/workflow.jpeg
        :alt: Cross-Family開発ワークフロー
        :align: center
        :width: 95%


2. 長崎からのお知らせ
======================================================================

九州のAWS仲間の皆さん、

「JAWS-UG長崎」は今年度からリスタートしました


長崎、動き出しています！
----------------------------------------------------------------------

.. container:: flex

    .. container:: size-2

        * 直近の活動 :

            - 先日も長崎でLT会やもくもく会を継続開催中
            - おととい（10/21）も長崎で BuilderCards Night #4 を開催！
            - そして今夜、福岡のこの場に来ています！

    .. container:: size-1

        .. figure:: _imgs/jaws_ug_ngs_vol0.png
            :alt: AWS Builder CArds Ni
            :align: center
            :width: 100%

        .. figure:: _imgs/jaws_ug_ngs_vol1.png
            :alt: AWS Builder CArds Ni
            :align: center
            :width: 100%

        .. figure:: _imgs/cardsnight.png
            :alt: AWS Builder CArds Ni
            :align: center
            :width: 100%

2027年 2月 27日（土）イベント開催！
----------------------------------------------------------------------


* 日程 : 2027年 2月 27日（土）
* 場所 : グラバー園内 旧スチイル記念学校
* 内容 :

  - JAWS-UG長崎 リスタート記念イベント
  - AWS最新技術セッション ＆ 交流LT会！

ぜひ福岡・九州各地から長崎へ遊びに来てください！


まとめ
======================================================================


1. AI主導開発 :

   - 垂直スライスの成功に安心せず、システム全体の批判的レビューを怠るな
   - サブエージェント、子エージェントの扱い方がわかれば教えていただきたいです
   - Claude (計画・監査) × Gemini (実装) の分業もありなのでは？

2. JAWS-UG長崎リスタート :

   - 2027年 2月 27日（土） 長崎でお待ちしています！
   - 一緒に九州のコミュニティを盛り上げていきましょう！

ありがとうございました！
