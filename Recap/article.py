import boxscore as b
import pdfkit as p
import nba
import pprint
import os
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
    table = "<center><table><tr><th/>"
    for i in range(0, len(home['quarters'])):
        table += "<th>" + nth[i+1] + "</th>"
    table += "<th>Total</th>"
    table += "<tr>" + parse_quarter_to_table(home) + "</tr>"
    table += "<tr>" + parse_quarter_to_table(away) + "</tr>"
    table += "</table></center>"
    return table

def generate_report(boxscore, home, away, article):
    content = "<html><head><link rel='stylesheet' type='text/css' href='/home/nogoodnamesqq/NBA/Recap/html/style.css'>"
    content += "<center><h1>" + home['team'] + " vs " + away['team'] + "</h1></center>"
    content += generate_summary_table(home, away)
    content += b.generate_boxscore(home, boxscore)
    content += b.generate_boxscore(away, boxscore)
    content += article
    content += "</html>"
    return content

def get_scoreboard(date):
    scoreboard = nba.nba_data("scoreboard", date)
    return scoreboard

def get_article(game, date):
    game_id = game.get('gameId')
    recap = nba.nba_data("recap_article", date, game_id)
    recap_paras = recap.get('paragraphs')
    article = "<center><h2> AP Summary </h2></center>"
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
    game_data['teamId'] = team_data.get('teamId')
    game_data['duration'] = team_data.get('gameDuration')
    game_data['attendance'] = team_data.get('attendance')
    return game_data

def init(date):
    dir = "/home/nogoodnamesqq/NBA/Recap/html/"+date+"/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    for game in get_scoreboard(date).get('games'):
        boxscore = nba.nba_data("boxscore", date, game.get('gameId'))
        home = get_game_data(game, 'hTeam')
        away = get_game_data(game, 'vTeam')
        article = get_article(game, date)
        report = generate_report(boxscore, home, away, article)
        file_name = home['team'] + "vs" + away['team'] + date + ".pdf"
        p.from_string(report, file_name)
        os.rename(file_name, dir+file_name)

def get_yesterday_date():
    return (date.today() - timedelta(1)).strftime('%Y%m%d')

if __name__ == "__main__":
    calendar = nba.nba_data("calendar")
    date = get_yesterday_date()
    if date in calendar:
        init(date)    
