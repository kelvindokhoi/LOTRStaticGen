# Lord of the Rings Static Site Generator

## Overview

This project is a **static site generator** built as part of a [Boot.dev](https://www.boot.dev/) course. It recursively converts Markdown files into a structured HTML website with a *Lord of the Rings*-themed design. The generator, written in Python, uses standard libraries (`re`, `os`, `sys`, `shutil`) to parse Markdown and generate HTML pages. The site is hosted on GitHub Pages at [https://kelvindokhoi.github.io/LOTRStaticGen/](https://kelvindokhoi.github.io/LOTRStaticGen/).

## Features

- **Recursive Markdown Conversion**: Transforms Markdown files into HTML pages using recursive parsing.
- **Lord of the Rings Theme**: Styled with a custom *Lord of the Rings*-inspired design via `index.css`.
- **GitHub Pages Deployment**: Deploys the site from the `docs/` directory using a build script.
- **Modular Python Code**: Includes modules for Markdown parsing, HTML generation, and text node processing.
- **Customizable**: Modify Markdown files, CSS, or Python scripts to create new themes or content.
- **Test Suite**: Includes unit tests for validating Markdown parsing and HTML generation.
- **No External Dependencies**: Uses only standard Python libraries (`re`, `os`, `sys`, `shutil`).

## Live Demo

Visit the live site at [https://kelvindokhoi.github.io/LOTRStaticGen/](https://kelvindokhoi.github.io/LOTRStaticGen/) to explore the *Lord of the Rings*-themed website.

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/) (includes `re`, `os`, `sys`, `shutil`).
- A modern web browser (e.g., Chrome, Firefox, Edge).
- A code editor (e.g., VS Code, Sublime Text).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kelvindokhoi/LOTRStaticGen.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LOTRStaticGen
   ```
   *Note*: No additional dependencies are required, as the project uses standard Python libraries.

### Running Locally

To generate the site and preview it locally:

1. Run the generator and start a local server:
   ```bash
   ./main.sh
   ```
   This executes `python3 src/main.py` to generate HTML files in the `public/` directory and starts a local server at `http://localhost:8888` using `python3 -m http.server 8888`.
2. Open `http://localhost:8888` in a web browser to view the site.

### Building for GitHub Pages

To generate the site and deploy it to GitHub Pages:

1. Run the build script:
   ```bash
   ./build.sh
   ```
   This executes `python3 src/main.py '/LOTRStaticGen/'` to generate HTML files and copy them to the `docs/` directory, using `/LOTRStaticGen/` as the repository name for correct URL paths.
2. Commit and push the changes to the `main` branch:
   ```bash
   git add docs/
   git commit -m "Update GitHub Pages content"
   git push origin main
   ```
3. The updated site will be available at [https://kelvindokhoi.github.io/LOTRStaticGen/](https://kelvindokhoi.github.io/LOTRStaticGen/).

### Usage

1. **Add Markdown Files**: Place Markdown files in the `content/` directory (e.g., `content/index.md`, `content/blog/glorfindel/index.md`) to define site content.
2. **Run the Generator**: Use `./main.sh` to generate HTML files in the `public/` directory for local testing, or `./build.sh` to generate files for GitHub Pages in `docs/`.
3. **Customize the Theme**: Edit `static/index.css` to modify the *Lord of the Rings* theme or create a new design.
4. **Extend Functionality**: Modify Python scripts in `src/` (e.g., `generate_page.py`, `markdown_to_html_node.py`) to add new features or Markdown support.
5. **Run Tests**: Execute unit tests to verify functionality:
   ```bash
   ./test.sh
   ```

## Project Structure

```
LOTRStaticGen/
├── content/                  # Markdown files for site content
│   ├── blog/                 # Blog section Markdown files
│   │   ├── glorfindel/index.md
│   │   ├── majesty/index.md
│   │   └── tom/index.md
│   ├── contact/index.md
│   └── index.md
├── docs/                     # GitHub Pages deployment directory
│   ├── blog/                 # Generated HTML for blog
│   │   ├── glorfindel/index.html
│   │   ├── majesty/index.html
│   │   └── tom/index.html
│   ├── contact/index.html
│   ├── images/               # Image assets
│   │   ├── glorfindel.png
│   │   ├── rivendell.png
│   │   ├── tolkien.png
│   │   └── tom.png
│   ├── index.css             # CSS stylesheet
│   └── index.html            # Homepage
├── public/                   # Generated HTML output (ignored by .gitignore)
│   ├── blog/                 # Generated HTML for blog
│   │   ├── glorfindel/index.html
│   │   ├── majesty/index.html
│   │   └── tom/index.html
│   ├── contact/index.html
│   ├── images/               # Copied image assets
│   │   ├── glorfindel.png
│   │   ├── rivendell.png
│   │   ├── tolkien.png
│   │   └── tom.png
│   ├── index.css
│   └── index.html
├── src/                      # Python source code for the generator
│   ├── block_to_blocktype.py
│   ├── blocktype.py
│   ├── extract_markdown_images.py
│   ├── extract_markdown_links.py
│   ├── extract_title.py
│   ├── generate_page.py
│   ├── generate_pages_recursive.py
│   ├── htmlnode.py
│   ├── main.py               # Main generator script
│   ├── markdown_to