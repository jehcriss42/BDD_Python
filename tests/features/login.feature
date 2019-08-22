Feature: Login
    As a customer
    I want to be able to login to the website
    so I can check my account

Scenario: Customer login to the application
    Given I am in the website
    When I press Sign in
    When I pass my e-mail: "aaa@jjj.com" and my password: "12345"
    Then I can see my account