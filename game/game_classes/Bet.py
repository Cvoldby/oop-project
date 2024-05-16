"""
This file includes the bet class.

Every bet needs a race, a horse paticipating in that race.

"""
from game_classes import *

class Bet:
    def __init__(self, race: Race) -> None:
        self.race = race
        self.horse = None

        self.bet_amount = 0

    def make_bet(self, amount, horse_name):
        self.bet_amount = amount
        print(self.race.get_name_of_horses())
        if horse_name in self.race.get_name_of_horses():
            self.horse = horse_name
        else:
            print("This horse doesn't compete in this race")

    def calculate_possible_winnings(self):
        self.race.odds[self.horse] * self.bet_amount


if __name__ == "__main__":
    test_bet = Bet(Race())
        