import nba
players = nba.nba_data("players", 2016).get("league").get("standard")

class Player:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if value != "":
                setattr(self, key, value)
            else:
                value = 0
                setattr(self, key, value)
        self.player = self.get_player_name(self.personId)
        
    def get_player_name(self, player_id):
        for each in players:
            if each['personId'] == player_id:
                return each['firstName'] + " " + each['lastName']
        return "N/A"

