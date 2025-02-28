from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

#2020 - 2021 season
fb1 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2020 - 2021")
print(fb1.head())
print()

#2021 - 2022 season
fb2 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2021 - 2022")
print(fb2.head())
print()

#2022 - 2023 season
fb3 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2022 - 2023")
print(fb3.head())
print()

#2023 -2024 season
fb4 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2023 - 2024")
print(fb4.head())
print()

#Api for current nba seaason
player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season="2024-25").get_data_frames()[0]
top_50_players = player_stats.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)
print(top_50_players[["PLAYER_NAME","TEAM_ABBREVIATION", "GP", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL","BLK"]])