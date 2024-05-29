import httpx
from parsel import Selector

class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        print("Статус код: ", response.status_code)
        return response.text

    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("div.list-item-title a::attr(href)").getall()
        links = list(map(lambda x: self.BASE_URL + x, links))
        return links

def get_links():
    crawler = HouseCrawler()
    page = crawler.get_page()
    links = crawler.get_links(page)
    return links