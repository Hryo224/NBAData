import nba
from collections import OrderedDict
from player import *
import pprint

mapping = OrderedDict([
            ("Player","player"),
            ("Min","min"),
            ("FG",["fga", "fgm"]),
            ("3PT",["tpa", "tpm"]),
            ("FT",["fta", "ftm"]),
            ("OReb","offReb"),
            ("DReb","defReb"),
            ("Reb","totReb"),
            ("Ast","assists"),
            ("Stl","steals"),
            ("Blk","blocks"),
            ("TO","turnovers"),
            ("PF","pFouls"),
            ("+/-","plusMinus"),
            ("Pts","points") ])


def parse_boxscore(team, boxscore):
    stats = boxscore.get('stats')
    table = "<h2>" + team['team'] + "</h2>"
    count = 0
    for player in stats.get('activePlayers'):
        if team.get('teamId') == player.get('teamId'):
           p = Player(**player)
           count += 1
           if count == 6:
               table += "<tr><th colspan=15><center>Bench</center></th></tr>"
           table += "<tr>"
           for key, value in mapping.items():
               if key == "Player":
                   table += "<th>" + getattr(p,value) + "</th>"
               else:
                   if isinstance(value, list):
                       table += "<td>" + str(getattr(p,value[1])) + "-" + str(getattr(p,value[0])) + "</td>"
                   else:
                       table += "<td>" + str(getattr(p,value)) + "</td>"
           table += "</tr>"
    return table

def generate_boxscore(team_id, boxscore):
    table = "<div class='datagrid'><table>"
    table += "<tr><th colspan=15><center>Starters</center></th></tr>"
    for head in mapping.keys():
        table += "<th>" + head + "</th>"
    table += "</tr>"
    table += parse_boxscore(team_id, boxscore)
    table += "</div></table>"
    return table
