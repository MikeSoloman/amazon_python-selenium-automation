from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    MAIN_PAGE = 'https://www.amazon.com'
    SEARCH_FIELD = By.ID, 'twotabsearchtextbox'
    SEARCH_ICON = By.ID, 'nav-search-submit-button'

    def open_main_page(self):
        self.open_page(self.MAIN_PAGE)

    def input_amazon_text(self, item):
        self.input_text(item, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)

    def verify_logo_url(self):
        self.verify_url('logo')
