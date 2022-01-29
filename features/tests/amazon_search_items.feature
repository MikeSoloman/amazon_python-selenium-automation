# Created by Mike SoloMan at 1/26/2022
#this feature BDD is using CSS locators

Feature: Amazon Main Page's Search Bar
#  From Amazon Main Page we are
#  Searching for a few items
#  Adding those items into the cart
#  Verifying that items are in the cart


  Scenario Outline: User can search for an item
    Given Open Amazon Main Page
    When Input <item name> into Amazon Search Field
    And Click on Amazon Search Icon
    Then Verify <search_query> is in Actual Text
    Then Verify URL contains <query> in it


    Examples:
      |   item name     |   search_query |  query   |
      |     Dress       |     "Dress"    |  Dress   |
      |    Men Shoes    |   "Men Shoes"  |  Shoes   |
      |  Cotton Candy   | "Cotton Candy" |  Cotton  |