import pytest
import sys
from datetime import date, datetime
import os
from models.person import Person

current_directory = os.path.dirname(os.path.realpath(__file__))
relative_path = os.path.join(current_directory, 'Oxygen-Consumption-Calculator')

sys.path.append(relative_path)



def test_createPerson():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "s")
    assert bob.name == "Bob"
    assert bob.age == 23
    assert type(bob.dob) == date

def test_incorrectPerson():
    with pytest.raises(ValueError):
        bob = Person("Bob", "20/12/2000", "70", "180", "eM", "s")
