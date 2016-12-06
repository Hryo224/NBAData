from nba import nba_data
import pprint
scoreboard = nba_data("scoreboard", 20161205)
for game in scoreboard.get('games'):
    game_id = game.get('gameId')
    pprint.pprint(nba_data("recap_article", 20161205, game_id))
