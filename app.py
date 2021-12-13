import constants
import random
import copy


replay = []
replayed = 1
my_teams = copy.deepcopy(constants.TEAMS)
my_players = copy.deepcopy(constants.PLAYERS)
store_cleaned_players = []


def menu():
    
    
        try:
            menu_option = int(input("""
                 BasketBall Teams
            -----------MENU-----------
             Please choose a option:
              1) Display Team Stats
              2) Quit
            Enter your choice > """))
            
            if menu_option == 1:
                chosen_team()
                
            if menu_option == 2:
                print("Thanks for stopping by")
                exit()
                
            if menu_option > 2:
                raise ValueError
            if menu_option < 1:
                raise ValueError
                
        except ValueError:
            print("Please enter a valid choice")


def chosen_team():
    
        try:
            team_chose = int(input("""
            1) Panthers
            2) Bandits
            3) Warriors

            Enter an option > """))
            
            if team_chose == 1:
                team_choice_answer = "Panthers"
                display_stats(team_choice_answer)
                
            if team_chose == 2:
                team_choice_answer = "Bandits"
                display_stats(team_choice_answer)
                
            if team_chose == 3:
                team_choice_answer = "Warriors"
                display_stats(team_choice_answer)
                
            if team_chose > 3:
                raise ValueError
            if team_chose < 1:
                raise ValueError
                
        except ValueError:
            print("Please enter a valid choice")


def clean_data():
    if len(replay) == 0:
        cleaned_players = []
        for data in my_players:
            add_player_data = {}
            add_player_data['name'] = data['name']
            if data['experience'] == 'YES':
                add_player_data['experience'] = True
            else:
                add_player_data['experience'] = False
            add_player_data["height"] = int(data['height'].split(' ')[0])
            cleaned_players.append(add_player_data)
    else:
        cleaned_players = store_cleaned_players[0].copy()
    return cleaned_players


def balance_teams():
    cleaned_players = clean_data()
    each_team_total = int(len(cleaned_players) / len(my_teams))
    if len(replay) == 0:
        shuffled_players = random.shuffle(cleaned_players)
        store_cleaned_players.append(cleaned_players.copy())
    player_names = []
    for player in cleaned_players:
        add_player_data = {}
        add_player_data = player["name"]
        player_names.append(add_player_data)
    panthers = []
    panthers.append(player_names[0:each_team_total])
    bandits = []
    bandits.append(player_names[each_team_total:each_team_total * 2])
    warriors = []
    warriors.append(player_names[each_team_total * 2:each_team_total * 3])
    return panthers, bandits, warriors, each_team_total


def display_stats(team_name):
    panthers, bandits, warriors, total_players = balance_teams()
    if team_name == "Panthers":
        player_names = ', '.join(panthers[0][0:total_players])
    if team_name == "Bandits":
        player_names = ', '.join(bandits[0][0:total_players])
    if team_name == "Warriors":
        player_names = ', '.join(warriors[0][0:total_players])
    choice = input("""
    
    Team {} Stats:
    --------------
    Total players: {}
    Players:
      {}

    Enter 1 to continue to start from the begining... """.format(team_name, total_players, player_names))
    if choice == "1":
        replay.append(replayed)
        menu()
    else:
        exit()


if __name__ == "__main__":
    menu()

