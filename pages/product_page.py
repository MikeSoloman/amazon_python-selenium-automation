from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    PRODUCTS_WHOLEFOODS = By.CSS_SELECTOR, "li.s-result-item div[class *= 'a-text-left']"
    WHOLEFOODS_PAGE = 'https://www.amazon.com/wholefoodsdeals'
    expected_colors = ["Black", "Dark Blue Vintage", "Dark Indigo/Rinsed", "Dark Wash", "Indigo Wash",
                       "Light Blue Vintage", "Light Wash", "Medium Blue, Vintage", "Medium Wash",
                       "Rinsed", "Vintage Wash", "Washed Black", "Bright White", "Dark Khaki Brown",
                       "Light Khaki Brown", "Olive", "Sage Green", "Blue, Over Dye", "Blue, Dip Dye"]
    GET_TEXT = By.CSS_SELECTOR, "div.a-row span.selection"
    PRODUCT_B07BJL37GD = "https://www.amazon.com/gp/product/B07BJL37GD"
    ACTUAL_COLORS = By.XPATH, "//div[@id = 'variation_color_name'] //li"
    REGULAR_TEXT = By.CSS_SELECTOR, ".a-row span[class *= 'card__regular-price']"
    PRODUCT_NAME_WHOLEFOODS = By.CSS_SELECTOR, ".a-row span[class *= 'product-name a-text-bold']"

    def open_product_B07BJL37GD(self):
        self.open_page(self.PRODUCT_B07BJL37GD)

    def verifying_colors(self):
        actual_colors = self.driver.find_elements(*self.ACTUAL_COLORS)

        # 1st way
        # print(actual_colors)
        # for num in range(len(actual_colors)):
        #     actual_colors[num].click()
        #     selected_color = self.driver.find_element(*self.GET_TEXT).text
        #     print(self.expected_colors[num])
        #     print(selected_color)
        #     assert selected_color == self.expected_colors[num], f"Expected color was {self.expected_colors[num]}," \
        #                                                         f" but the actual is {selected_color}"

        # 2nd way
        for num in range(len(actual_colors)):
            actual_colors[num].click()
            selected_color = self.driver.find_element(*self.GET_TEXT).text
            print(selected_color)
            assert selected_color in self.expected_colors, f"Expected color was {self.expected_colors[num]}," \
                                                           f" but the actual is {selected_color}"

    def open_wholefoods_page(self):
        self.open_page(self.WHOLEFOODS_PAGE)

    def check_regular_and_item_name(self, txt):
        regular_items = self.driver.find_elements(*self.REGULAR_TEXT)
        all_items_names = self.driver.find_elements(*self.PRODUCT_NAME_WHOLEFOODS)

        # 1st way
        # for num in range(len(regular_items)):
        #     item_regular = regular_items[num].text
        #     print(item_regular)
        #     item_name = all_items_names[num].text
        #     print(item_name)
        #     assert item_name, f"No item name is present"
        #     assert txt in item_regular, f"Expected text {txt}, doesn't match {item_regular}"

        # 2nd way

        products_list = self.driver.find_elements(*self.PRODUCTS_WHOLEFOODS)
        for item in products_list:
            assert txt in item.text, f"Regular is not preset"
            item_name = item.find_element(*self.PRODUCT_NAME_WHOLEFOODS).text
            assert item_name, f"No item name is present"
            print(item_name)

