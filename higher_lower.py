import random
import art, game_data
print(art.logo)
right_guess=True
option_A=[]
option_B=[]
option_A = random.choice(game_data.data)
points=0
while right_guess==True:
    option_B = random.choice(game_data.data)
    print(f"A: {option_A["name"]}, {option_A["description"]} from {option_A["country"]}")
    print(art.vs)
    print(f"B: {option_B["name"]}, {option_B["description"]} from {option_B["country"]}")
    try:
        user_choice=(input("What do you think? A or B? ")).upper()
        if (user_choice!="A" and user_choice!="B"):
            raise RuntimeError("Not A or B")
    except RuntimeError:
            while RuntimeError:
                user_choice = (input("Only options are letter 'A' or 'B'? ")).upper()
                if (user_choice == "A" or user_choice == "B"):
                    break
    if user_choice=='A' and option_A["follower_count"] > option_B["follower_count"]:
        right_guess = True
        points+=1
    elif user_choice=='B' and option_A["follower_count"] < option_B["follower_count"]:
        option_A = option_B
        points += 1
        #option_B = random.choice(game_data.data)
        right_guess = True
    else:
        right_guess = False
        print(f"You lost {option_A['name']} has {option_A['follower_count']} and {option_B['name']} has {option_B['follower_count']} milion followers")
        print(f"You collected {points} points.")
