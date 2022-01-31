from behave import when, then, given
from selenium.webdriver.common.by import By


@given("Open Product Page")
def open_product_page(context):
    context.app.product_page.open_product_B07BJL37GD()


@then("Verify Expected colors match Actual Colors")
def verify_colors(context):
    context.app.product_page.verifying_colors()

@given("Open Amazon Wholefoods page")
def open_wholefoods(context):
    context.app.product_page.open_wholefoods_page()

@then("Verify that every product on the Wholefoods page has a text {txt} and a product name")
def verify_regular_and_name(context, txt):
    context.app.product_page.check_regular_and_item_name(txt)