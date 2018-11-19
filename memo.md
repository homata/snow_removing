メモ
-----

### リアルタイム表示
* [リアルタイムグラフなら「とりあえずEpoch.js」をおススメしたい](https://qiita.com/okoppe8/items/d8d8bc4e68b1da4a0a36)

    * [chartjs-plugin-streaming](https://nagix.github.io/chartjs-plugin-streaming/samples/line-horizontal.html)
    
### jVector Maps
 * http://jvectormap.com/
* [jVectorMap - fast and easy plugin to display vector maps of the world](http://plugindetector.com/jvector-map)
* コピペで(ほぼ)一発！jQueryでオシャレな地図ツールを作ったよ。
    * http://www.procrasist.com/entry/map-tool
    * https://github.com/hokekiyoo/map_maker 

 #### 心拍計、ECG（心電図）
* [心拍センサ WHS-2](https://www.uniontool-mybeat.com/SHOP/8600043.html)
* [ハートレートセンサー HRM4-Run](https://www.garmin.co.jp/products/accessories/010-10997-13_010-01529-05/)
    - [Garmin ハートレートセンサーHRM4-Run で 乳酸閾値を測る](https://live-simply.hatenadiary.jp/entry/FA935-hrm4run)
    - [Garmin Connect](https://connect.garmin.com/ja-JP/)
* [Garmin Connect IQ プログラミング](http://yaonobibouroku.blogspot.com/p/blog-page_26.html)
   - [Connect IQ SDK](https://developer.garmin.com/connect-iq/sdk/)
   

### Web Bluetooth API 
* [Can I Use](https://caniuse.com/#feat=web-bluetooth)
    - Web Bluetooth APIのサポート状況 - Chromeのデスクトップ版とAndroid版、Android標準ブラウザ、Opera

* [Web Bluetooth API ](https://www.chromestatus.com/feature/5264933985976320)
    * [Web Bluetooth Samples](https://googlechrome.github.io/samples/web-bluetooth/)
* [GoogleChrome/samples](https://github.com/GoogleChrome/samples)
* [WebBluetoothCG/demos](https://github.com/WebBluetoothCG/demos)
* [Web Bluetooth APIを使って体温計のデータをブラウザでBLE経由で受信してみた](https://qiita.com/megadreams14/items/02f524540896449944cd)
* [Web Bluetooth (仕様)](https://webbluetoothcg.github.io/web-bluetooth/)

* [Web Bluetooth API を使ってBLEデバイスをブラウザから操作する](http://tkybpp.hatenablog.com/entry/2016/08/18/100000)


### Cordova

* [Cordovaを使って、Androidの実機実行するまで](https://qiita.com/cognitom/items/3b30284e8d01eaf122b7)
    * [Genymotion](https://qiita.com/cognitom/items/3b30284e8d01eaf122b7) 
* [[Ionic3] 開発環境の構築からAndroid実機デバッグまでの手順まとめ](https://qiita.com/alclimb/items/a266871625f1227f425d)
* [CordovaでHTML5ハイブリッドアプリ開発 - Android編](http://cordovaandroid.saetl.net/process2_5.html)
* [Chrome Inspectの使い方](http://android.akjava.com/html5/chromeinspect.html)


#### 実機で検証
    空のアプリを作成
    $ cordova create hello-app

    プラットフォームの追加
    $ cd hello-app
    $ cordova platform add browser
    $ cordova platform add android

    $ vi .gitignore
    platforms/*
    !platforms/platforms.json
    plugins

    エミュレータでの検証
    1. Genymotion.appを起動
    2. アプリケーション内で、VMをダウンロード (もしまだなければ)
    3. VMを起動
    4. Cordovaから起動 $ cordova run android

    実機で検証
    1. Android実機のUSBデバッグ機能をONに
    2. MacにAndroid実機をUSB接続 (USBケーブルが充電専用だとNGなので注意)
    3. 次のコマンドで接続確認して、表示されればOK $ adb devices
    4. Cordovaから起動 $ cordova run android
    5. ビルドを待つ...
    6. 実機でアプリが起動!
    7. パソコンでChrome://inspectを開く (Chromeブラウザーを使う)
