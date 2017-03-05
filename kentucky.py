from nba import nba_data
from pprint import pprint
CURRENT_YEAR = 2016

def get_players():
    return nba_data("players", CURRENT_YEAR)

def get_player_id_from_college(college):
    players = []
    players_obj = get_players().get('league').get('standard')
    for player in players_obj:
        if player.get('collegeName') == college:
            players.append(player)
    return players

def get_player_stats(player_id):
    return nba_data("player_game_log", CURRENT_YEAR, player_id)

if __name__ == "__main__":
    kentucky = get_player_id_from_college('Kentucky')
    for each in kentucky:
        stats = get_player_stats(each.get('personId'))
        for stat in stats.get('league').get('standard'):
            string = each['firstName'] + " " + each['lastName'] + " had the following stats on " + stat['gameDateUTC']
            points = stat['stats']['points']
            assists = stat['stats']['assists']
            string += " " + points + " points, " + assists + " assists"
            print(string)

