Feature: Add scores and view scores
    
         As a score recorder, I can Add scores
	 to each team and see the their record
  
         Scenario: Add score to team1
         Given I have team1 and team2
         When I add "1" to "team1"
         Then I will see:
         | team1 |  team2  |
         |   1   |    0    |

         Scenario: Add score to team2
         Given I have team1 and team2
         When I add2 "2" to "team1" 
         Then I will see the following:
         | team1 |  team2  |
         |   1   |    2    |



