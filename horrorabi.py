# SET UP

import random

game_state = dict.fromkeys([
        "year", "starved", "immigrants", "population", "acres", 
        "harvest", "grain_eaten", "grain", "land_value"
        ])
bushel_allocation = { 
        "land": [0, "How much land do you buy? "],
        "food": [0, "How much do you feed your people? "],
        "plant": [0, "How much do you plant? "]
        }
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
name = ""

def validate(num, multiplier = 1, variable = "grain"):
    """ Test if input can be accepted. """
    if not num.isdigit():
        raise ValueError("You need to enter a number! ")
    if int(num) * multiplier > game_state[variable]:
        raise ValueError("You only have {} {}!".format(
            game_state[variable], variable))

def game_init():
    """ Initialize variables to initial states prior to play. """
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

random.seed()
game_init()

# CORE LOOP

while game_state["year"] < 11:
    # OUTPUT
    print(GAME_SUMMARY.format(**game_state))
    
    # INPUT
    for expense in bushel_allocation:
        category = bushel_allocation[expense]
        while True:
            try: 
                answer = input(category[1])
                if expense  == "land":
                    validate(answer, game_state["land_value"])
                else:
                    validate(answer)
            except ValueError as error:
                print(error)
            else:
                answer = int(answer)
                if expense == "land":
                    # Make this a function?
                    if answer == 0:
                        while(True):
                            try:
                                # Checking if answer is within bounds if selling
                                answer = input("How much land do you sell? ")
                                validate(answer, 1, "acres")
                            except ValueError as error:
                                print(error)
                            else:
                                game_state["grain"] += int(answer) * game_state["land_value"]            
                                break
                    else:
                         game_state["grain"] -= answer *  game_state["land_value"]
                else:
                    game_state["grain"] -= answer
                category[0] = answer 
                break

    # PROCESSING

    # Generate land value
    game_state["land_value"] = random.randint(17, 26)

    # Determine how much grain was eaten
    game_state["grain_eaten"] = random.randint(0,
            game_state["grain"] // 200) * 100
    game_state["grain"] -= game_state["grain_eaten"]


    game_state["year"] += 1

# SHUT DOWN
