from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice):
    """
    Starts a game of Ten Thousand.

    Parameters:
    - roller (function, optional): A function that returns a list of integers representing the result of rolling a set of dice.
      Default is GameLogic.roll_dice.

    Returns:
    - None

    The function prompts the user to start a game or decline it.
    If the user chooses to start, a new game is started using the given roller function.
    If the user declines, the function exits without starting the game.
    """

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    player_input = input("> ")
    if player_input == 'y':
        start_game(roller)
    elif player_input == 'n':
        print("OK. Maybe another time")


def start_game(roller):
    """
    Starts a new game of Ten Thousand.

    Parameters:
    - roller (function): A function that returns a list of integers representing the result of rolling a set of dice.

    Returns:
    - None

    The function initializes the game state and starts a new round.
    It then prompts the user to enter dice to keep, quit the game, or roll again.
    Depending on the user's choice, the function either handles the input, rolls the dice again,
    or ends the game and prints the player's final score.
    """

    round = 1
    dice_num = 6
    total_score = 0
    # new_round(round)
    new_roll(roller, dice_num, round)
    print("Enter dice to keep, or (q)uit:")
    player_input = input("> ")
    handle_player_input(player_input, dice_num,
                        round, total_score, roller)


def format_roll(dice_roll):
    dice_roll_str = [str(i) for i in dice_roll]
    roll = ' '.join(dice_roll_str)
    return roll


def format_user_input(num):
    num = [char for char in str(num) if char.isdigit()]
    num_tuple = tuple(map(int, num))
    return num_tuple


def calculate_remaining_dices(dice_num, formated_user_input):
    return dice_num-len(formated_user_input)


def new_round(round):
    print(f"Starting round {round}")


def new_roll(roller, dice_num, round):
    new_round(round)
    print(f"Rolling {dice_num} dice...")
    dice_roll = roller(dice_num)
    print(f"*** {format_roll(dice_roll)} ***")


def handle_player_input(player_input, dice_num, round, total_score, roller):
    """
    Handles the user's input during a game of Ten Thousand.

    Parameters:
    - player_input (str): The user's input.
    - dice_num (int): The number of dice being rolled.
    - round (int): The current round of the game.
    - total_score (int): The player's total score.
    - roller (function): A function that returns a list of integers representing the result of rolling a set of dice.

    Returns:
    - None

    The function handles the user's input, updating the game state and prompting the user for further input
    until the game is ended or the player decides to bank their points.
    """

    if player_input == 'q':
        print(f"Thanks for playing. You earned {total_score} points")
    else:
        formated_user_input = format_user_input(player_input)
        unbanked_score = GameLogic.calculate_score(formated_user_input)
        remaining_dices = calculate_remaining_dices(
            dice_num, formated_user_input)
        print(
            f"You have {unbanked_score} unbanked points and {remaining_dices} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        player_input = input("> ")

        if player_input == 'r':
            round += 1
            dice_num = remaining_dices
            new_roll(roller, dice_num, round)
            print("Enter dice to keep, or (q)uit:")
            player_input = input("> ")
            handle_player_input(player_input, dice_num, round, total_score, roller)


        elif player_input == 'b':
            print(f"You banked {unbanked_score} points in round {round}")
            total_score += unbanked_score
            round += 1
            print(f"Total score is {total_score} points")
            # new_round(round)
            new_roll(roller, dice_num, round)
            print("Enter dice to keep, or (q)uit:")
            player_input = input("> ")
            handle_player_input(player_input, dice_num,
                                round, total_score, roller)

        elif player_input == 'q':
            print(f"Thanks for playing. You earned {total_score} points")


if __name__ == "__main__":
    play()
