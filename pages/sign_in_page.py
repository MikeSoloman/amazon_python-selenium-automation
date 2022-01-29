from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):
    SIGN_IN_PAGE_URL = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid' \
                       '.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&' \
                       'openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fident' \
                       'ifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&' \
                       'openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fide' \
                       'ntifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'

    AMAZON_LOGO = By.XPATH, "//a[@class = 'a-link-nav-icon']/i[@class = 'a-icon a-icon-logo']"
    EMAIL_PHONE_TEXT_VERIF_FIELD = By.XPATH, "//label[@for = 'ap_email']"
    EMAIL_PHONE_FILL_FIELD = By.XPATH, "//div[contains(@class, 'a-padding-extra-large')] // input[@id='ap_email'] "
    CONTINUE_BTN = By.XPATH, "//input[@id = 'continue']"
    INVALID_EMAIL_ERROR = By.XPATH, "//div[@class='a-alert-content'] // span[@class='a-list-item']"
    LEGAL_ROW_LINKS = By.XPATH, "//div[@id='legalTextRow'] // a[@href]"
    CONDITIONS_OF_USE_LINK = By.XPATH, "//div[@id='legalTextRow'] // a[contains(@href, 'nodeId=508088')]"
    CONDITIONS_OF_USE_TEXT = By.XPATH, "//h1"
    PRIVACY_NOTICE_LINK = By.XPATH, "//div[@id='legalTextRow'] // a[contains(@href, 'nodeId=468496')]"
    NEED_HELP_EXPANDER = By.XPATH, "//span[@class='a-expander-prompt']"
    NEED_HELP_ATTACHED_LINKS = By.XPATH, "//div[@class='a-section'] // div[@aria-expanded]"
    FOOTER_LINK_COUNT = By.XPATH, "//div[contains(@class, 'a-size-mini')]//a[@class = 'a-link-normal']"
    CREATE_YOUR_ACCOUNT_BTN = By.XPATH, "//a[@id='createAccountSubmit']"

    def open_sign_in_page(self):
        self.open_page(self.SIGN_IN_PAGE_URL)

    def sign_in_url_contains(self, text):
        self.verify_url(text)

    def click_on_amazon_logo(self):
        self.click(*self.AMAZON_LOGO)

    def fields_email_phone_verification(self, text):
        self.verify_text(text, *self.EMAIL_PHONE_TEXT_VERIF_FIELD)

    def fill_email_phone(self, text):
        self.input_text(text, *self.EMAIL_PHONE_FILL_FIELD)

    def click_continue_btn(self):
        self.click(*self.CONTINUE_BTN)

    def invalid_email_message(self, text):
        self.verify_text(text, *self.INVALID_EMAIL_ERROR)

    def legal_row_count_links(self, num):
        self.count_links(num, *self.LEGAL_ROW_LINKS)

    def conditions_of_use_verification(self, text):
        self.click(*self.CONDITIONS_OF_USE_LINK)
        self.verify_text(text, *self.CONDITIONS_OF_USE_TEXT)

    def privacy_notice_verification(self, text):
        self.click(*self.PRIVACY_NOTICE_LINK)
        self.verify_text(text, *self.CONDITIONS_OF_USE_TEXT)

    def help_expander(self, num):
        self.click(*self.NEED_HELP_EXPANDER)
        self.count_links(num, *self.NEED_HELP_ATTACHED_LINKS)

    def footer_link_count(self, num):
        self.count_links(num, *self.FOOTER_LINK_COUNT)

    def click_on_create_account_btn(self):
        self.click(*self.CREATE_YOUR_ACCOUNT_BTN)


