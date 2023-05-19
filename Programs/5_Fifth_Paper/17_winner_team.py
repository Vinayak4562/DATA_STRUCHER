'''17. Create a function that takes the number of wins, draws and losses and calculates the number of points obtained so far for 'n' number of football teams . Print the winner team in the end .
wins get +3 points, draws get +1 point, losses get -1 points .
I/p: Team1(3, 4, 2) ## calculation : 3*3 +4*1 + 2(-1) = 11Team2(5, 0, 2) ## calculation : 5*3 + 0*1 + 2(-1) = 13 Team3(0, 0, 1) ## calculation : 0*3 + 0*1 + 1(-1) = -1
O/p: Winner: Team2
'''

def calc_points(*teams):
    points = []
    for team in teams:
        team_points = team[0] * 3 + team[1] * 1 + team[2] * -1
        points.append(team_points)
    max_points = max(points)
    winner_index = points.index(max_points)
    print("The Winner Team is: Team", winner_index + 1)

calc_points((3, 4, 2), (5, 0, 2), (0, 0, 1))
# calc_points((3, 4, 2), (0, 0, 1), (5, 0, 2))
# calc_points((5, 0, 2), (0, 0, 1), (3, 4, 2))
