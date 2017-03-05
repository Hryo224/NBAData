import nba
from player import *
import pprint


def parse_boxscore(boxscore):
    stats = boxscore.get('stats')
    for player in stats.get('activePlayers'):
       p = Player(**player) 

def generate_boxscore(boxscore):
    headers = ["Player", "Min", "FG", "3PT", "FT", "OReb", "DReb", "Reb", "Ast", "Stl", "Blk", "TO", "PF", "+/-", "Pts"]
    table = "<table><tr>"
    for head in headers:
        table += "<th>" + head + "</th>"
     table += "</tr>
