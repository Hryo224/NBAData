import boxscore as b
import nba
import pprint
from datetime import date, timedelta

def parse_quarter_to_table(team):
    content = "<th>" + team['team'] + "</th>"
    total = 0
    for quarter in team['quarters']:
        total += int(quarter)
        content += "<td>" + quarter + "</td>"
    content += "<td>" + str(total) + "</td>"
    return content

def generate_summary_table(home, away):
    nth = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "OT1", 6: "OT2", 7: "OT3"}
    table = "<table><tr><th/>"
    for i in range(0, len(home['quarters'])):
        table += "<th>" + nth[i+1] + "</th>"
    table += "<th>Total</th>"
    table += "<tr>" + parse_quarter_to_table(home) + "</tr>"
    table += "<tr>" + parse_quarter_to_table(away) + "</tr>"
    table += "</table>"
    return table

def generate_report(boxscore, home, away, article):
    b.parse_boxscore(boxscore)
    content = "<h1>" + home['team'] + " vs " + away['team'] + "</h1>"
    content += generate_summary_table(home, away)
    content += article
    return content

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

def get_game_data(game, team):
    game_data = {}
    quarter_data = []
    team_data = game.get(team)
    per_quarter = team_data.get('linescore')
    for quarter in per_quarter:
        quarter_data.append(quarter.get('score'))
    game_data['quarters'] = quarter_data
    game_data['team'] = team_data.get('triCode')
    game_data['duration'] = team_data.get('gameDuration')
    game_data['attendance'] = team_data.get('attendance')
    return game_data

def init(date):
    for game in get_scoreboard(date).get('games'):
        boxscore = nba.nba_data("boxscore", date, game.get('gameId'))
        home = get_game_data(game, 'hTeam')
        away = get_game_data(game, 'vTeam')
        article = get_article(game, date)
        report = generate_report(boxscore, home, away, article)

def get_yesterday_date():
    return (date.today() - timedelta(1)).strftime('%Y%m%d')

if __name__ == "__main__":
    calendar = nba.nba_data("calendar")
    date = get_yesterday_date()
    if date in calendar:
        init(date)    
