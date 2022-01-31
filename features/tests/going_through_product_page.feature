# Created by Mike Soloman at 1/30/2022
Feature: Going through product page and verifying colors and descriptions match
  # Enter feature description here

  Scenario: Go through A Product Page and Verify Colors Match
    Given Open Product Page
    #  we can also verify if url or text matches a specific product
    Then Verify Expected colors match Actual Colors

  Scenario: Verify that every product on the Wholefoods page has a text ‘Regular' and a product name
    Given Open Amazon Wholefoods page
    #  we can also verify if url or text matches wholefoods
    Then Verify that every product on the Wholefoods page has a text Regular and a product name