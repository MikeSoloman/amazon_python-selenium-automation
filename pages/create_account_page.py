from pages.base_page import Page
from selenium.webdriver.common.by import By


class CreateAccountPage(Page):
    VERIFICATION_TEXT = By.XPATH, "//h1"
    CREATE_URL = "https://www.amazon.com/ap/register?showRememberMe=true&openid" \
                 ".pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazo" \
                 "n.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&prevRID=64" \
                 "7T6JG416SPYVYQA0K7&openid.identity=http%3A%2F%2Fspecs.openid." \
                 "net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usfle" \
                 "x&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignIn" \
                 "Count=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth" \
                 "%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%" \
                 "2Fspecs.openid.net%2Fauth%2F2.0"
    CREATE_YOUR_ACCOUNT_BTN = By.CSS_SELECTOR, "input#continue.a-button-input"
    NAME_LOCATOR = By.CSS_SELECTOR, "div.a-row.a-spacing-base input[name = 'customerName']"
    EMAIL_LOCATOR = By.CSS_SELECTOR, "#ap_email"
    PASSWORD1_LOCATOR = By.CSS_SELECTOR, "div.a-row.a-spacing-base input[name = 'password']"
    PASSWORD2_LOCATOR = By.CSS_SELECTOR, "div.a-row.a-spacing-base input[name = 'passwordCheck']"
    SOLVE_PUZZLE_TEXT = By.CSS_SELECTOR, "div.a-row.a-spacing-mini span.a-size-large"

    def verify_create_account_page(self, text):
        self.verify_text(text, *self.VERIFICATION_TEXT)

    def open_create_account_page(self):
        self.open_page(self.CREATE_URL)

    def verify_create_url(self, text):
        self.verify_url(text)

    def fill_up_name(self, text):
        self.input_text(text, *self.NAME_LOCATOR)

    def fill_up_email(self, text):
        self.input_text(text, *self.EMAIL_LOCATOR)

    def fill_up_password_fields(self, text):
        self.input_text(text, *self.PASSWORD1_LOCATOR)
        self.input_text(text, *self.PASSWORD2_LOCATOR)

    def click_on_create_account_btn(self):
        self.click(*self.CREATE_YOUR_ACCOUNT_BTN)

    def solve_puzzle(self, text):
        self.verify_text(text, *self.SOLVE_PUZZLE_TEXT)


