import requests
from bs4 import BeautifulSoup

def extract_data(url: str):
    print(f"Extract data from '{url}'")

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    items = soup.select("article.product_pod")
    titles = soup.select("h3 a")
    ratings = soup.select("p.star-rating")
    prices = soup.select("p.price_color")

    for index, _ in enumerate(items):
      title = titles[index].get("title")
      rating = ratings[index]["class"][1]
      price = prices[index].text.strip()

      data.append({
         "title": title,
         "rating": rating,
         "price": price
      })
    
    # print(data)
    return data


# if __name__ == "__main__":
#     extract("https://books.toscrape.com/catalogue/page-1.html")