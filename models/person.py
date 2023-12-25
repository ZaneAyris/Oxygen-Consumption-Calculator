from datetime import date, datetime

def calculateAge(born):
    if type(born) != date:
        born = datetime.strptime(born, "%d/%m/%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class Person:
    def __init__(self, name, dob, weight, height, gender, activity):
        self.name = name
        self.dob = dob
        self.weight = int(weight)
        self.height = int(height)
        self.gender = gender
        self.activity = activity
        self.age = int(calculateAge(dob))

    
    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        self._dob = datetime.strptime(value, "%d/%m/%Y").date()

    @property
    def age(self):
        currAge = calculateAge(self.dob)
        if currAge != self._age:
            self._age = currAge
        return currAge

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = float(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = float(value)
    
    @age.setter
    def age(self, value):
        self._age = int(value)
    
    def __str__(self):
        return f'{self.name}'

