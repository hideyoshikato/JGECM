# JGECM
## 概要

[BCCWJ](https://pj.ninjal.ac.jp/corpus_center/bccwj/)から複数誤りタイプをもつ日本語文法誤り訂正のための評価用コーパス(An Evaluation Corpus for Japanese Grammar Error Correction with Multiple Error Types: JGECM)を構築するためのリポジトリ


## 実行環境

Python >= 3.6
[Beautiful Soup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) >= 4.1



## 特徴

提案された日本語GECモデルを複数の誤りタイプごとに評価することが可能なデータセットです．


## ディレクトリ構成

`JGECM_org.csv` : JGECMデータの本体です．各列の説明はデータの説明部分を参照してください．
`buildJGECM.py` : BCCWJデータを用いて文法的に誤りを含む文と文法的に正しい文の対データを作成するためのスクリプトです．実行手順については実行手順部分を参照してください．また，出力されるデータの形式についてはデータの説明部分を参照してください．


## データの説明

本データに含まれる誤り種類は下記の通りです．

- 削除(助詞)
- 挿入(助詞)
- 置換(助詞)
- 語彙選択
- 表記
- 動詞
- 削除(助詞・動詞以外)
- 挿入(助詞・動詞以外)

**JGECM_org.csv**

| 列名       | 説明                             |
| -------- | ------------------------------ |
| filename | 構築の元となったBCCWJデータのファイル名         |
| sen_id   | 当該ファイルにおける誤り作成元文を示すID          |
| goku     | 挿入している文字列（空白の場合は削除していることを表します） |
| leftpos  | 誤り発生箇所の開始位置を左から数えた場合の場所        |
| rightpos | 誤り発生箇所の終了位置を右から数えた場合の場所        |
| type     | 誤り種類                           |

**作成****される****対訳データ**

| 列名   | 説明                               |
| ---- | -------------------------------- |
| tgt  | 文法的に正しい文（BCCWJデータから当該文を抜き出したデータ） |
| src  | 文法的に誤りを含む文（BCCWJの文に）             |
| type | 誤り種類                             |

**出力形式の例**
出力されるcsvデータの形式は以下のとおりです．

デフォルト設定での出力

    tgt,src,type
    私は猫が大好きです。,私猫が大好きです。,削除(助詞)
    私は猫が大好きです。,私はを猫が大好きです。,挿入(助詞)

--sep 1とした場合の出力

    tgt,src,type
    私は猫が大好きです。,私[]猫が大好きです。,削除(助詞)
    私は猫が大好きです。,私は[を]猫が大好きです。,挿入(助詞)



## 対訳データ作成の実行手順

**実行例**
デフォルトでの実行

    python buildJGECM.py ~/BCCWJ/Disk1/

オプションの指定

    python buildJGECM.py ~/BCCWJ/Disk1/ --output output.csv --sep 1

第1引数にはBCCWJ-DVD版(Version 1.1)，Disk1のC-XMLディレクトリpathを指定してください．

オプション
--output 出力先を指定します．指定しない場合には，`JGECM.csv`というファイル名で保存されます．
--sep 誤り挿入箇所を`[`, `]`で囲む場合には1を指定します．省略時には囲まれません．


## 参考文献

Kikuo Maekawa, Makoto Yamazaki, Toshinobu Ogiso,Takehiko Maruyama, Hideki Ogura, Wakako Kashino,Hanae Koiso, Masaya Yamaguchi, Makiro Tanaka, andYasuharu Den. ``Balanced corpus of contemporary written Japanese". *Language resources and evaluation*, Vol. 48,No. 2, pp. 345–371, 2014.


## Author

Hideyoshi KATO
https://sites.google.com/view/webpageofhideyoshikato/

## Licence

本レポジトリで公開しているデータ(JGECM_org.csv)およびスクリプト(buildJGECM.py)
は，「クリエイティブ・コモンズ 表示 4.0 国際 パブリック・ライセンス（CC BY 4.0）」とします．
ただし，本スクリプトによりBCCWJを用いて作成されたデータについては，BCCWJの利用規約に従ってください．BCCWJデータを利用するためには，国立国語研究所との利用契約が必要です．

