from nba_api.stats.endpoints import leaguedashplayerstats

def fetch_nba_fantasy_data(season):
    playerstats = leaguedashplayerstats.LeagueDashPlayerStats(season=season).get_data_frames()[0]
    topplayers = playerstats.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
    
    columns = ["PLAYER_NAME", "TEAM_ABBREVIATION", "GP", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL", "BLK"]
    topplayers[columns].to_csv(f"NBA_Fantasy_{season}.csv", index=False)

seasons = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
for season in seasons:
    fetch_nba_fantasy_data(season)
print("CSV files have been created.")