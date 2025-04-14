from nba_api.stats.endpoints import leaguedashplayerstats, commonplayerinfo
import pandas as pd
import os
import time
from requests.exceptions import ReadTimeout

# Cache to store player_id -> position (avoids repeated requests)
player_position_cache = {}

def get_player_position(player_id):
    if player_id in player_position_cache:
        return player_position_cache[player_id]

    try:
        info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_data_frames()[0]
        position = info["POSITION"].values[0]
    except ReadTimeout:
        print(f"Timeout on player {player_id}. Retrying after short wait...")
        time.sleep(5)
        return get_player_position(player_id)  # Retry once
    except Exception as e:
        print(f"Error fetching position for player {player_id}: {e}")
        position = "Unknown"

    player_position_cache[player_id] = position
    time.sleep(0.7)  # Gentle delay to avoid rate limits
    return position

def fetch_nba_fantasy_data(season):
    try:
        print(f"Fetching fantasy data for {season}...")
        playerstats = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
        ).get_data_frames()[0]

        topplayers = playerstats.sort_values(by="NBA_FANTASY_PTS_RANK", ascending=True).head(50)

        print("Fetching player positions...")
        topplayers["PLAYER_POSITION"] = topplayers["PLAYER_ID"].apply(get_player_position)

        columns = ["PLAYER_NAME", "TEAM_ABBREVIATION", "PLAYER_POSITION", "NBA_FANTASY_PTS", "GP",
                   "FG3M", "FGM", "FGA", "FTM", "FTA", "PTS", "REB", "AST", "TOV", "STL", "BLK",
                   "FG3_PCT", "FT_PCT", "FG_PCT"]

        topplayers[columns].to_csv(f"NBA_Fantasy_{season}.csv", index=False)
        print(f"Saved: NBA_Fantasy_{season}.csv\n")
        time.sleep(1.5)  # Delay between seasons
    except ReadTimeout:
        print(f"Timeout when fetching data for season {season}. Retrying after short wait...")
        time.sleep(5)
        fetch_nba_fantasy_data(season)  # Retry once

# Main
seasons = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
for season in seasons:
    fetch_nba_fantasy_data(season)

# Combine results
os.chdir("C:/Users/leben/OneDrive/Documents/Fantasy-Basketball-Analysis")
combined_data = []

for season in seasons:
    file = f"NBA_Fantasy_{season}.csv"
    if os.path.exists(file):
        df = pd.read_csv(file)
        df["SEASON"] = season
        combined_data.append(df)
    else:
        print(f"⚠️ Missing file: {file}")

final_df = pd.concat(combined_data, ignore_index=True)
final_df.to_csv("NBA_Fantasy_Combined_2020_to_2025.csv", index=False)
print("Done! Combined fantasy data saved with real player positions.")