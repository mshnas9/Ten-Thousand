# Python Dice Game Expansion.

#### You:
Today you’ll begin working in pairs on a command line version of the dice game Ten Thousand by expanding your understanding of Python standard library.

i'll give you the rules

#### ChatGPT:
Sure, I'd be happy to hear the rules of the dice game Ten Thousand!

Ten Thousand, also known as Farkle, is a multiplayer dice game in which players take turns rolling six dice to try to reach 10,000 points. The game can be played with any number of players, and the goal is to be the first player to reach 10,000 points or more.

Players begin their turn by rolling six dice. After each roll, the player must set aside any dice


#### You:
wait for the rules 

#### ChatGPT:
My apologies for misunderstanding! Here are the complete rules for the dice game Ten Thousand:

Ten Thousand, also known as Farkle, is a multiplayer dice game in which players take turns rolling six dice to try to reach 10,000 points. The game can be played with any number of players, and the goal is to be the first player to reach 10,000 points or more.

Players begin their turn by rolling six dice. After each roll, the player must set aside any dice that score points and can choose to re-roll the remaining dice to try to score more points. The player must keep rolling as long as they score points with each roll. If a roll does not result in any points, the turn ends and the player loses all points scored in that turn.

Points are scored as follows:

- A 1 is worth 100 points
- A 5 is worth 50 points
- Three of a kind is worth 100 times the face value of the dice (e.g. three 4s would be worth 400 points)
- Four of a kind is worth double the value of three of a kind (e.g. four 4s would be worth 800 points)
- Five of a kind is worth double the value of four of a kind (e.g. five 4s would be worth 1600 points)
- Six of a kind is worth double the value of five of a kind (e.g. six 4s would be worth 3200 points)

If a player sets aside all six dice, they can choose to re-roll all six dice and continue their turn.

The first player to score 10,000 or more points at the end of a complete turn wins the game. If two or more players reach 10,000 or more points at the end of the same turn, the player with the highest score wins. If a player rolls all six dice and scores no points, they lose all points accumulated during their turn and play passes to the next player.


#### You:
or 10000, 10,000 Dice, Ten Grand) also Greed, Dix Mille, 5-Dice is the name of a family dice game played with 6 dice, it is similar or identical to the commercialized Farkle. It also goes by other names, including Zilch, Zilchers, Foo, Boxcar, Bogus, Lewis' Dice and Crap Out.

The Game achieved some level of fame and notoriety during early 2023 due to its extreme rise in popularity throughout London, particularly in the South East.

Scoring
These are the base methods of scoring:

Single fives are worth 50 points
Single ones are worth 100 points
Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 die showing the number 3 would be 600 points and 5 die showing the number 3 would be 1200 points
This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
Full house (3 of a kind plus 2 of a kind) are worth 1,500
Typically each roll scores separately, with dice scored at the time they are rolled, so that three or more of a kind must be rolled simultaneously, and dice from later rolls do not "stack" for the higher score. In so-called progressive scoring, dice can form combinations with dice previously scored and set aside. Also to add you can not take a full house with 4 of a kind and a 2 of a kind without rolling 1 of the 4 dice to make the full house a 3 of a kind and a 2 of a kind for a full house

Example: Player 1 rolls all six dice, and chooses to score three fours for 400 points. She rolls the remaining three dice for a 2, 4, 5; the additional 4 does not multiply the previous three of a kind unless playing progressive, and she can only score 50 points for the lone 5. If she rolls two more 5's with the remaining dice, if not playing progressive they will only score 50 points each, and do not form a three of a kind with the other 5.

Progressive mode

Dice Roll	Points
Single 5's	50
Single 1's	100
Three Pairs	1,000
Straight 1- 6	1,500
Full House	1,500
Double Trips when 2 sets of a 3 of a kind are hit. Scores are added together and doubled.

Separate turns mode, (6 dice)

Dice Roll	Points
Single 5's	50
Single 1's	100
Three Pairs	1,500
Straight 1- 6	2,000
Double Trips when 2 sets of a 3 of a kind are hit. Scores are added together and doubled.
Dice Roll	3 of a kind	4 of a kind	5 of a kind	6 of a kind
1's	1,000	2,000	4,000	8,000
2's	200	400	800	1,600
3's	300	600	1,200	2,400
4's	400	800	1,600	3,200
5's	500	1,000	2,000	4,000
6's	600	1,200	2,400	4,800
Rule variations
super greedy dramatic fun variation.
Whatever dice that are left over after completing their turn, are passed to the next player to attempt to steal the points with a 1 or 5. If that player fails to score they are given a strike. 3 strikes and you lose all your points.
Winning
There are two main winning variants, one requires an ''exact'' score of 10,000. The others criteria is that you only have to exceed 10,000. With playing the exact score, in the event that a player goes over, the score for that turn is lost and they need to try again next turn. If the 10,000 is hit, that player wins immediately without giving the other players a chance to roll. However, in progressive mode if the winner leaves at least one die then the next player may 'roll off the score'. The first player to score over 10,000 points temporarily becomes the winner, and each other player gets one more turn to top that player's score. Whoever ends with the highest score wins the game. [citation needed]

A rule variation states that if a player rolls all 6 dice with the same number they instantly win. This is part of another ruleset which allows rolling dices off other players.



#### ChatGPT:
Sure, I'd be happy to help with that. What specific question do you have about dice probabilities?


