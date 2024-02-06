# main.py
from datetime import datetime
from get_game_release import search_games_by_date, get_anniversary_years

def main():
    """
    Main function to fetch games from RAWG API that are celebrating significant anniversaries
    on a user-specified date. Users should replace 'YOUR_API_KEY_HERE' with their actual RAWG API key.
    """
    # Placeholder for API key - User should replace with their actual RAWG API key
    api_key = 'YOUR_API_KEY_HERE'  # <-- Replace 'YOUR_API_KEY_HERE' with your actual RAWG API key.

    if api_key == 'YOUR_API_KEY_HERE':
        print("API key is not set. Please replace 'YOUR_API_KEY_HERE' in the script with your actual RAWG API key.")
        return

    try:
        date_input = input("Enter the date (MM-DD): ")
        current_year = datetime.now().year
        datetime.strptime(date_input, "%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Please enter the date in MM-DD format.")
        return

    anniversary_years = get_anniversary_years(current_year)
    games = search_games_by_date(api_key, date_input, anniversary_years, current_year)

    if games:
        print("Games with specified anniversaries on this date:")
        for game in games:
            print(game)
    else:
        print("No games found for the specified anniversaries on this date.")


if __name__ == "__main__":
    main()
