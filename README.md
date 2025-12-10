# ETL-Pipeline

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
