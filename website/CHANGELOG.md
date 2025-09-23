<p align="center">
  <a href="https://github.com/dracoboost/dracoboost" target="_blank">
    <img alt="dracoboost" src="https://raw.githubusercontent.com/dracoboost/dracoboost/master/website/public/images/logos/dracoboost-blog-logo.png" height="60">
  </a>
  <span>Website 📝CHANGELOG</span>

  <p align="center">
    <a href="https://github.com/dracoboost/dracoboost/releases">
      <img alt="website version" src="https://img.shields.io/badge/website%20version-0.1.1-lightgrey">
    </a>
  </p>
</p>

> [!TIP]
> All notable changes to this project will be documented in this file.
> The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2025-09-24

### Added

- GitHub Actions workflow for automated website releases (`.github/workflows/release_website.yml`).
- Programmatic sitemap generation (`app/sitemap.xml/route.ts`) for improved SEO.
- Dynamic `robots.txt` generation (`app/robots.ts`) for search engine directives.
- Initial `CHANGELOG.md` for the website to document all notable changes.

## [0.1.0] - 2025-09-23

### Added

- Initial project setup using Next.js, React, TypeScript, and Tailwind CSS.
- Main page structure with Profile, Projects, and Blog sections.
- Core components including `site-header`, `site-footer`, and `markdown-renderer`.
- Blog functionality to render articles from Markdown files.
- Basic theme and styling implementation.

[unreleased]: https://github.com/dracoboost/dracoboost/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/dracoboost/dracoboost/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/dracoboost/dracoboost/releases/tag/v0.1.0
