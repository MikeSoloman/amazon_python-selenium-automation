from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    MAIN_PAGE = 'https://www.amazon.com'
    SEARCH_FIELD = By.ID, 'twotabsearchtextbox'
    SEARCH_ICON = By.ID, 'nav-search-submit-button'
    BEST_SELLERS_PAGE = By.CSS_SELECTOR, ".nav-fill a[href*='cs_bestsellers']"

    def open_main_page(self):
        self.open_page(self.MAIN_PAGE)

    def input_amazon_text(self, item):
        self.input_text(item, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)

    def verify_logo_url(self):
        self.verify_url('logo')

    def click_on_best_sellers_page_link(self):
        self.click(*self.BEST_SELLERS_PAGE)
