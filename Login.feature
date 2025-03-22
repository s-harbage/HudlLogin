Feature: Hudl Login Functionality

  Scenario: Successful login with valid credentials
    Given the user is on the Hudl login page
    When the user enters a valid email
    And clicks the login button
    And the user enters a valid password
    And clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Login with an invalid email and valid password
    Given the user is on the Hudl login page
    When the user enters an invalid email
    And clicks the login button
    And the user enters an invalid password
    And clicks the login button
    Then an error message should be displayed

  Scenario: Login with an invalid password
    Given the user is on the Hudl login page
    When the user enters a valid email
    And clicks the login button
    And the user enters an invalid password
    And clicks the login button
    Then an error message should be displayed

  Scenario: Login with both an invalid email and password
    Given the user is on the Hudl login page
    When the user enters an invalid email
    And clicks the login button
    And the user enters an invalid password
    And clicks the login button
    Then an error message should be displayed

  Scenario: Login with an empty email field
    Given the user is on the Hudl login page
    When the user enters an empty email
    And clicks the login button
    Then an error message should be displayed

  Scenario: Login with an empty password field
    Given the user is on the Hudl login page
    When the user enters a valid email
    And clicks the login button
    And the user enters an empty password
    And clicks the login button
    Then an error message should be displayed