DATA_URL = "/data/10s/prod/v1"

methods = {

    "CALENDAR":{
        "function":"calendar",
        "endpoint":DATA_URL + "/calendar.json" 
    },
    "SCOREBOARD":{
        "function":"scoreboard",
        "endpoint":DATA_URL + "/%s/scoreboard.json",
        "params":"date"
    },

    "TEAMS":{
        "function":"teams",
        "endpoint":DATA_URL + "/%s/teams.json",
        "params":"year"
    },
    "PLAYERS_BY_YEAR":{
        "function":"players",
        "endpoint":DATA_URL + "/%s/players.json",
        "params":"year"
    },
    "COACHES_BY_YEAR": {
        "function":"coaches",
        "endpoint":DATA_URL+"/%s/coaches.json",
        "params":"year"
    },
    "CONFERENCE_STANDINGS":{
        "function":"conference_standings",
        "endpoint":DATA_URL+"/current/standings_conference.json"
    },
    "LEAGUE_DIVISION_STANDINGS":{
        "function":"division_standings",
        "endpoint":DATA_URL+"/current/standings_division.json"
    },
    "LEAGUE_UNGROUPED_STANDINGS":{
        "function":"standings",
        "endpoint":DATA_URL+"/current/standings_all.json"
    },
    "LEAGUE_MINI_STANDINGS":{
        "function":'mini_standings',
        "endpoint":DATA_URL+"/current/standings_all_no_sort_keys.json"
    },
    "LEAGUE_TEAM_STATS_LEADERS":{
        "function":"team_stats_leaders",
        "endpoint":DATA_URL+"%s/team_stats_rankings.json"
    },
    "LEAGUE_LAST_FIVE_GAME_TEAM_STATS":{
        "function":"last_five_game_team_stats",
        "endpoint":DATA_URL+"/%s/team_stats_last_five_games.json"
    },
    "PREVIEW_ARTICLE":{
        "function":"preview_article",
        "endpoint": DATA_URL+"/%s/%s_preview_article.json"
    },
    "TEAM_LEADERS":{
        "function":"team_leaders",
        "endpoint":DATA_URL+"/%s/teams/%s/leaders.json"
    },
    "RECAP_ARTICLE":{
        "function":"recap_article",
        "endpoint":DATA_URL+"/%s/%s_recap_article.json"
    },
    "BOXSCORE":{
        "function":"boxscore",
        "endpoint":DATA_URL+"/%s/%s_boxscore.json"
    },
    "PLAY_BY_PLAY":{
        "function":"play_by_play",
        "endpoint":DATA_URL+"/%s/%s_pbp_%s.json"
    },
    "LEADTRACKER":{
        "function":"leadtracker",
        "endpoint":DATA_URL+"/%s/%s_lead_tracker_%s.json"
    }
}
