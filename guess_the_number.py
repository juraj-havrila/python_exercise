import random
print("Welcome to the Number Guessing Game!")
guesses=0
while guesses==0:
    dificulty=(input("Choose the difficulty (easy,hard): ")).lower()
    if dificulty=="easy":
        guesses=10
    elif dificulty=="hard":
        guesses=5
    else:
        print("wrong option..")
secret_number = random.randint(1,100)
print("I am thinking a number between 1 and 100.")
user_won=False
guess_attempt=guesses
while guess_attempt !=0 and user_won==False:
    users_guess= input(f"You have {guess_attempt} attempts left, what is your guess? ")
    guess_attempt-=1
    if int(users_guess)==secret_number:
        print(f"You won my number is {secret_number}")
        user_won=True
    elif int(users_guess) > secret_number:
        print("Your guess is too high. ")
    elif int(users_guess) < secret_number:
        print("Your guess is too low. ")

if not user_won:
    print(f"You lost, my number was {secret_number}.")
