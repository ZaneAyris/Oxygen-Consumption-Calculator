import pytest
import sys
from datetime import date, datetime
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.join(current_directory, 'Oxygen-Consumption-Calculator')

sys.path.append(project_root)

from models.person import Person
from models.calculator import calculateBMR, calculateVO2

class Struct:
    def __init__(self, **entries): self.__dict__.update(entries)

# Unit Testing
def test_create_person():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "Light")
    assert bob.name == "Bob"
    assert bob.age == 23
    assert type(bob.dob) == date

def test_incorrect_person():
    with pytest.raises(ValueError):
        bob = Person("Bob", "20/12/2000", "70", "180", "eM", "Light")
    with pytest.raises(ValueError):
        bob = Person("Bob", "20/12/2000", "70", "180", "M", "h")


def test_bmr():
    assert(round(calculateBMR(Struct(age = 20, weight=70, height=160, gender="M", activity=2)))) == 2488


def test_incorrect_bmr():
    with pytest.raises(IndexError):
        calculateBMR(Struct(age = 20, weight=70, height=160, gender="M", activity=9))
    with pytest.raises(TypeError):
        calculateBMR(Struct(age = 20, weight=70, height=160, gender="M", activity="Active"))

def test_vo2():
    assert(round(calculateVO2(Struct(age=21, restingHR = 60)))) == 49

# Integration Testing

def test_bmr_with_person():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "Light")
    john = Person("John", "20/12/2000", "70", "180", "F", "Light")
    ben = Person("Ben", "20/12/2023", "8", "30", "M", "Extreme")
    assert round(calculateBMR(bob)) == 2358
    assert round(calculateBMR(john)) == 2130
    assert round(calculateBMR(ben)) == 518


