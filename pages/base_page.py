from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def input_text_no_enter_btn(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text, Keys.ENTER)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelemnt (ex. (By.ID, 'id') )
        """
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_url(self, expected_text: str):
        actual_url = self.driver.current_url
        assert expected_text in actual_url, f"Expected {expected_text} does not match actual url"
        # we could also use self.driver.wait.until(expected_conditions.url_contains)

    def count_links(self, expected_number: str, *locator):
        actual_number = self.driver.find_elements(*locator)
        assert int(expected_number) == len(
            actual_number), f"Expected was {expected_number} and actual is {len(actual_number)} "
