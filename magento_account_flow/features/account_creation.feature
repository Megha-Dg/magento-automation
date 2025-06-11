Feature: Account Creation and Login on Magento

  Scenario: User creates a new account successfully
    Given the user is on the Magento homepage
    When the user navigates to Create Account page
    And the user fills in valid registration details
    Then the account should be created successfully
    And the user logs out

  Scenario: Existing user logs in with valid credentials
    Given the user is on the Magento homepage
    When the user navigates to Sign In page
    And the user enters valid login credentials
    Then the user should be logged in and see the dashboard
