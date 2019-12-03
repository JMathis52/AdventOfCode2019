import math

def fuelCounter():
    fuel = 0
    file = open("./modules.txt", "r")
    for line in file:
        moduleMass = int(line.strip())
        fuel += math.floor(moduleMass / 3) - 2
    return fuel

def fuelCounterWithAddedMass():
    fuel = 0
    file = open("./modules.txt", "r")
    for line in file:
        moduleMass = int(line.strip())
        while (moduleMass > 0):
            nextMass = math.floor(moduleMass / 3) - 2
            if (nextMass <= 0):
                fuel += 0
            else:
                fuel += nextMass
            moduleMass = nextMass
        
    return fuel

if __name__ == "__main__":
    totalFuel = fuelCounterWithAddedMass()
    print(totalFuel)
