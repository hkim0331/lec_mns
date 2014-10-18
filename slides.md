### 総合システムネットワーク講習会

総シスネットワークは夏休み頃から不調が目立つ。

#### 目的

* 卒論シーズンを迎え、問題点をクリアする。
* 不調の原因を作らないよう、最低限を覚える。
* [責任者メールリスト](lists.cgi)の作成。

この資料のアドレスは [どこかに](http://some.where) です。

----

### 知っておくべきこと

* 九工大ネットワークは脆弱。
* 一研究室のケアレスミスがサブネット全体のネットワークに影響する。
* デフォルトでつなぐと良くないことが起こる。

----

### 何が不調か？

* メールの送受信に時間がかかる。
* ファイル転送が遅い。
* リモートログインしての作業がとぎれとぎれ。
* 丸腰の Windows がネットワーク上に見える。

<pre>
dhcp30.mns.kyutech.ac.jp (150.69.84.30) at 00:0a:79:60:f5:f3 [ether] on eth0
dhcp37.mns.kyutech.ac.jp (150.69.84.37) at 00:3a:9d:20:ff:59 [ether] on eth0
dhcp35.mns.kyutech.ac.jp (150.69.84.35) at 20:c9:d0:2a:c2:6b [ether] on eth0
dhcp24.mns.kyutech.ac.jp (150.69.84.24) at 10:6f:3f:fc:b5:df [ether] on eth0
</pre>

----

### こんなことはない

前スライドの<span class='warn'>「丸腰 PC」</span>を除いて、

- パスワードやデータが漏れることはない。
- PCのデータが消えることはない。
- PCが知らない間に遠隔操作されることはない。

ただし、きちんとルータ下に収まった PC でも、
USBスティックやメールでウィルスを持ち込んでしまうことはある。
そんなのは別。守れない。

研究活動以外、YouTube や楽曲の違法ダウンロードでウィルス食らったやつは
<span class='warn'>自分で責任とれ</span>。

----

### 原因

研究室PCがウィルスに感染していないとしても、気になる点がいくつか。

* <span class='warn'>ケーブルの扱い</span>が雑。
* ルータ、ハブの役割を理解していない。
* ルータの設定を確認していない。九工大ネットはデフォルト値の使用を<span class='warn'>許していない</span>。
* 無線 AP にパスワード設定していない。
* 部屋が汚い。

----

### ケーブル

* きちんとしたケーブルを使わないと通信は安定しない。

[good cable](images/good_cable.jpg)

* きちんとしたケーブルは外被がプラグにきちっと押さえられている。

[bad cable 1](images/no_cover.jpg)

* きちんとしたケーブルはラッチが折れていない。差し込むと「カチっ」とはまり、少々引いても抜けない。

[bad cable 2](images/no_ratch.jpg)

----

### ルータ・ハブ

同じ箱に見えるが、役割はまったく違う。

<p><img src="images/router_hub.jpg" style="width:70%;"></p>

____

### ルータは上下を区別する

<p><img src="images/router_role.png" style="width:50%;"></p>

____

### ハブは上下の区別なし

<p><img src="images/hub_role.png" style="width:50%;"></p>

----

### 正：壁面からのケーブルにルータ、ルータとPCの間にハブ

<p><img src="images/router_hub.png" style="width:50%;"></p>

----

### 間違い：ハブがルータよりも上流にある

ルータとハブの場所が逆。守られているつもりで晒される PC。

<p><img src="images/hub_router.png" style="width:50%;"></p>

----

### ルータの向きを逆にすると他研究室も止める

ルータの向きが逆。

* 自分研究室のPCがネットにつながらない。
* 研究室のルータに間違いアドレスを提供してしまう。食らった研究室は全滅。

<p><img src="images/reverse_router.png" style="width:86%;"></p>

----

### 九工大ネットは IPv6 が嫌い

* デフォルトで
<span class='warn'>IPv6 ブリッジ</span>
の設定が生きているルータがある。設定を外すこと。
* デフォルトで Windows7 は <span class='warn'>IPv6 がイネーブル</span>されている。
設定を外すこと。
* 九工大ネットワークは IPv6 が嫌いだ。

<p><img src="images/ipv6_bridge.png" style="width:86%;"></p>

設定が確認できないときはつなぐな。

----
### 間違い例

空いているケーブルを収めたつもりだったが、研究室がネットワークから切り離される（ことになっているが、、、）

<p><img src="images/loop1.png" class="three"></p>

<p><img src="images/loop2.png" class="three"></p>


----
### 自分 PC の IP アドレスを知れ。

自分PCのIPアドレスみると、
* 自分PCが正しくルータの下に収まっているか、
* 九工大ネットが毛嫌いする IPv6 は有効か、無効か
を確認できる。

Windows なら「コマンドプロンプト」開いて ipconfig。IPAddress の右。


    > ipconfig
    Ethernet adapter ローカルエリア接続:
    IP Address ............: 192.168.10.3
    Subnet Mask ...........: 255.255.255.0
    Default Gateway .......: 192.168.10.1


OSXやLinuxはターミナル開いて ifconfig。inet addr: の右が IP アドレス。

    $ ifconfig
    eth0      Link encap:Ethernet  HWaddr 52:54:00:38:ce:ef
              inet addr:10.0.3.24  Bcast:10.0.3.255  Mask:255.255.255.0
              inet6 addr: fe80::5054:ff:fe38:ceef/64 Scope:Link
              ...

ifconfig の例にある fe80: で始まるようなのが見えるときは IPv6 が有効になっている。

----
### まとめ

* 知らずに使うな。
* ケーブルをあまく見るな。
* つながったからと安心するな。
* 大学院生を信用するな。
* 自分で考えろ。

<hr>
written by hkimura.

