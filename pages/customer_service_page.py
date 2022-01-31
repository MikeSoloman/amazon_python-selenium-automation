from pages.base_page import Page
from selenium.webdriver.common.by import By


class CustomerServicePage(Page):
    CUSTO_SERVICE_LINK = "https://www.amazon.com/gp/help/customer/display.html"
    GREETING_CUSTO = By.CSS_SELECTOR, "div[class *= ss-landing-container] h1"
    MIDDLE_DIV_ELEMENTS = By.XPATH, "//div[@class = 'a-column a-span12'] // div[@class = 'a-box-inner']"
    BOTTOM_DIV_ELEMENTS = By.XPATH, "//div[contains(@class, 'categories')] // li"

    def open_customer_service_page(self):
        self.open_page(self.CUSTO_SERVICE_LINK)

    def verify_greeting(self, text):
        self.verify_text(text, *self.GREETING_CUSTO)

    def verify_middle_div_elements(self, num):
        self.count_links(num, *self.MIDDLE_DIV_ELEMENTS)

    def verify_bottom_div_elements(self, num):
        self.count_links(num, *self.BOTTOM_DIV_ELEMENTS)
