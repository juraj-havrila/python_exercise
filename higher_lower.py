import random
import art, game_data
print(art.logo)
right_guess=True
option_A=[]
option_B=[]
while right_guess==True:
    option_A = random.choice(game_data.data)
    option_B = random.choice(game_data.data)

    print(f"A: {option_A["name"]}, {option_A["description"]} from {option_A["country"]}")
    print(art.vs)
    print(f"B: {option_B["name"]}, {option_B["description"]} from {option_B["country"]}")
    try:
        user_choice=(input("What do you think? A or B")).upper()
        if (user_choice!="A" and user_choice!="B"):
            raise RuntimeError("Not A or B")
    except RuntimeError:
            while RuntimeError:
                user_choice = (input("Only options are letter 'A' or 'B'?")).upper()
                if (user_choice == "A" or user_choice == "B"):
                    break
