# Created by Mike SoloMan at 1/27/2022


Feature: Amazon Sign-In Page Links/Locators Verification
#  We are verifying if all links, locators, fields are working properly
#  We are going to click/fill every element on this page
#  We will be using ONLY XPATH locators for this scenario
#  As well as we will be using ONLY Relative Path - more stable


  Scenario: Verifying that Sign-In Page fields are working properly
    Given Open Amazon Sign-In Page
    Then Verify signin is present in the URL
    When Click on Amazon Logo
    Then Verify Amazon Logo takes to the home page
    Then Verify Field: Email or mobile phone number is present
    When Fill up Email or mobile phone number field: MySuperFakeEmail@SpamAndFake.com
    When Click Continue btn
    Then Verify user sees: We cannot find an account with that email address

    # keeping scenario under 10 steps suggested, therefore, for links and a href,
    # we will have a second separate scenario

  Scenario: Verifying that that Sign-In Page links and locators are working properly
    Given Open Amazon Sign-In Page
    Then Verify there are 2 links in the Legal Text Row
    Then Verify Conditions of Use Link redirects to the right page
    Then Verify Amazon.com Privacy Notice redirects to the right page
    Then Verify Need help expander has 2 links visible once expanded
    Then Verify sign-in footer has 3 links present
    When Click on Create your Amazon Account BTN
    Then Verify user sees Create account


    #again, for this feature, I will only be using XPATH, just to show how to handle this with XPATH,
    #next feature BDD, we will be doing CSS, the goal is to show different ways of using XPATH and CSS
    #even though ID and NAME is the easiest and the most common ones

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help Page
    When Use "Search Help Library" field and search for: Canceled Orders
    #no enter button is available, therefore we will be using Keys.ENTER,
    #another common way is to use Keys.RETURN
    Then Verify that Cancel Items or Orders text is present

