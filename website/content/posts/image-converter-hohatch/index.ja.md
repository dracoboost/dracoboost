---
title: "Shadowverse MOD画像変換ソフトHohatchについて"
date: 2026-01-06
lastmod: 2026-02-08
draft: false
description: "開発したHoHatchに付いて紹介する。HoHatchはShadowverse: Worlds BeyondのMOD作成の支援のため、JPG・DDS画像の変換および、DDS画像の管理を行うアプリケーションである。"
tags: ["hohatch"]
---

## HoHatch とは？

HoHatch (ダウンロード先：[HoHatch - the JPG/DDS converter for modding ShadowverseWB](https://hohatch.draco.moe)) は  
Windows用インジェクションソフトウェアSpecial Kを用いた[**Shadowverse: Worlds Beyond**](https://shadowverse-wb.com/en/) (以下、シャドバWB) への  
MOD作成の支援のため、JPG・DDS画像の変換および、DDS画像の管理を行うアプリケーションである。  

シャドバWBのMOD作成者にとって、  
MOD画像の作成以外に時間を割くのは非常に憂鬱である。  
MOD画像の作成には、シャドバWB本体のアプリのリソースファイルからのオリジナルDDS ([DirectDraw Surface](https://en.wikipedia.org/wiki/DirectDraw_Surface)) 画像の抽出、
DDS画像からJPG画像への変換、MOD済みJPG画像の作成、そのJPG画像からDDS画像への変換という工程が必要となる。

そこで、画像ファイルの管理と変換を効率的かつ直感的に行えるDDS・JPG間の画像変換器として、デスクトップアプリHoHatchを制作した。  
これにより、画像作成の部分により集中することができるだろう。

![HoHatch Application Screenshot](/images/hohatch/hohatch-application-screenshot.jpg)

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
