Feature: Test case AQA_33


  Scenario: User can filter by sale status Newly Launch
    Given Open the main page
    Then Input email andrii.horshkov@gmail.com  is entered
    Then Input password field Andrey380192! is entered
    When Click on Continue button
    Then Verify Andrii Horshkov logged in
    Then Click on Off-plan at the left side menu
    Then Open filter window
    When Select “Newly Launched”
    Then Verify Newly Launched tag for displayed products