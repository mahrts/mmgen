# 🎭 Meme Generator
A simple Python package that generates memes by combining **random images and quotes**..

---

## ✨ Features
- 🖼️ Combine images and quotes into memes
- ✏️ Automatic text wrapping and and random positioning of the text on the image
- 📂 Load quotes from various file formats (.txt, .pfd, .csv, .docx)
- 🎲 Combine and generate random memes
- 🧩 Modular Python architecture
- ⚡ Simple command-line interface
- 🌐 Runs on flask server, and can ingest image input from url

- Structure:

├── pyproject.toml
├── requirements.txt
├── src
│   ├── app.py
│   ├── _data
│   ├── main.py
│   ├── MemeGenerator
│   │   ├── fonts
│   │   ├── __init__.py
│   │   └── MemeGenerator.py
│   ├── QuoteEngine
│   │   ├── __init__.py
│   │   └── QuoteEngine.py
│   ├── README.md
│   ├── static
│   └── templates
│       ├── base.html
│       ├── meme_form.html
│       └── meme.html
└── tests
    └── test_quoteengine.py

# 📦 Installation

Clone the repository: git clone https://github.com/mahrts/mmgen,
and install the package:

```bash
cd mmgen
pip install -e .
```

Or install dependencies only:

```bash
pip install -r requirements.txt
```

---

## Usages

The project can be used in two ways: via the **command-line interface (CLI)** or by running the **Flask web server**.

### 1. Command-line interface

Run the main script with:

```bash
python main.py
```

Run the following for help, and and see all possible optional arguments:

```bash
python main.py --help
```
---

### 2. Run the Flask server

Start the web server:

```bash
flask --app app run
```

and open the resulting address in your browser to interact with the application.

---

## Running tests

```bash
pytest
```

---

# 🙌 Acknowledgments

This project is from Intermediate Python nanodegree of Udacity
https://www.udacity.com/course/intermediate-python-nanodegree--nd303