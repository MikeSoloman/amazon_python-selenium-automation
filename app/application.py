from pages.amazon_help_page import AmazonHelpPage
from pages.create_account_page import CreateAccountPage
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.amazon_help_page = AmazonHelpPage(self.driver)
        self.create_account_page = CreateAccountPage(self.driver)
