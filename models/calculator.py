from person import Person

def calculateBMR(person):
        #Mifflin-St Jeor equation
        baseBMR = 10 * person.weight + 6.25 * person.height - 5 * person.age
        match person.gender:
            case "M":
                return baseBMR + 5
            case "F":
                return baseBMR - 161
            case _:
                raise ValueError("Person does not have gender") 

