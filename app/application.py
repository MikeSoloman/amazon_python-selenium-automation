from pages.amazon_help_page import AmazonHelpPage
from pages.best_sellers_page import BestSellersPage
from pages.create_account_page import CreateAccountPage
from pages.customer_service_page import CustomerServicePage
from pages.main_page import MainPage
from pages.product_page import ProductPage
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
        self.best_sellers_page = BestSellersPage(self.driver)
        self.customer_service_page = CustomerServicePage(self.driver)
        self.product_page = ProductPage(self.driver)
