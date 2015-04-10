# book_manager_server

サーバーを構築して実際に動かすまでの手順を示す。

##実行環境の作成方法
- - - - -
実機に仮想OSを立てて、仮想サーバーとやりとりをできるようにする。
行う手順は以下の通り。

1. VirtualBox + Vagrantのインストール
2. 仮想環境の構築
3. 動作確認

###1: VirtualBox + Vagrant のインストール
インストール済みだったら飛ばして次へ。

それぞれを簡単に説明すると

- VirtualBox: 仮想化ソフトウェア・パッケージ。仮想OS環境を構築してくれる。
- Vagrant: 仮想環境作成ツール。上記の仮想環境の設定を指定しておけば勝手に実行環境を作ってくれる。

というもの。

ダウンロードページはこちら

- VitrualBox:https://www.virtualbox.org/wiki/Downloads
- Vagrant:https://www.vagrantup.com/downloads.html

確認としてはターミナルで

```
 vagrant -v
```
とコマンドを入力してversionが返ってこればOK。

###2:仮想環境の構築
まずは仮想環境を動かすためのディレクトリを作成し、そこにリポジトリーのVagrantfileとboxを置く。
ちなみに

- vagrantfile: vagrantで環境を作る手順ファイル
- box: 構築する環境の設計図

ぐらいに認識してもらえれば大丈夫。

以下のコマンドを実行

```
$ vagrant box add bookmanager bookmanager.box 
$ vagrant up
```

これで仮想マシンの実行が行われる。

マシンへの接続は

```
$ vagrant ssh
```

で行う。

###3:動作確認

構築した仮想サーバーにアクセスしてちゃんと動くかを確認。

まずはnginxとuWSGIの起動。nginxはすでに動いているが念のために再起動を行うと良いと思われる。

```
$ sudo service nginx restart
$ uwsgi --ini ~/book_manager_server/setting/uwsgi.ini
```

本当にサーバーにアクセスできるかを確認する。

実機にてhostsの指定を行う。/etc/hostsを書き加えてやる。

```
  1 ##
  2 # Host Database
  3 #
  4 # localhost is used to configure the loopback interface
  5 # when the system is booting.  Do not change this entry.
  6 ##
  7 127.0.0.1>localhost
  8 255.255.255.255>broadcasthost
  9 ::1             localhost-
 10 192.168.33.10 app.com 
```

上記の10行目を追加してやればいい。

これでブラウザでapp.comにアクセスしてできたら環境構築完了。
