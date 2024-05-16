"""This file includes the stuff """
from random import randint

from Horse import Horse
from Race import Race
from Weather import *
from Bet import Bet

horse_names = [
    "Dolly",
    "Tarok",
    "Ivan",
    "Pingo",
    "Zimba",
    "John",
    "Stuart",
    "Ejnar",
    "Loke",
    "Mulle",
    "Hubert",
    "Anker"
]

HORSES = [Horse(horse_names[i], randint(7,14)) for i in range(len(horse_names))]


