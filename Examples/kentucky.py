from NBAData import nba_data
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

def get_kentucky_stat_lines():
    kentucky = get_player_id_from_college('Kentucky')
    for player in kentucky:
        stats = get_player_stats(player.get('personId'))
        for stat in stats.get('league').get('standard'):
            stat_line = player['firstName'] + " " + player['lastName'] + " had the following stats on " + stat['gameDateUTC']
            points = stat['stats']['points']
            assists = stat['stats']['assists']
            rebounds = stat['stats']['totReb']
            stat_line += " " + points + " points, " + assists + " assists" + "and " + rebounds + " rebounds"
            print(stat_line)

if __name__ == '__main__':
    get_kentucky_stat_lines()
