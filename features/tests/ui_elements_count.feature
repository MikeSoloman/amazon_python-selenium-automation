# Created by Mike Soloman at 1/29/2022
Feature: Amazon UI elements count
  # We will be counting UI elements in BestSeller's Page and Customer Service’s page
  #

  Scenario: Amazon BestSeller's Page UI elements count
    Given Open Amazon Main Page
    When Click on BestSeller's Page
    # We could directly go to BestSeller's Page, but the purpose of my Selenium Frame creation
    # is to show different ways of doing things.
    Then Verify it's bestsellers page
    Then Verify BestSeller's Page has 5 UI elements with links

  Scenario: Customer Service’s page UI elements are present
    # created a new custo_page page object and as always attached to our application page - app
    Given Open Customer Service Page
    Then Verify Hello. What can we help you with? text
    #used combination of CSS and XPath with contains, to give examples of both
    Then Verify there are 9 elements present on Some Things you can do here div
    Then Verify there are 12 elements present on Browse Help Topics