import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play=input("Do you want to play a game? (y/n)")

def show_cards(gamestate):
    score_dealer=0
    score_player=0
    if gamestate == "ingame":
        first_card = cards_dealer[0]
        print(f"Dealer cards: {first_card}, X")
    else:
        pom = ''
        for card in cards_dealer:
            pom +=str(card) +", "
            score_dealer+=int(card)
        print(f"Dealer cards: {pom}")
    pom = ''
    for card in cards_player:
        pom+=str(card) + ", "
        score_player+=int(card)
    print(f"Player cards: {pom} \n")
    return(score_dealer, score_player)

while play=="y":
    cards_dealer=[]
    cards_player=[]
    for i in range(2):
        cards_dealer.append(cards[random.choice(cards)])
        cards_player.append(cards[random.choice(cards)])
    show_cards('ingame')
    another_card=input("Do you want another card? (y/n)")
    while another_card=="y":
        cards_player.append(cards[random.choice(cards)])
        show_cards('ingame')
        another_card = input("Do you want another card? (y/n)")

    (score_dealer, score_player)=show_cards('endgame')
    while score_dealer<16:
        print("Dealer takes another card...")
        cards_dealer.append(cards[random.choice(cards)])
        (score_dealer, score_player)=show_cards('endgame')

    #(score_dealer, score_player) = show_cards('endgame')
    if score_dealer>21:
        if 11 in cards_dealer:
            score_dealer-=10
        else:
            print(f"Dealer has more than 21, you win with {score_player} points")
    elif score_player>21:
        if 11 in cards_player:
            score_player-=10
        else:
            print(f"You have more than 21, you loose, dealer wins with {score_dealer} points")
    elif score_dealer>score_player:
        print (f"Dealer wins! {score_dealer} : {score_player}")
    else:
        print(f"You win! {score_player} : {score_dealer}")
    play = input("Do you want to play another game? (y/n)")
