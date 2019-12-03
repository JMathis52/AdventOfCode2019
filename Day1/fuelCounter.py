import math
FILE_PATH = "modules.txt"

# Should return 3303995 for the fuel count
def fuelCounter():
    fuel = 0
    file = open(FILE_PATH, "r")
    for line in file:
        moduleMass = int(line.strip())
        fuel += math.floor(moduleMass / 3) - 2
    return fuel

# Should return 4953118 for the fuel count
def fuelCounterWithAddedMass():
    fuel = 0
    file = open(FILE_PATH, "r")
    for line in file:
        moduleMass = int(line.strip())
        while (moduleMass > 0):
            nextMass = math.floor(moduleMass / 3) - 2
            fuel += 0 if nextMass <= 0 else nextMass
            moduleMass = nextMass
    return fuel

if __name__ == "__main__":
    totalFuel = fuelCounter()
    print(totalFuel)
    totalFuel = fuelCounterWithAddedMass()
    print(totalFuel)
