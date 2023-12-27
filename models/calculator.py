def calculateBMR(person):
        #Mifflin-St Jeor equation
        bmrMultiplier = [1.2, 1.375, 1.55, 1.725, 1.9]
        baseBMR = 10 * person.weight + 6.25 * person.height - 5 * person.age
        baseBMR = baseBMR + 5 if person.gender == "M" else baseBMR - 161
        return baseBMR * bmrMultiplier[person.activity]


def calculateVO2(person):
        return ((208 - (person.age * 0.7)) / person.restingHR) * 15.3 #ml/kg/min


