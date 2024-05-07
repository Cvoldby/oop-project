"""
This is the Weather class with the diffent subclasses
"""
from scipy.stats import norm

class Weather:
    def __init__(self) -> None:
        self.temperature = None # 0-35
        self.wind_speed = None # 0-16
        self.humitity = None # 20-80


    def __str__(self) -> str:
        return f"This is the weather"
    
    def calculate_weather_effect(self) -> float:
        """This function calculates the weather effect on a race"""

        temp_effect = (self.temperature / 38)**2
        wind_effect = (self.wind_speed / 20)**2
        humidity_effect = ((50-self.humitity)/80)**2

        weather_effect = (temp_effect + wind_effect + humidity_effect) / 3
        return weather_effect
        


class Windy(Weather):
    def __init__(self) -> None:
        super().__init__()

        self.humitity = norm.rvs(loc=40,scale=5)
        self.wind_speed = norm.rvs(loc=14, scale=4)
        self.temperature = norm.rvs(loc=20, scale=5)

        self.weather_effect = self.calculate_weather_effect()


class Hot(Weather):
    def __init__(self) -> None:
        super().__init__()

        self.humitity = norm.rvs(loc=30,scale=8)
        self.wind_speed = abs(norm.rvs(loc=3, scale=2))
                
        
        self.temperature = norm.rvs(loc=33, scale=4)

        self.weather_effect = self.calculate_weather_effect()


class Tropical(Weather):
    def __init__(self) -> None:
        super().__init__()

        self.humitity = norm.rvs(loc=70,scale=7)
        self.wind_speed = norm.rvs(loc=8, scale=2)
        self.temperature = norm.rvs(loc=25, scale=5)

        self.weather_effect = self.calculate_weather_effect()



if __name__ == '__main__':
    """Testing site"""
    
    for _ in range(10):
        h = Hot()
        
        print(f"Hot: {h.weather_effect}")
        
    for _ in range(10):
        t = Tropical()

        print(f"Tropical: {t.weather_effect}")
    
    for _ in range(10):
        w = Windy()

        print(f"Windy: {w.weather_effect}")