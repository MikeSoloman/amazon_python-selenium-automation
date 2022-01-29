from pages.base_page import Page
from selenium.webdriver.common.by import By


class AmazonHelpPage(Page):
    AMAZON_HELP_PAGE_LINK = "https://www.amazon.com/gp/help/customer/display.html"
    SEARCH_LIBRARY = By.XPATH, "//input[@id='helpsearch']"
    SEARCH_TEXT_VERIFICATION = By.XPATH, "//h1"

    def go_to_amazon_help_page(self):
        self.open_page(self.AMAZON_HELP_PAGE_LINK)

    def search_library(self, query):
        self.input_text_no_enter_btn(query, *self.SEARCH_LIBRARY)

    def verify_search_text(self, query):
        self.verify_text(query, *self.SEARCH_TEXT_VERIFICATION)

