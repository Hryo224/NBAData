import nba
import pprint

def get_scoreboard(date):
    scoreboard = nba.nba_data("scoreboard", date)
    return scoreboard

def get_article(game, date):
    game_id = game.get('gameId')
    recap = nba.nba_data("recap_article", date, game_id)
    recap_paras = recap.get('paragraphs')
    article = ""
    for paragraph in recap_paras:
        article += "<p>" + paragraph.get('paragraph') + "</p>"
    return article

if __name__ == '__main__':
    date = "20170304"
    for game in get_scoreboard(date).get('games'):
        pprint.pprint(game)
        article = get_article(game, date)
