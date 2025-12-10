from extract import extract_data
from transfrom import transfrom_data
from load import load_data

data = extract_data("https://books.toscrape.com/catalogue/page-1.html")

transfrom = transfrom_data(data)

load = load_data(transfrom)

print(transfrom)