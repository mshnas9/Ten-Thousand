from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice, num_rounds=20):
    """Starts the game, asks the player if they want to play and begins the game."""
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    player_input = input("> ")
    if player_input == 'y':
        start_game(roller, num_rounds)
    elif player_input == 'n':
        print("OK. Maybe another time")


def start_game(roller, num_rounds):
    """Starts a game of Ten Thousand."""
    max_rounds = num_rounds
    total_score = 0

    for round in range(1, max_rounds + 1):
        new_round(round)
        unbanked_score = 0
        remaining_dices = 6
        while True:
            dice_roll = new_roll(roller, remaining_dices)

            if GameLogic.calculate_score(dice_roll) == 0:
                zilch()
                print(f"You banked 0 points in round {round}")
                print(f"Total score is {total_score} points")
                break

            print("Enter dice to keep, or (q)uit:")
            player_input = input("> ")
            while True:
                if player_input == 'q':
                    print(
                        f"Thanks for playing. You earned {total_score} points")
                    return
                formatted_user_input = format_user_input(player_input)
                if GameLogic.validate_keepers(dice_roll, formatted_user_input):
                    break
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    print(f"*** {format_roll(dice_roll)} ***")
                    print("Enter dice to keep, or (q)uit:")
                    player_input = input("> ")

            if player_input != 'q':
                formated_user_input = format_user_input(player_input)
                unbanked_score += GameLogic.calculate_score(
                    formated_user_input)
                remaining_dices = calculate_remaining_dices(
                    remaining_dices, formated_user_input)

                if remaining_dices == 0 and GameLogic.calculate_score(
                        formated_user_input) > 0:
                    remaining_dices = 6
                print(
                    f"You have {unbanked_score} unbanked points and {remaining_dices} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                player_input = input("> ")
                if player_input == 'r':
                    pass
                elif player_input == 'b':
                    print(
                        f"You banked {unbanked_score} points in round {round}")
                    total_score += unbanked_score
                    print(f"Total score is {total_score} points")
                    break
                elif player_input == 'q':
                    print(
                        f"Thanks for playing. You earned {total_score} points")
                    return
        if round == max_rounds or total_score >= 10000:
            print(f"Thanks for playing. You earned {total_score} points")
            break


def format_roll(dice_roll):
    """Formats the dice roll for output."""
    dice_roll_str = [str(i) for i in dice_roll]
    roll = ' '.join(dice_roll_str)
    return roll


def format_user_input(num):
    """Formats the user input for validation."""
    num = [char for char in str(num) if char.isdigit()]
    num_tuple = tuple(map(int, num))
    return num_tuple


def calculate_remaining_dices(dice_num, formated_user_input):
    """Calculate the number of remaining dices after the user has selected which ones to keep."""
    return dice_num - len(formated_user_input)


def new_round(round):
    """Print the start of a new round."""
    print(f"Starting round {round}")


def new_roll(roller, dice_num):
    """Roll a number of dices and return the results."""
    print(f"Rolling {dice_num} dice...")
    dice_roll = roller(dice_num)
    print(f"*** {format_roll(dice_roll)} ***")
    return dice_roll


def zilch():
    """Zilch message, appear when the dices have no scores """
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")

if __name__ == "__main__":
    play()
