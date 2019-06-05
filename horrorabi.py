# SET UP

import random

# Year use as for loop variable

GAME_SUMMARY =  ( 
       "In year {year}:\n"
       "{starved} people starved, and {immigrants} came to the city.\n"
       "The population is now {population}.\n"
       "The city owns {acres} acres.\n"
       "We harvested {harvest} bushels per acre.\n"
       "Rats ate {grain_eaten} bushels.\n"
       "You now have {grain} bushels in storage.\n"
       "Land is trading at {land_value} bushels per acre.\n" 
        ) 

game_state = dict.fromkeys([
        "year", "starved", "immigrants", "population", "acres", 
        "harvest", "grain_eaten", "grain", "land_value"
        ])

name = ""

# TODO: FIGURE OUT A BETTER WAY TO DEAL WITH THIS
def game_init():
    """Initialize variables to default states prior to play."""
    game_state["year"] = 1
    game_state["starved"] = 0
    game_state["immigrants"] = 5
    game_state["population"] = 100
    game_state["acres"] = 1000
    game_state["harvest"] = 3
    game_state["grain_eaten"] = 200
    game_state["grain"] = 2800
    game_state["land_value"] = 26
    name = input("What is your name, ruler? ")

game_init()
random.seed()
# CORE LOOP

while game_state["year"] < 11:
    # Output
    print(GAME_SUMMARY.format(**game_state))
    
    # Input

    # Processing
    game_state["land_value"] = random.randint(17, 26)

    # IS TOO MUCH GRAIN EATEN? BALANCE ONCE GAME IS WORKING
    game_state["grain_eaten"] = random.randint(0,
            game_state["grain"] // 200) * 100
    game_state["grain"] -= game_state["grain_eaten"]


    game_state["year"] += 1

# SHUT DOWN

