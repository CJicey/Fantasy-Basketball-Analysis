from nba_api.stats.endpoints import leaguedashplayerstats

#Api for 2020 nba seaason
player_stats0 = leaguedashplayerstats.LeagueDashPlayerStats(season="2020-21").get_data_frames()[0]
fb20 = player_stats0.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(fb20[["PLAYER_NAME","TEAM_ABBREVIATION", "NBA_FANTASY_PTS", "GP", "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK","FG3_PCT","FT_PCT","FG_PCT"]])
print()

#Api for 2021 nba seaason
player_stats1 = leaguedashplayerstats.LeagueDashPlayerStats(season="2021-22").get_data_frames()[0]
fb21 = player_stats1.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(fb21[["PLAYER_NAME","TEAM_ABBREVIATION", "NBA_FANTASY_PTS", "GP", "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK","FG3_PCT","FT_PCT","FG_PCT"]])
print()

#Api for 2022 nba seaason
player_stats2 = leaguedashplayerstats.LeagueDashPlayerStats(season="2022-23").get_data_frames()[0]
fb22 = player_stats2.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(fb22[["PLAYER_NAME","TEAM_ABBREVIATION", "NBA_FANTASY_PTS", "GP", "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK","FG3_PCT","FT_PCT","FG_PCT"]])
print()

#Api for 2023 nba seaason
player_stats3 = leaguedashplayerstats.LeagueDashPlayerStats(season="2023-24").get_data_frames()[0]
fb23 = player_stats3.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(fb23[["PLAYER_NAME","TEAM_ABBREVIATION", "NBA_FANTASY_PTS", "GP", "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK","FG3_PCT","FT_PCT","FG_PCT"]])
print()

#Api for current nba seaason
player_stats4 = leaguedashplayerstats.LeagueDashPlayerStats(season="2024-25").get_data_frames()[0]
fb24 = player_stats4.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(fb24[["PLAYER_NAME","TEAM_ABBREVIATION", "NBA_FANTASY_PTS", "GP", "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK","FG3_PCT","FT_PCT","FG_PCT"]])
print()

