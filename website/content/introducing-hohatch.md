---
title: "Introducing HoHatch: A Powerful Modding Tool for Shadowverse: Worlds Beyond"
date: "2025-09-23"
excerpt: "Discover HoHatch, the essential desktop app for Shadowverse: Worlds Beyond modders. Effortlessly convert, manage, and inject DDS/JPG image files with a modern, user-friendly interface."
thumbnail: "/images/hohatch/hohatch-application-screenshot.jpg"
author:
  name: "dracoboost"
  picture: "/avatars/dracoboost.png"
---

For modders of **Shadowverse: Worlds Beyond**, managing and converting image assets can be a tedious but necessary part of the creative process. Manually handling DDS and JPG files, ensuring they are in the correct format, and moving them to the right folders for injection with Special K is often a cumbersome workflow.

**HoHatch** is a desktop application built to solve exactly this problem. It provides a streamlined, intuitive interface for managing and converting image files, allowing you to focus on creating great mods, not fighting with file formats.

![HoHatch Application Screenshot](/images/hohatch/hohatch-application-screenshot.jpg)

## Key Features for Modders

HoHatch is designed with the modder's workflow in mind, offering a suite of powerful features accessible from a clean and modern UI.

### Seamless Image Conversion & Management

The main screen is your central hub for all image-related tasks. It's split into two clear sections:

* **Dumped DDS Images**: Images extracted from the game using Special K's dump feature. These are your raw materials for creating new mods.
* **Injected DDS Images**: Modded images ready to be injected into the game.

From here, you can perform several actions:

* **JPG to DDS**: Convert your edited JPG files into the DDS format required by the game and automatically place them in the `inject/textures` folder.
* **DDS to JPG**: Convert dumped DDS files into JPGs, so you can easily edit them in your favorite image editor.
* **Batch Operations**: Select multiple images and download them as JPGs or delete them in a single click, saving you valuable time.
* **Individual Actions**: Each image has quick-action buttons to download, replace, or delete it individually.

### Smart & Simple Settings

The settings screen gives you full control over how HoHatch works:

* **Dependency Downloads**: Instantly download the correct versions of **Texconv** and **Special K** directly from the app, ensuring you always have the right tools.
* **Custom Image Dimensions**: Set a desired height for your converted images, and HoHatch will automatically calculate the correct width (53/64 ratio) to prevent distortion in-game.
* **Language Toggle**: Switch between English and Japanese interfaces.

## Getting Started

HoHatch is a Windows-only application.

To get started, simply download the latest executable from the **[HoHatch Releases Page](https://github.com/dracoboost/hohatch/releases)** and run it. No complex installation is required.

---

## For Developers

Interested in the technology behind HoHatch or want to contribute?

HoHatch is built with a modern tech stack, featuring a **React** frontend (using Next.js and Tailwind CSS) and a **Python** backend powered by **PyWebView**. This architecture allows for a fast, responsive user interface combined with powerful backend processing.

The backend follows a service-oriented architecture, making the codebase modular, testable, and easy to maintain.

### Contributing

We welcome contributions! The project is hosted on GitHub. Before committing any changes, please ensure you run the pre-flight checks to maintain code quality and stability:

```sh
# From the frontend directory
cd frontend
npm run preflight
```

You can find more detailed development guidelines and a complete overview of the project structure in the `GEMINI.md` files within the repository.

Check out the project on our **[GitHub Repository](https://github.com/dracoboost/hohatch)** to learn more or get involved!
