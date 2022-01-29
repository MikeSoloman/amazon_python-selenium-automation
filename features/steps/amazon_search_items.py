from behave import when, given, then


@given("Open Amazon Main Page")
def open_amazon(context):
    context.app.main_page.open_main_page()


@when("Input {item} into Amazon Search Field")
def input_item_into_search_bar(context, item):
    context.app.main_page.input_amazon_text(item)


@when("Click on Amazon Search Icon")
def search_icon_click(context):
    context.app.main_page.click_search_amazon()


@then("Verify {search_word} is in Actual Text")
def search_text_verification(context, search_word):
    context.app.search_result_page.verify_search_text(search_word)


@then("Verify URL contains {query} in it")
def search_result_url_verification(context, query):
    context.app.search_result_page.verify_search_page_url(query)
