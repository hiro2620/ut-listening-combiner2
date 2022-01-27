# ut-listening-combiner

青本や実戦模試の東大英語のリスニング音源を本番と同じ形式の
1つのファイルに結合できるプログラムです。

## セットアップ
### 0. ダウンロード
    git clone https://github.com/hiro2620/ut-listening-combiner2
    cd ut-listening-combiner2

### 1. ffmpegをインストール
    ffmpeg -version
    # ffmpeg version 4.1.6-1~deb10u1 Copyright (c) 2000-2020 the FFmpeg developers
    # built with gcc 8 (Debian 8.3.0-6)

### 2. 依存ライブラリをインストール
    pip install -r requirements.txt


## 使い方
```bash
python3 main.py
```

mp3ファイルは、デフォルトでは`config.py`内の`config`に従って結合されます。
`config`の`sections`が結合する要素と順序を表し、各要素ごとに使うファイルは
`src`で指定します。

`src`でのファイルの指定方法は以下に挙げる2つがあります。
- numbered assets(整数)
    `config`の`base_path`に指定したディレクトリ(デフォルトでは実行時のパス)内にあるmp3ファイルで、
    ファイル名に含まれる数字が小さい方から順に0,1,2...となります。(ファイル名に数字が含まれている必要があります。また、ファイル名に含まれている数字と`src`で指定する名前としての数字は一致しません。)

    CDのトラック番号を含むファイルでの使用を想定しています。(リスニング読み上げ分本体など)

- named assets(文字列)
    `config`の`named_assets`に指定した要素の`name`属性です。
    適当なディレクトリに保管された、年度を超えて再利用するファイルでの使用を想定しています。(試験の説明など)

ファイル配置の例
```bash
.
├── assets
│   └── 試験の注意.mp3   <- named assets
│
├──main.py
│
├──Track8.mp3          <- numberd assets
├──Track9.mp3          <- numberd assets
│
└── out
    └── 出力されたmp3ファイル.mp3
```

上に挙げなかった`config`の属性については、`define_types.py`を参照して下さい。

結合されたファイルは


## 動作確認環境
- Ubuntu 20.04.2 LTS x86_64
- Python 3.8.10
- ffmpeg 4.1.6-1
