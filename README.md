# ETL-Pipeline

This repository provides a simple example of an ETL Pipeline built using Python.
In this case study, data is collected through web scraping, processed, and then loaded into a MySQL database.

## ETL Architecture

`src/extract.py`

The script performs web scraping to collect raw data from the target website.HTML content is parsed and converted into a structured format (dictionary / DataFrame).

`src/transfrom.py`

The retrieved data is cleaned and transformed, such as trimming whitespace, formatting dates, or normalizing text. Basic validation is applied before loading the data into MySQL.

`src/load.py`

The processed data is inserted into a MySQL table.

`main.py`

Entry Point. It loads environment variables, initializes the pipeline, and runs Extract → Transform → Load in sequence.

`.env_copy`

a file that provides the full list of environment variables required by the .env configuration file.

---

## How to Run ETL Pipeline

### Run Project with CLI

#### Requirements

- Python 3+
- MySQL
- Command Line Interface

#### Start

1. install module in virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. copy .env_copy to .env, ensure to set into your mysql config

```
cp .env_copy .env
```

3. Run entry point

```
python3 main.py
```
