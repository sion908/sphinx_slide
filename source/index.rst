======================================
Sphinxでのプレゼンテーションを体験する
======================================

.. revealjs-notes::
   
   ここのコメント行は、スピーカーノートして扱われる

準備
====

絵文字を使おう
--------------

絵文字芸：スト2

|:flag_jp:| |:arrow_right:| |:arrow_right:| |:airplane:| |:arrow_right:| |:arrow_right:| |:flag_th:|


動画を埋め込もう
----------------

.. oembed:: https://youtube.com/watch?v=Ps9JiaYqAFg

sphinx-quickstart
----------------

.. code-block:: python

    extensions = [
        'sphinx_revealjs',
    ]

Python仮想環境を用意する
------------------------

ローカル共通環境に不必要なライブラリをインストールしないために、
``venv`` を使って仮想環境を用意します。

ドキュメントを新規作成する
--------------------------

``sphinx-quickstart`` を使って、ドキュメントに必要なファイル一式を用意します。

執筆
====

(TBD)