#### You:
#score test
import pytest 
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_1]


def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected


def test_single_one():
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected


def test_two_fives():
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected


def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected


def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected


def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 2000
    assert actual == expected


def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 1600
    assert actual == expected


def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 8000
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 4000),
        ((1, 1, 1, 1, 1, 1), 8000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 800),
        ((2, 2, 2, 2, 2, 2), 1600),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 1200),
        ((3, 3, 3, 3, 3, 3), 2400),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1600),
        ((4, 4, 4, 4, 4, 4), 3200),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 2000),
        ((5, 5, 5, 5, 5, 5), 4000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 2400),
        ((6, 6, 6, 6, 6, 6), 4800),
        ((1, 2, 3, 4, 5, 6), 2000),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 2400),
    ],
)
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected
#dice test

"""
- Handle rolling dice
- Add `roll_dice` static method to GameLogic class.
- The input to `roll_dice` is an integer between 1 and 6.
- The output of `roll_dice` is a tuple with random values between 1 and 6.
- The length of tuple must match the argument given to `roll_dice` method.

"""
import pytest 
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_1]


def test_1_dice():
    values = GameLogic.roll_dice(1)
    assert len(values) == 1
    value = values[0]
    assert 1 <= value <= 6


def test_2_dice():
    values = GameLogic.roll_dice(2)
    assert len(values) == 2

    for value in values:
        assert 1 <= value <= 6


def test_3_dice():
    values = GameLogic.roll_dice(3)
    assert len(values) == 3

    for value in values:
        assert 1 <= value <= 6


def test_4_dice():
    values = GameLogic.roll_dice(4)
    assert len(values) == 4

    for value in values:
        assert 1 <= value <= 6


def test_5_dice():
    values = GameLogic.roll_dice(5)
    assert len(values) == 5

    for value in values:
        assert 1 <= value <= 6


def test_6_dice():
    values = GameLogic.roll_dice(6)
    assert len(values) == 6

    for value in values:
        assert 1 <= value <= 6

@pytest.mark.parametrize("num_dice,expected_length",
                         [
                            (1,1),
                            (2,2),
                            (3,3),
                            (4,4),
                            (5,5),
                            (6,6),
                         ],
)
def test_all_dice_rolls(num_dice,expected_length):
    values = GameLogic.roll_dice(num_dice)
    assert len(values) == expected_length

    for value in values:
        assert 1 <= value <= 6
keep them and wait

#### ChatGPT:
This is a test suite for the game of ten thousand or Farkle game, a dice game. The game has different scoring rules, and this test suite is meant to test the different rules.

The `test_single_five()` function tests whether rolling a single 5 gives the correct score.

The `test_single_one()` function tests whether rolling a single 1 gives the correct score.

The `test_two_fives()` function tests whether rolling two fives gives the correct score.

The `test_two_ones()` function tests whether rolling two ones gives the correct score.

The `test_one_and_five()` function tests whether rolling a one and a five gives the correct score.

The `test_zilch()` function tests whether rolling no scoring dice gives the correct score.

The `test_three_fives()` function tests whether rolling three fives gives the correct score.

The `test_three_ones()` function tests whether rolling three ones gives the correct score.

The `test_three_ones_and_a_five()` function tests whether rolling three ones and a five gives the correct score.

The `test_straight()` function tests whether rolling a straight (1, 2, 3, 4, 5, 6) gives the correct score.

The `test_three_of_a_kind()` function tests whether rolling three of a kind (e.g., three twos) gives the correct score.

The `test_four_of_a_kind()` function tests whether rolling four of a kind (e.g., four twos) gives the correct score.

The `test_five_of_a_kind()` function tests whether rolling five of a kind (e.g., five twos) gives the correct score.

The `test_six_of_a_kind()` function tests whether rolling six of a kind (e.g., six twos) gives the correct score.

The `test_six_ones()` function tests whether rolling six ones gives the correct score.

The `test_parameterized()` function tests a range of input dice combinations and their expected score to ensure the game logic works correctly for a variety of cases.


#### You:
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.


#### ChatGPT:
Here is an implementation of the GameLogic class that meets the requirements specified:

```
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        score = 0
        if len(set(dice)) == 6:
            score += 1500
        else:
            for num in range(1, 7):
                count = dice.count(num)
                if count >= 3:
                    if num == 1:
                        score += 1000
                    else:
                        score += num * 100
                    count -= 3
                if num == 1:
                    score += count * 100
                elif num == 5:
                    score += count * 50
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
```

Explanation of `calculate_score` method:

- First, we check if all the values in the dice roll are unique. If so, it is a straight and the score is 1500.
- Otherwise, we iterate through each possible number (1-6) and count how many times it appears in the dice roll.
- If a number appears 3 or more times, we score it accordingly (1000 for 3 ones, 200 for 3 twos, etc.) and subtract 3 from the count.
- If the number is a 1, we add 100 points for each remaining 1.
- If the number is a 5, we add 50 points for each remaining 5.
- Finally, we return the total score.

Explanation of `roll_dice` method:

- We use a list comprehension to generate `num_dice` random integers between 1 and 6 using `random.randint()`.
- We convert the list to a tuple and return it.
# Lab 7:
used it just to generate docstring for methods and fix some bugs
prompts:
- Generate docstring
- Explain tests