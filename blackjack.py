main_game_loop = True
play_or_quit = input("Type 's' to start,Type 'q' to quit:").lower()
if play_or_quit == "s":
    main_game_loop = True
elif play_or_quit == "q":
    main_game_loop = False
import random
def calculations():
    #block one
    if player_win_or_lose > win_or_lose:
        print(f"dealer's final hand: [{card_1},{card_2}] the dealer hes a total of: {card_1 + card_2}")
        print(f"you win!")
        main_game_loop = False
    elif pass_or_hit == "h" and player_win_or_lose_2 > win_or_lose:
        print(f"dealer's final hand: [{card_1},{card_2}] the dealer hes a total of: {card_1 + card_2}")
        print(f"you win!")
        main_game_loop = False
    if player_win_or_lose < win_or_lose:
        print(f"dealer's final hand: [{card_1},{card_2}] the dealer hes a total of: {card_1 + card_2}")
        print(f"you lose")
        main_game_loop = False
    elif pass_or_hit == "h" and player_win_or_lose_2 < win_or_lose:
        print(f"dealer's final hand: [{card_1},{card_2}] the dealer hes a total of: {card_1 + card_2}")
        print(f"you lose")
        main_game_loop = False
def dealer():
    print(f"one of dealer's cards: {card_2}")
def player():
    print(f"Your cards are: [{player_card_1},{player_card_2}] you have a total of: {player_card_1 + player_card_2}")
while main_game_loop:
    card_1 = random.randint(1, 10)
    card_2 = random.randint(1, 10)
    win_or_lose = card_1 + card_2
    player_card_1 = random.randint(1, 10)
    player_card_2 = random.randint(1, 10)
    player_card_3 = random.randint(1, 10)
    player_win_or_lose = player_card_1 + player_card_2
    player_win_or_lose_2 = player_card_1 + player_card_2 + player_card_3
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
     """
    print(logo)
    player()
    dealer()
    pass_or_hit = input(f"Type 'h' to hit, Type 'p' to pass:").lower()
    if pass_or_hit == "h":
        print(f"Your cards are: [{player_card_1},{player_card_2},{player_card_3}] you have a total of: {player_card_1 + player_card_2 + player_card_3}")
        calculations()
    elif pass_or_hit == "p":
        calculations()
    play_or_quit = input("play again ? Type 's' to start,Type 'q' to quit:").lower()
    if play_or_quit == "s":
        main_game_loop = True
    elif play_or_quit == "q":
        main_game_loop = False
