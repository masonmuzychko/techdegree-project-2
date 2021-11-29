from constants import PLAYERS
from constants import TEAMS
import random


def menu():
    menu_choice = input("""
    BASKETBALL TEAM STATS TOOL
        ---MENU---
    Here are your choices:
    1) Display team Stats
    2) Quit
    Enter an option:    """)

    if menu_choice == "1":
        choose_team()
    if menu_choice == "2":
        exit()
    else:
        print("Please choose 1 or 2")
        menu()


def choose_team():
    choose_team = input("""
    1) Panthers
    2) Bandits
    3) Warriors

    Enter an option:   """)

    if choose_team == "1":
        choose_team_answer = "Panthers"
        display_stats(choose_team_answer)
    elif choose_team == "2":
        choose_team_answer = "Bandits"
        display_stats(choose_team_answer)
    elif choose_team == "3":
        choose_team_answer = "Warriors"
        display_stats(choose_team_answer)
    else:
        print("Please enter a valid option")
        choose_team()

def clean_data():
    players_experienced = []
    players_inexperienced = []
    players_heights = []
    for player in PLAYERS:
        add_player_data = {}
        add_player_data["name"] = player["name"]
        if "and" in player["guardians"]:
            add_player_data["guardians"] = player["guardians"].split(' and ')
        else:
            add_player_data["guardians"] = [player["guardians"]]
        if player["experience"] == 'YES':
            add_player_data["experience"] = True
        else:
            add_player_data["experience"] = False
        add_player_data["height"] = int(player['height'].split(' ')[0])
        players_heights.append(player["height"])
        if add_player_data['experience'] is True:
            players_experienced.append(add_player_data)
        else:
            players_inexperienced.append(add_player_data)
    return players_experienced, players_inexperienced






def balance_teams():
    each_team_total = int(len(PLAYERS) / len(TEAMS))
    team_players_chosen = random.sample(PLAYERS, each_team_total)
    player_names = []
    for player in team_players_chosen:
        add_player_name = {}
        add_player_name = player["name"]
        player_names.append(add_player_name)

    return each_team_total, player_names


def display_stats(team):
    total_players, player_names = balance_teams()

    enter = input("""
    Team: {} Stats
    --------------
    Total players: {}
    Players:
      {}

    Press 1 to continue...""".format(team, total_players, ', '.join(player_names)))
    if enter == "1":
        exit()
    else:
        exit()








if __name__ == "__main__":
    menu()
