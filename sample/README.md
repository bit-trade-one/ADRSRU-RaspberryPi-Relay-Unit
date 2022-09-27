# ADRSRU2/4/8 ラズベリーパイ用リレー制御拡張基板
# サンプルプログラムのインストールについて


## ライブラリ関連のインストール

```
$ sudo apt-get update
$ sudo apt-get install -y python-dev
$ sudo apt-get install -y python-pip
sudo pip install RPi.GPIO

```

## 使用方法
sample.pyを起動すると、1秒周期で4つのリレーを順にON/OFFします。
使用するボード（2回路、4回路、8回路）に合わせて引数（2,4,8)を指定してください。
```
$ python3 sample.py 4
port on : 0
port on : 1
port on : 2
port on : 3
port off: 0
port off: 1
port off: 2
port off: 3
```
