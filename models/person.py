class Person:
    def __init__(self, name, dob, weight, height, gender, activity):
        self.name = name
        self.dob = dob
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity = activity

    def calculate(self, calculator):
        return calculator.calculate(self)

    def __str__(self):
        return f'{self.name}'
