import random
from typing import Tuple
from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(dice: Tuple[int, ...]) -> int:
        """
        Calculate the score for the given dice roll based on the rules of the game.

        :param dice: a tuple of integers representing the values of the rolled dice
        :return: an integer representing the score of the roll
        """
        score = 0

        # check for three of a kind
        for i in range(1, 7):
            if dice.count(i) >= 3:
                if i == 1:
                    score += 1000
                else:
                    score += i * 100

                # check for four, five, or six of a kind
                if dice.count(i) >= 4:
                    score *= 2
                if dice.count(i) >= 5:
                    score *= 2
                if dice.count(i) == 6:
                    score *= 2

        # check for single fives and ones when there are less than three
        score += dice.count(5) * 50 if dice.count(5) < 3 else 0
        score += dice.count(1) * 100 if dice.count(1) < 3 else 0

        # check for a straight
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            score = 2000

        # check for three pairs
        elif len(set(dice)) == 3 and all(dice.count(i) == 2 for i in set(dice)):
            score = 1500

        # check for three pairs
        elif len(set(dice)) == 2 and all(dice.count(i) == 3 for i in set(dice)):
            score = 2400

        # check for full house
        elif len(set(dice)) == 2 and all(dice.count(i) in [2, 3] for i in set(dice)):
            score = 1500

        return score

    @staticmethod
    def roll_dice(num_dice: int) -> Tuple[int, ...]:
        """
        Roll the given number of dice and return the tuple of dice values.

        :param num_dice: an integer representing the number of dice to roll
        :return: a tuple of integers representing the values of the rolled dice
        """
        dice = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice

    def get_scorers(test_input):
        full_score = GameLogic.calculate_score(test_input)
        scorers = []

        for i in range(len(test_input)):
            # remove the i-th dice from the tuple
            test_rolls = test_input[:i] + test_input[i+1:]
            # calculate the score without the i-th dice
            test_score = GameLogic.calculate_score(test_rolls)
            if test_score < full_score:
                scorers.append(test_input[i])
        
        return tuple(scorers)

    def validate_keepers(roll, keepers):
        """
        Validates whether the user's selection of keepers is valid or not.

        Arguments:
        - roll: a list of integers representing the dice values rolled
        - keepers: a list of integers representing the dice values selected by the user to keep

        Returns:
        - True if the user's selection of keepers is valid(when sub result is empty), False otherwise
        """
        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        result_counter = keepers_counter - roll_counter
        return not result_counter
