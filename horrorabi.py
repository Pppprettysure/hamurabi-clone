# SET UP

import random

game_state = dict.fromkeys([
        "year", "starved", "immigrants", "population", "acres", 
        "harvest", "grain_eaten", "grain", "land_value"
        ])
bushel_allocation = { 
        "land": [0, "How much land do you buy? "],
        "sell": [0, "How much land do you sell? "],
        "food": [0, "How much do you feed your people? "],
        "plant": [0, "How much do you plant? "]
        }
GAME_SUMMARY =  (
       "\n"
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
    """ Test if input can be accepted and return as int. """
    if not num.isdigit():
        raise ValueError("You need to enter a number! ")
    if int(num) * multiplier > game_state[variable]:
        raise ValueError("You only have {} {}!".format(
            game_state[variable], variable))
    else:
        return int(num)

def check_loss():
    if game_state["population"] < 1:
        print("You've lost all citizens! ")
        return True
    elif game_state["population"] * .45 < game_state["starved"]:
        print("\nYou've been overthrown by the starving peasantry! ")
        return True
    else:
        return False

def loss():
    # TODO: These loops could be made into a function maybe? or maybe
    # just reutilize the main function
    while True:
        answer = input("Do you want to play again? Y/N: ")
        if answer.casefold() == "y":
            game_init()
            break
        elif answer.casefold() == "n":
            game_state["year"] = 100
            break
        else:
            print("Please enter a valid answer.")
                
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
    lost = False

    # OUTPUT
    print(GAME_SUMMARY.format(**game_state))
    
    # INPUT
    for expense in bushel_allocation:
        category = bushel_allocation[expense]
        while True:
            try: 
                answer = input(category[1])
                if expense  == "land":
                    answer = validate(answer, game_state["land_value"])
                    game_state["grain"] -= answer * game_state["land_value"]
                    game_state["acres"] += answer
                elif expense == "sell":
                    answer = validate(answer, 1, "acres") 
                    game_state["grain"] += answer * game_state["land_value"]
                    game_state["acres"] -= answer
                elif expense == "plant":
                    validate(answer) # Check seed
                    answer = validate(answer, 1, "acres") # Check acres
                    game_state["grain"] -= answer
                else:
                    answer = validate(answer)
                    game_state["grain"] -= answer
            except ValueError as error:
                print(error)
            else:
                category[0] = answer 
                break

    # PROCESSING
    
    # Dependent on player action 

    # Starvation (each person needs 20 grain)
    game_state["starved"] = (
        (game_state["population"] * 20) - bushel_allocation["food"][0] 
        ) // 20 

    if check_loss():
        lost = True
    else:
        game_state["population"] -= game_state["starved"]
   
    # Generate land value
    game_state["land_value"] = random.randint(17, 26)

    # Generate productivity of land
    game_state["harvest"] = random.randint(1, 6)

    # Add harvest
    game_state["grain"] += game_state["harvest"] * bushel_allocation["plant"][0]

    # Determine how much grain was eaten by rats
    game_state["grain_eaten"] = random.randint(0,
            game_state["grain"] // 200) * 100
    game_state["grain"] -= game_state["grain_eaten"] 
     
    # Immigrant random + add
    immigrant_modifiers = (
            (game_state["acres"]) 
            + game_state["grain"]
            )

    game_state["immigrants"] = (((
            random.randint(0 , 5) * 20 * game_state["acres"] + 
            game_state["grain"]) // game_state["population"]) // 101 
            )

    game_state["population"] += game_state["immigrants"]

    # Advance year
    game_state["year"] += 1

    # Check if player wants to restart of if program should terminate on loss
    if lost == True:
        loss()

# SHUT DOWN
print("\nThanks for playing! ")
