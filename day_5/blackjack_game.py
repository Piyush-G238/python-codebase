import random

def deal_card():
    """ This function is used to randomly select a card from deck of cards """
    playing_cards = [
        11,  # Ace
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        10,  # jack
        10,  # king
        10  # Queen
    ]
    return random.choice(playing_cards)

def calculate_score(cards):
    """ This function calculate score from list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_sc, computer_sc):
    """
    This function does the comparison based on user_score and computer_score

    Parameters:
        user_sc - score achieved by user
        computer_sc - score achieved by computer
    Returns:
        message to be displayed on console right after comparison
    """
    if user_sc == computer_sc:
        return "Draw"
    elif computer_sc == 0:
        return "Lose, opponent has blackjack"
    elif user_sc == 0:
        return "Win with a blackjack"
    elif user_sc > 21:
        return "You went over, You lose"
    elif computer_sc > 21:
        return "Opponent, went over. You win"
    elif user_sc > computer_sc:
        return "You win"
    else:
        return "You lose"

def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, Your current score: {user_score}")
    print(f"Computer First card: {computer_cards[0]}")

    while not is_game_over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type y to get another card, Type n to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"user final card: {user_cards}, user final score: {user_score}")
    print(f"computer final card: {computer_cards}, computer final score: {computer_score}")
    print(compare_score(user_score, computer_score))

print("Hey, Welcome to Blackjack game!")
while True:
    play_blackjack()
    option = input("Type \"exit\" to quit the game: ")
    if option == "exit":
        break