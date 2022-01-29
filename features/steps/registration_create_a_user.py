from behave import when, given, then


@given("Open Create account page")
def open_create_page(context):
    context.app.create_account_page.open_create_account_page()


@then("Verify page URL contains {text} in it")
def url_verification(context, text):
    context.app.create_account_page.verify_create_url(text)


@when("Fill up Your name section with: {name}")
def name_fill_up(context, name):
    context.app.create_account_page.fill_up_name(name)


@when("Fill up Email section with: {email}")
def name_fill_up(context, email):
    context.app.create_account_page.fill_up_email(email)


@when("Type these credentials for password & re-enter password: {password}")
def name_fill_up(context, password):
    context.app.create_account_page.fill_up_password_fields(password)


@when("Click on Create your Amazon Account")
def click_create(context):
    context.app.create_account_page.click_on_create_account_btn()


@then("Verify {text} pops up")
def verify_puzzle_text(context, text):
    context.app.create_account_page.solve_puzzle(text)
