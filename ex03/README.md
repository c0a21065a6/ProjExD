# 第3回
##　迷路ゲーム:迷えるこうかとん(ex03/maze.py)
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する

### 操作方法
- 矢印キーでこうかとんを上下左右に移動する

### 追加機能
- スタート地点とゴール地点の追加：スタート地点をランダムに決定し，ゴール地点をスタートから最も遠い場所に設定する機能を追加した．
- ゴールのメッセージ:ゴールした際に"Congratulations"と表示されるようにした
- 敵:敵を表示し，衝突した際にスタート地点に戻るようにした
- 敵の増加:敵を2体にした
- スタートに戻る:ゴールしたらスタートに戻るようにした
### ToDo（実装しようと思ったけど時間がなかった）
- 

### メモ
- 壁に当たったとき警告を出そうとしたが，操作をやめても警告が出続けてしまうため断念
- スタートの際にtkinterで開始の旨を表示しようとしたが，表示するとこうかとんが動かなくなってしまったため断念
- 敵がこうかとんに近づいていくようにしたかったが，敵が動かなくなってしまったため断念