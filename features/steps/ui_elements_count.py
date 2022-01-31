from behave import when, given, then


@when("Click on BestSeller's Page")
def click_best_sellers_page(context):
    context.app.main_page.click_on_best_sellers_page_link()


@then("Verify it's {text} page")
def best_sellers_url_verification(context, text):
    context.app.best_sellers_page.best_sellers_url_verif(text)


@then("Verify BestSeller's Page has {num} UI elements with links")
def best_sellers_page_link_count(context, num):
    context.app.best_sellers_page.link_count(num)


@given("Open Customer Service Page")
def open_customer_service_page(context):
    context.app.customer_service_page.open_customer_service_page()


@then("Verify {text} text")
def customer_service_page_greeting_verification(context, text):
    context.app.customer_service_page.verify_greeting(text)


@then("Verify there are {num} elements present on Some Things you can do here div")
def customer_service_middle_div_elements_verif(context, num):
    context.app.customer_service_page.verify_middle_div_elements(num)


@then("Verify there are {num} elements present on Browse Help Topics")
def customer_service_bottom_div_elements_verif(context, num):
    context.app.customer_service_page.verify_bottom_div_elements(num)