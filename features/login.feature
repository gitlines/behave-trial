# Created by phil at 03.07.18

Feature: Login Page
  In order for the product to be usable there needs
  to be a working login mechanism.

  Scenario: Login as admin
    Given I load the website
    When I enter the credentials "admin" for user and "rhebo" for password
    Then I should be redirected to the "/notifications/inbox" page
