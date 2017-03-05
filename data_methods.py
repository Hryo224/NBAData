DATA_URL = "/data/10s/prod/v1"

methods = {

    "CALENDAR":{
        "function":"calendar",
        "endpoint":DATA_URL + "/calendar.json",
        "params":["none"]
    },
    "SCOREBOARD":{
        "function":"scoreboard",
        "endpoint":DATA_URL + "/%s/scoreboard.json",
        "params":["date (format YYYYMMDD)"]
    },

    "TEAMS":{
        "function":"teams",
        "endpoint":DATA_URL + "/%s/teams.json",
        "params":["year"]
    },
    "PLAYERS_BY_YEAR":{
        "function":"players",
        "endpoint":DATA_URL + "/%s/players.json",
        "params":["year"]
    },
    "COACHES_BY_YEAR": {
        "function":"coaches",
        "endpoint":DATA_URL+"/%s/coaches.json",
        "params":["year"]
    },
    "CURRENT_CONFERENCE_STANDINGS":{
        "function":"conference_standings",
        "endpoint":DATA_URL+"/current/standings_conference.json",
        "params":["none"]
    },
    "CURRENT_DIVISION_STANDINGS":{
        "function":"division_standings",
        "endpoint":DATA_URL+"/current/standings_division.json",
        "params":["none"]
    },
    "STANDINGS":{
        "function":"standings",
        "endpoint":DATA_URL+"/current/standings_all.json",
        "params":["none"]
    },
    "MINI_STANDINGS":{
        "function":'mini_standings',
        "endpoint":DATA_URL+"/current/standings_all_no_sort_keys.json",
        "params":["none"]
    },
    "TEAM_STATS_RANKINGS":{
        "function":"team_stats_leaders",
        "endpoint":DATA_URL+"%s/team_stats_rankings.json",
        "params":["year"]
    },
    "TEAM_STATS_LAST_FIVE_GAMES":{
        "function":"last_five_game_team_stats",
        "endpoint":DATA_URL+"/%s/team_stats_last_five_games.json",
        "params":["year"]
    },
    "PREVIEW_ARTICLE":{
        "function":"preview_article",
        "endpoint": DATA_URL+"/%s/%s_preview_article.json",
        "params":["date (format YYYYMMDD)","gameId"]
    },
    "TEAM_LEADERS":{
        "function":"team_leaders",
        "endpoint":DATA_URL+"/%s/teams/%s/leaders.json",
        "params":["year","teamName"]
    },
    "RECAP_ARTICLE":{
        "function":"recap_article",
        "endpoint":DATA_URL+"/%s/%s_recap_article.json",
        "params":["date (format YYYYMMDD)", "gameId"]
    },
    "BOXSCORE":{
        "function":"boxscore",
        "endpoint":DATA_URL+"/%s/%s_boxscore.json",
        "params":["date (format YYYYMMDD)", "gameId"]
    },
    "PLAY_BY_PLAY":{
        "function":"play_by_play",
        "endpoint":DATA_URL+"/%s/%s_pbp_%s.json",
        "params":["date (format YYYYMMDD)", "gameId", "period"]
    },
    "LEADTRACKER":{
        "function":"leadtracker",
        "endpoint":DATA_URL+"/%s/%s_lead_tracker_%s.json",
        "params":["date (format YYYYMMDD)", "gameId", "period"]
    },
    "MINI_BOXSCORE":{
        "function":"mini_boxscore",
        "endpoint":DATA_URL+"/%s/%s_mini_boxscore.json",
        "params":["date (format YYYYMMDD)", "gameId"]
    },
    "PLAYER_GAME_LOG":{
        "function":"player_game_log",
        "endpoint":DATA_URL+"/%s/players/%s_gamelog.json",
        "params":["year", "playerId"]
    },
    "PLAYER_UBER_STATS":{
        "function":"player_uber_stats",
        "endpoint":DATA_URL+"/%s/players/%s_uber_stats.json",
        "params":["year", "playerId"]
    },
    "TEAM_SCHEDULE":{
        "function":"team_schedule",
        "endpoint":DATA_URL+"/%s/teams/%s/schedule.json",
        "params":["year", "teamName"]
    },
    "TEAM_ROSTER":{
        "function":"team_roster",
        "endpoint":DATA_URL+"/%s/teams/%s/roster.json",
        "params":["year", "teamName"]
    }
}
