---
title: "Shadowverse MOD画像変換ソフトHohatchについて"
date: 2026-01-06
draft: false
description: "開発したHoHatchに付いて紹介する。HoHatchはShadowverse: Worlds BeyondのMOD作成の支援のため、JPG・DDS画像の変換および、DDS画像の管理を行うアプリケーションである。"
tags: ["hohatch"]
---

## HoHatch とは？

2025/8/29に初リリースを[GitHubに公開](https://github.com/dracoboost/hohatch/tree/c94031b6fdacf581d5993a0c7be9bc4df188a04d)し、2025/10/5に[Redditに公開](https://www.reddit.com/r/ShadowverseMods/comments/1naxk3j/hohatch_streamline_shadowversewb_modding/)したHoHatchについて紹介する。

HoHatch (ダウンロード先 **[dracoboost/hohatch Releases Page](https://github.com/dracoboost/hohatch/releases)**) は  
Windows用インジェクションソフトウェアSpecial Kを用いた[**Shadowverse: Worlds Beyond**](https://shadowverse-wb.com/en/) (以下、ビヨンド) への  
MOD作成の支援のため、JPG・DDS画像の変換および、DDS画像の管理を行うアプリケーションである。  

(ちなみに、一般に、モバイルOSはセキュリティのためアプリへのインジェクションは難しいため、Android, iOSにおけるビヨンドのModdingは非常に難しい。)  

ビヨンドのMOD作成者にとって、  
MOD画像の作成以外に時間を割くのは非常に憂鬱である。  
MOD画像の作成には、ビヨンドアプリのリソースファイルからのオリジナルDDS ([DirectDraw Surface](https://en.wikipedia.org/wiki/DirectDraw_Surface)) 画像の抽出、
DDS画像からJPG画像への変換、MOD済みJPG画像の作成、そのJPG画像からDDS画像への変換という工程が必要となる。

そこで、画像ファイルの管理と変換を効率的かつ直感的に行えるDDS・JPG間の画像変換器として、デスクトップアプリHoHatchを制作した。  
これにより、画像作成の部分により集中することができるだろう。

![HoHatch Application Screenshot](/images/hohatch/hohatch-application-screenshot.jpg)

― 以下の内容は、hohatch.draco.moeに以降予定 ―

## 主な機能

メイン画面と設定画面の2画面がある。

### メイン画面

メイン画面には画像変換の機能がある。

* **Dump済みDDS画像**: SpecialKにより、ビヨンドアプリのリソースファイルから抽出されたオリジナルDDS画像。
* **Inject済みDDS画像**: MODが完了した画像であり、ビヨンドアプリに挿入される。挿入先は`XXXXXXXX.dds`のようなファイル名により規定されている。

次に、各DDS画像をホバーした際に表示されるボタンについて説明する。

* **JPG to DDS**: 改変JPG画像を、ビヨンドアプリで読み込む形式であるDDS画像に変換し、自動的に`inject/textures`フォルダに配置する。
* **DDS to JPG**: Convert dumped DDS files into JPGs, so you can easily edit them in your favorite image editor.

一括変換機能について説明する。画像名`XXXXXXXX`の部分をクリックして複数の画像を選択すると、`保存 (現在の名称はダウンロード)`・`削除`ボタンが表示される。

* **保存**: 選択画像を一括でJPGとして、ダイアログで指定したフォルダ内に保存する。
* **削除**: 選択画像を一括で削除します。「一つ戻る」機能がないため、慎重に削除してください。

### 設定画面 (歯車アイコンから遷移)

上から、`言語`、`Special Kフォルダパス`、`保存JPGサイズ (アスペクト比53:64か否か選択可能)`、`システムフォルダ`の設定を行う。

* `言語`: 日本語か英語かを選択する。
* `Special Kフォルダパス`: ダウンロードしたSpecial Kの実行ファイルがあるフォルダを指定する。
* `保存JPGサイズ`: カード画像はアスペクト比53:64で保存するとよい。
* `システムフォルダ`: キャッシュフォルダ、ログフォルダを開けることができる。バグがあった場合は、DiscordかXで私に

## Tips

エクスプローラー上でDDS画像のイラストが表示されない場合、DDS画像に対応した画像編集ソフト ([paint.net](https://www.getpaint.net)など) をインストールすると良い。

---

## 今後の展望

* 現在DDS・PNG画像間の変換機能が実装できていない。  
  これは、TexconvがPNG画像を入れたときに真っ黒の画像を生成してくるという問題があったためである。  
  解決するには変換方法を抜本的に変える必要がありそうなので、放置している。

## コントリビューター向け

今のところ HoHatch (**[dracoboost/hohatch](https://github.com/dracoboost/hohatch)**) は一人で作っている。  
ほとんど求めていた機能は完成したが、  
何か機能を追加したいかつ、Python、Next.jsを書ける人はぜひコントリビュートしていただきたい。

{{< github repo="dracoboost/hohatch" >}}

注意点としては、更新前にpreflightチェックが成功することを確認してほしい。
細かいガイドラインは、英語だが `GEMINI.md` を読んでほしい。

```sh
# From the frontend directory
cd frontend
npm run preflight
```
