"""
This file includes the race class

Every race has 6 horses competing.

The following parameters effects the race.
- Wheather
- Laps
- 
"""
from time import sleep
from random import sample
from scipy.stats import rv_discrete

from Weather import Hot, Windy, Tropical
from __init__ import *


class Race:
    def __init__(self) -> None:
        self.id = 0
        self.laps = 1 # randint(1,5) # perhaps more laps as development comes along
        self.length_lap = 10

        self.horses = sample(HORSES, 6)
        self.weather = sample([Hot, Windy, Tropical], 1)
        self.weather = self.weather[0]()
        self.weather_effect = self.weather.calculate_weather_effect()
        self.position = {
            idx: [horse.name, 0] for idx, horse in enumerate(self.horses)
        }

        self.odds = {}


    def get_name_of_horses(self):
        return [horse.name for horse in self.horses]

    def get_race_state(self):
        print(self.position)


    def calculate_odds(self):
        temp_sum = 0
        for horse in self.horses:
            temp_sum += horse.calculate_race_stat(self.weather_effect)
        

        for horse in self.horses:
            self.odds[horse.name] = round(horse.calculate_race_stat(self.weather_effect)/temp_sum, 3)

        while sum(self.odds.values()) != 1:
            if sum(self.odds.values()) < 1:
                self.odds[sample(self.horses, 1)[0].name] += 1-sum(self.odds.values())
            if sum(self.odds.values()) > 1:
                self.odds[sample(self.horses, 1)[0].name] -= sum(self.odds.values())-1
        
        #return self.odds


    def discrete(self):
        pk = list(self.odds.values())
        #print(pk)
        discrete_rv = rv_discrete(name='Odds', values=(range(6), pk))
        return discrete_rv


    def check_for_winner(self):
        for idx, pos in enumerate(self.position.values()):
            #print(idx, pos)
            if pos[1] == self.length_lap:
                return idx
            
        return -1


    def run_race(self):
        R = self.discrete()

        winner = -1
        while winner < 0:
            r1 = R.rvs()
            r2 = R.rvs()

            self.position[r1][1] += 1
            self.position[r2][1] += 1

            print(list(self.position.values()))
            
            winner = self.check_for_winner()
            sleep(1)

        winner = self.position[self.check_for_winner()]
        print(f"The winner is {winner[0]}")
        return winner
    
    def run_once(self):
        R = self.discrete()
        r1 = R.rvs()
        r2 = R.rvs()

        self.position[r1][1] += 1
        self.position[r2][1] += 1

        print(list(self.position.values()))
        
        winner = self.check_for_winner()
        if winner > 0:
            winner = self.position[self.check_for_winner()]
            print(f"The winner is {winner[0]}")
            return winner


    def push_to_database(self):
        pass


if __name__ == "__main__":
    test = Race()

    test.get_race_state()

    test.calculate_odds()
    print(test.odds)

    RV = test.discrete()
    print(RV.rvs())

    print()
    print("start race")
    test.run_race()


