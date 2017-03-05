import nba
import pprint
nba.print_method_list()
scoreboard = nba.nba_data("scoreboard", 20161205)
for game in scoreboard.get('games'):
    game_id = game.get('gameId')
    pprint.pprint(nba.nba_data("recap_article", 20161205, game_id))
