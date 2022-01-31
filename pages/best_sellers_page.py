from pages.base_page import Page
from selenium.webdriver.common.by import By


class BestSellersPage(Page):
    BEST_SELLERS_LINKS = By.CSS_SELECTOR, "div[class *= style_zg-tabs__EYPLq] li"

    def best_sellers_url_verif(self, text):
        self.verify_url(text)

    def link_count(self, num):
        self.count_links(num, *self.BEST_SELLERS_LINKS)
