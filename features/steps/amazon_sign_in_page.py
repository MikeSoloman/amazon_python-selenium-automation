from behave import when, given, then


@given("Open Amazon Sign-In Page")
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in_page()


@then("Verify {text} is present in the URL")
def url_verification(context, text):
    context.app.sign_in_page.sign_in_url_contains(text)


@when("Click on Amazon Logo")
def logo_click(context):
    context.app.sign_in_page.click_on_amazon_logo()


@then("Verify Amazon Logo takes to the home page")
def logo_takes_to_home_verification(context):
    context.app.main_page.verify_logo_url()
    context.driver.back()


@then("Verify Field: {text} is present")
def email_phone_field_verification(context, text):
    context.app.sign_in_page.fields_email_phone_verification(text)


@when("Fill up Email or mobile phone number field: {credentials}")
def fill_up_email_phone_field(context, credentials):
    context.app.sign_in_page.fill_email_phone(credentials)


@when("Click Continue btn")
def click_continue_button(context):
    context.app.sign_in_page.click_continue_btn()


@then("Verify user sees: {text}")
def email_error_message(context, text):
    context.app.sign_in_page.invalid_email_message(text)


@then("Verify there are {num} links in the Legal Text Row")
def num_of_links_verification(context, num):
    context.app.sign_in_page.legal_row_count_links(num)


@then("Verify {text} Link redirects to the right page")
def verify_conditions_link_and_text(context, text):
    context.app.sign_in_page.conditions_of_use_verification(text)
    context.driver.back()
    context.driver.refresh()


@then("Verify {text} redirects to the right page")
def privacy_notice_verification(context, text):
    context.app.sign_in_page.privacy_notice_verification(text)
    context.driver.back()
    context.driver.refresh()


@then("Verify Need help expander has {num} links visible once expanded")
def need_help_expander(context, num):
    context.app.sign_in_page.help_expander(num)


@then("Verify sign-in footer has {num} links present")
def sign_in_footer_link_verification(context, num):
    context.app.sign_in_page.footer_link_count(num)


@when("Click on Create your Amazon Account BTN")
def sign_in_page_account_create_btn(context):
    context.app.sign_in_page.click_on_create_account_btn()


@then("Verify user sees {text}")
def verify_create_account_page_text(context, text):
    context.app.create_account_page.verify_create_account_page(text)


@given("Open Amazon Help Page")
def open_amazon_help_page(context):
    context.app.amazon_help_page.go_to_amazon_help_page()


@when("Use \"Search Help Library\" field and search for: {query}")
def search_for_query(context, query):
    context.app.amazon_help_page.search_library(query)


@then("Verify that {query} text is present")
def verify_customer_text_present(context, query):
    context.app.amazon_help_page.verify_search_text(query)

