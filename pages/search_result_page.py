from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):
    RESULT = By.CSS_SELECTOR, '.a-color-state.a-text-bold'

    def verify_search_text(self, results_word):
        self.verify_text(results_word, *self.RESULT)

    def verify_search_page_url(self, query):
        self.verify_url(query)
