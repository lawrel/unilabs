## Process results for any game
def gamestats(country,num_wins,num_losses,num_draw,goals_for,goals_against):
    points = num_wins * 3+num_draw
    goal_adv = goals_for - goals_against
    print(country+":\nWin:",num_wins, "Lose:",num_losses, "Draw:",num_draw,"\nTotal number of points:", points, "Goal advantage:", goal_adv)
gamestats("Germany",2,1,0,7,2)
gamestats("USA",1,1,1,4,4)
gamestats("Argentina",3,0,0,6,3)
gamestats("England",0,1,2,2,4)