Feature: Testing param feature
  @smoke
  Scenario: login to application
    Given launch the application
    When open the orangeHrm
    Then Enter the username "admin" and password "admin123"
    And close browser


  Scenario Outline: Testing param feature with outline and examples
    Given launch the application
    When open the orangeHrm
    Then Enter the username "<username>" and password "<password>"
    And close browser

    Examples:
      | username | password  |
      | admin    | admin123  |
      | admin    | admin1234 |
      | admin2   | admin123  |