---
title: "About HoHatch – Shadowverse MOD Image Conversion Tool"
date: 2026-01-06
lastmod: 2026-02-08
draft: false
description: "Introducing HoHatch, a tool developed to assist with MOD creation for Shadowverse: Worlds Beyond. It handles conversion between JPG and DDS images, as well as management of DDS files."
tags: ["hohatch"]
---

## What is HoHatch?

*HoHatch** (Download: [HoHatch - the JPG/DDS converter for modding ShadowverseWB](https://hohatch.draco.moe)) is a Windows desktop application designed to support MOD creation for  
[**Shadowverse: Worlds Beyond**](https://shadowverse-wb.com/en/) (hereinafter referred to as "ShadowverseWB") using the Special K injection tool.  
It specializes in converting between JPG and DDS formats and managing DDS texture files.

For ShadowverseWB MOD creators, spending time on anything other than the actual artwork creation process can be very frustrating.  
The typical workflow for creating MOD images includes:

* Extracting original DDS files from the game using Special K  
* Converting those DDS files to editable JPGs  
* Editing/modifying the JPGs  
* Converting the edited JPGs back to DDS format for injection

HoHatch was created to streamline and make the image conversion and file management part of this workflow as efficient and intuitive as possible, allowing creators to focus more on the creative artwork itself.

![HoHatch Application Screenshot](/images/hohatch/hohatch-application-screenshot.jpg)

## Future Plans

* DDS ↔ PNG conversion is not yet implemented.  
  When using texconv with PNG input, it often produces completely black output.  
  Fixing this issue likely requires a fundamental change in the conversion pipeline, so it has been postponed for now.

## For Contributors

Currently, I'm the only one developing HoHatch (**[dracoboost/hohatch](https://github.com/dracoboost/hohatch)**).  
Most of the core features I personally needed have already been implemented, but  
if you would like to add new features and are comfortable writing **Python** and/or **Next.js**, contributions are very welcome!

{{< github repo="dracoboost/hohatch" >}}

Please make sure the preflight check passes before submitting updates.  
For detailed guidelines (in English), please read `GEMINI.md`.

```sh
# From the frontend directory
cd frontend
npm run preflight
```
