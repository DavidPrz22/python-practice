import pandas as pd
import matplotlib.pyplot as plt
import requests
import pprint


from bs4 import BeautifulSoup


def main():

    product_titles = []

    for i in range(1, 5):
        urll = f"https://www.amazon.com/s?i=fashion-luggage&rh=n%3A9479199011%2Cp_36%3A2661612011&s=featured-rank&page={i}&language=es&content-id=amzn1.sym.e8166536-0a9e-4ac7-adba-207c4e685029&pd_rd_r=d15c0c6e-df47-44f4-9a2d-4150c769b0aa&pd_rd_w=tfAJS&pd_rd_wg=xZym6&qid=1738641376&xpid=a_eyzjoVRL_mV&ref=sr_pg_{i}"
        url = f"https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A193870011&language=es&qid=1738468469&refresh=1&xpid=HiER_QO91f5Mi&ref=sr_pg_{i}"
        website_data = fetch_data_from_url(url)
        cards = website_data.select(".s-card-container")

        for card in cards:

            title = card.select('[data-cy="title-recipe"] a')[0]

            reviews_block = card.select('[data-cy="reviews-block"]')[0]
            stars = reviews_block.select('[data-cy="reviews-ratings-slot"]')[0]

            reviews_count = reviews_block.select(
                '[data-csa-c-content-id="alf-customer-ratings-count-component"]'
            )[0]

            price_container = card.select('[data-cy="price-recipe"]')[0]
            price = price_container.select("span.a-offscreen")[0] if price_container.select("span.a-offscreen") else None


            product_titles.append(
                {
                    "product": title.text,
                    "price": float(price.text.replace("US$", "")) if price else 0,
                    "reviews": reviews_count.text.strip(),
                    "href": "amazon.com" + title.get("href"),
                }
            )

    amazon_data = pd.DataFrame(product_titles)

    indices = amazon_data[amazon_data["href"] == "amazon.comjavascript:void(0)"].index
    amazon_data = amazon_data.drop(indices)
    amazon_data = amazon_data.reset_index(drop=True)

    amazon_data.to_csv("amazon_prices_clothes.csv")


def fetch_data_from_url(url):
    agent = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "accept-language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    }

    res = requests.get(url, headers=agent)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


if __name__ == "__main__":
    main()
