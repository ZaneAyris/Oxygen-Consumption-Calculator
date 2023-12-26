import pytest
import sys
from datetime import date, datetime
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.join(current_directory, 'Oxygen-Consumption-Calculator')

sys.path.append(project_root)

from models.person import Person
from models.calculator import calculateBMR, calculateVO2


def test_createPerson():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "Light")
    assert bob.name == "Bob"
    assert bob.age == 23
    assert type(bob.dob) == date

def test_incorrectPerson():
    with pytest.raises(ValueError):
        bob = Person("Bob", "20/12/2000", "70", "180", "eM", "Light")
    with pytest.raises(ValueError):
        bob = Person("Bob", "20/12/2000", "70", "180", "M", "h")

def test_bmr():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "Light")
    john = Person("John", "20/12/2000", "70", "180", "F", "Light")
    assert round(calculateBMR(bob)) == 2358
    assert round(calculateBMR(john)) == 2130
