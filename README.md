# mypkg
![test](https://github.com/Takuto2345/Mypkg/actions/workflows/test.yml/badge.svg)
![test](https://img.shields.io/badge/ros2-humble-blue)
![test](https://img.shields.io/badge/python-v3.10-blue)
## 概要
countupという名のトピックを介して16bitの符号つき整数型のメッセージをtalker.py,listener.pyという名の２つのノードでパブリッシュ並びにサブスクライブするros2用のパッケージ



## 使い方
mypkgをインストール後、ビルドをした後実行するとtalker.pyから数を０から１ずつ増やすメッセージを渡し、listener.pyで受け取ったものを標準出力する。
### ビルド
````
colcon build
````
```
source ~/.bashrc
```
### 実行
```
ros2 launch mypkg talk_listen.launch.py
```
### 結果
```
[listener-2] [INFO] [1672222662.417031373] [listener]: Listen: 0
[listener-2] [INFO] [1672222662.903533239] [listener]: Listen: 1
[listener-2] [INFO] [1672222663.405118836] [listener]: Listen: 2
[listener-2] [INFO] [1672222663.904896988] [listener]: Listen: 3
[listener-2] [INFO] [1672222664.404957803] [listener]: Listen: 4
[listener-2] [INFO] [1672222664.904812236] [listener]: Listen: 5
```

## 環境
* Ubuntu 22.04

## ライセンス

  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * © 2022 Takuto Kanno
