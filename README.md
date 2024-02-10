<div align="center">
    ここに画像を貼り付け
</div>
# highTech-gomiBox

![Licence](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=43200)
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">
<img src="https://img.shields.io/badge/-CSS3-1572B6.svg?logo=css3&style=flat">
<img src="https://img.shields.io/badge/-HTML5-333.svg?logo=html5&style=flat">
<img src="https://img.shields.io/badge/-Tailwind%20CSS-56347C.svg?logo=Tailwind%20CSS&style=plastic">
<img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=flat">
<img src="https://img.shields.io/badge/-OpenCV-5C3EE8.svg?logo=OpenCV&style=plastic">
<img src="https://img.shields.io/badge/-Raspberry%20Pi-C51A4A.svg?logo=raspberry-pi&style=flat">
<img src="https://img.shields.io/badge/-Arduino-00979D.svg?logo=arduino&style=plastic">
<img src="https://img.shields.io/badge/-GitHub-181717.svg?logo=github&style=flat">

## OverView

highTech-gomiBox(選択通過型廃棄飲料容器収集箱)は缶とペットボトルの自動識別を行うゴミ箱搭載型システムです。  
また，ゴミ箱からの様子を配信する管理者用 Web アプリも含まれます。  
ここに画像を追加

## Usage

構成は以下のようになっています。  
(画像を追加)
Raspberry Pi に下記に示すモジュールをインポートします。

- Flask
- http.server
- OpenCV(opencv-python)
- pigpiod
  RaspberryPi 起動後に下記コマンドを実行します。(サーボモータを動かすのに必要です。)

```shell
sudo pigpiod
```

また，ゴミ検知用と Web アプリ用で RaspberryPi を 2 台用意することを推奨します。(性能上の問題)

### システムの起動手順

- 2 台の RaspberryPi を起動
- Web アプリ用 RaspberryPi で，webApp フォルダ内の App.py と dataServer.py を管理者権限で実行
- ゴミ箱用 RaspberryPi で，gomiApp フォルダ内の gomiBoxSystem.py を実行

なお，ゴミ箱用 RaspberryPi 側の gomiBoxSystem.py 内の IP アドレスを WebApp 用の IP アドレスに書き換える必要があります。  
現時点で，localhost にのみ対応しております。また，2 台の RaspberryPi は同一ネットワークに接続している必要があります。

## Author

このシステムは舞鶴工業高等専門学校電気情報工学科の 3 年次開講科目「電気情報工学実験 IIB」の制作実験において作成されました。

- Kawagoe Chihaya
- Senzaki Rintaroh
- Hirata Soma  
  [GitHub](https://github.com/s-hirata0831)
- Fujii Koki
  [GitHub](https://github.com/kouki-f)
