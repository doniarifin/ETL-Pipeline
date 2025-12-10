import os
from dotenv import load_dotenv

from src.extract import extract_data
from src.transfrom import transfrom_data
from src.load import load_data

def run_etl():
  # load environment variables from .env file
  load_dotenv()

  # access the variables
  db_name = os.getenv("db")
  host = os.getenv("host")
  port = os.getenv("port")
  user = os.getenv("user")
  password = os.getenv("password")

  variables = {
    "db_name": db_name,
    "host": host,
    "port": port,
    "user": user,
    "password": password,
  }

  data = extract_data("https://books.toscrape.com/catalogue/page-1.html")

  transfrom = transfrom_data(data)

  load = load_data(transfrom, variables)

  # print(transfrom)

if __name__ == "__main__":
  run_etl()