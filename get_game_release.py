# get_name_release.py
import requests
from typing import List, Dict
from datetime import datetime


def get_anniversary_years(current_year: int, anniversaries=None) -> List[int]:
    """
    Calculate the years to search for based on the specified anniversaries.

    Parameters:
    - current_year (int): The current year.
    - anniversaries (List[int]): A list of anniversary milestones.

    Returns:
    - List[int]: A list of years corresponding to the anniversaries.
    """
    if anniversaries is None:
        anniversaries = [5, 10, 15, 20, 25, 30, 35]
    return [current_year - anniversary for anniversary in anniversaries]


def search_games_by_date(api_key: str, date: str, years: List[int], current_year: int) -> List[str]:
    """
    Search for games released on 'date' during the 'years' and calculate their anniversaries.

    Parameters:
    - api_key (str): The RAWG API key.
    - date (str): The date (MM-DD) to search for game releases.
    - years (List[int]): The years to include in the search, derived from significant anniversaries.
    - current_year (int): The current year for anniversary calculation.

    Returns:
    - List[str]: A list of strings describing the games and their anniversaries.
    """
    games_found = []
    for year in years:
        full_date = f"{year}-{date}"  # Construct the full date string
        url = f"https://api.rawg.io/api/games?key={api_key}&dates={full_date},{full_date}&page_size=40"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the response was an error
            data = response.json()
            for game in data.get('results', []):
                release_year = game.get('released')[:4]  # Extract the release year from the release date
                anniversary = current_year - int(release_year)  # Calculate the anniversary
                if current_year - int(release_year) in [5, 10, 15, 20, 25, 30, 35]:  # Directly check against the list
                    games_found.append(f"{game['name']} ({game['released']}) - [{anniversary}th anniversary]")
        except requests.RequestException as e:
            print(f"Request to RAWG API failed: {e}")
            break  # Exit the loop on failure

    return games_found
