"""
This file includes the horse classes.

Every horse receive the same attributes at random levels

"""
from scipy.stats import norm
from random import randint

class Horse:
    def __init__(self, name=None, age=None) -> None:
        self.name = name 
        self.age = age
        
        self.speed = int(norm.rvs(loc=75, scale=5))
        self.accelaration = int(norm.rvs(loc=60, scale=10))
        self.attitude = int(norm.rvs(loc=50, scale=20))
        self.overtake_ability = randint(1, 5)
        self.endurance = int(norm.rvs(loc=78, scale=4))
        self.weather_resilience = int(norm.rvs(loc=64, scale=12))

    def __str__(self) -> str:
        return f"This horse is called: {self.name} and is {self.age} years old."

    def return_level_of_skills(self):
        """Return relevent attribute stats"""
        
        return self.speed, self.accelaration, self.attitude, self.endurance #, self.weather_resilience

    def enter_race(self, race):
        pass

    def calculate_race_stat(self, weather_effect):
        race_score = (sum(self.return_level_of_skills())+self.weather_resilience*weather_effect)/5

        return round(race_score,2)


if __name__ == '__main__':
    name_of_horses = ['John', 'Chris', 'Dolly', 'Tarok']
    
    for name in name_of_horses:
        hest = Horse(name)
        print(hest.return_level_of_skills())

        print(hest.calculate_race_stat(0.4))
