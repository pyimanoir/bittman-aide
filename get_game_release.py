# get_name_release.py
import requests
from datetime import datetime


def get_anniversary_years(current_year, anniversaries=[5, 10, 15, 20, 25, 30, 35]):
    return [current_year - anniversary for anniversary in anniversaries]


def search_games_by_date(api_key, date, years, current_year):
    games_found = []
    for year in years:
        full_date = f"{year}-{date}"  # Construct the full date string
        url = f"https://api.rawg.io/api/games?key={api_key}&dates={full_date},{full_date}&page_size=40"
        response = requests.get(url)
        data = response.json()

        for game in data.get('results', []):
            release_year = game.get('released')[:4]  # Extract the release year from the release date
            anniversary = current_year - int(release_year)  # Calculate the anniversary
            if anniversary in [5, 10, 15, 20, 25, 30, 35]:  # Check if it's a significant anniversary
                games_found.append(f"{game['name']} ({game['released']}) - [{anniversary}th anniversary]")

    return games_found
