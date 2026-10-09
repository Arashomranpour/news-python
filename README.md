<div align="center">

# 📰 News CLI

**Read the latest headlines from your terminal - search by keyword with a single command.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![NewsAPI](https://img.shields.io/badge/NewsAPI-top--headlines-informational)
![Windows](https://img.shields.io/badge/Windows-batch_launcher-0078D6?logo=windows&logoColor=white)

</div>

---

## ✨ Features

- 🗞️ Fetches popular English top headlines from [NewsAPI](https://newsapi.org/).
- 🔍 Search by keyword: `news apple`, `news america`.
- 📄 Prints the title, description and a link to read more for every article.
- 🪟 Includes a Windows launcher so `news` works from any `cmd` window.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A free [NewsAPI key](https://newsapi.org/register)

```bash
git clone https://github.com/Arashomranpour/news-python.git
cd news-python
pip install requests
```

Put your key in `news.py` (`api_key = "..."`, preferably loaded from an environment variable), then:

```bash
python news.py            # general news
python news.py apple      # headlines about "apple"
```

### Run as a command on Windows

1. Edit `news.bat` so it points to the full path of `news.py`.
2. Copy `news.bat` into a folder on your `PATH` (e.g. `C:\Windows\System32`).
3. Open `cmd` and run:

```bat
news america
```

## 📁 Project Structure

```
.
├── news.py     # NewsAPI client + CLI
└── news.bat    # Windows launcher
```

## 🛠️ Tech Stack

`Python` · `requests` · `NewsAPI`
