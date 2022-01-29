# Created by Mike at 1/28/2022
Feature: Working with Registration page elements, fields, and links
#  We are verifying if all links, locators, fields are working properly
#  We are going to click/fill every element on this page
#  We will be using ONLY CSS locators for this scenario
#  As well as we will be using ONLY Relative Path - more stable

  Scenario Outline: User can create a new account
    Given Open Create account page
    Then Verify page URL contains register in it
    When Fill up Your name section with: <name>
    And Fill up Email section with: <email>
    When Type these credentials for password & re-enter password: <password>
    #we could create many scenarios with password checks, but this is just a frame, feel free to improvise
    When Click on Create your Amazon Account
    Then Verify Solve this puzzle to protect your account pops up


    Examples:
      |     name     |          email              |     password     |
      | James Monroe | JamesFake@FakeSuperFake.com | MyFakePassword22 |
      | Eduardo 3rd  | EdikMedik@FakeSuperFake.com | SuperFakePasswrd |
      |Evgeniy Zurab | Kavkazec1@FakeSuperFake.com | DagestanOrel1922 |

