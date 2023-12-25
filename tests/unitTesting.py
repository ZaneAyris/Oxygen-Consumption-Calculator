import pytest
import sys
from datetime import date, datetime
sys.path.append(r'C:\Users\Jeff\Desktop\Oxygen-Consumption-Calculator')

from models.person import Person


def test_createPerson():
    bob = Person("Bob", "20/12/2000", "70", "180", "M", "s")
    assert bob.name == "Bob"
    assert bob.age == 23
    assert type(bob.dob) == date
