from src.extract import extract_data
from src.transfrom import transfrom_data
from src.load import load_data

data = extract_data("https://books.toscrape.com/catalogue/page-1.html")

transfrom = transfrom_data(data)

load = load_data(transfrom)

# print(transfrom)