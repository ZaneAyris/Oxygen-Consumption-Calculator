from person import Person

def calculateBMR(person):
        #Mifflin-St Jeor equation
        bmrMultiplier = [1.2, 1.375, 1.55, 1.725, 1.9]
        baseBMR = 10 * person.weight + 6.25 * person.height - 5 * person.age
        baseBMR = baseBMR + 5 if person.gender == "M" else baseBMR - 161
        return baseBMR * bmrMultiplier[person.activity]


def calculateVO2(bmr, fCarb = 0.5, fFat = 0.3, fProt = 0.2):
        rq = (1.0, 0.7, 0.8)
        ratio = (rq[0] * fCarb + rq[1] * fFat + rq[2] * fProt) /21.1
        return bmr * ratio



bob = Person("Bob", "23/09/2004", "62", "180", "M", "Sedentary")
bobsBmr = calculateBMR(bob)
print(bobsBmr)
bobsVO2 = calculateVO2(bobsBmr)
print(bobsVO2)
