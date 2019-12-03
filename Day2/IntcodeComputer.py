import math
FILE_PATH = "intcodeProgram.txt"

def intcode():
    file = open(FILE_PATH, "r")
    # convert file from list of strings to integers
    program = list(map(lambda x: int(x) , file.read().strip().split(',')))

    for i in range(0, len(program), 4):
        opcode = program[i]
        if (opcode == 99): break
        else:
            value1Pos = program[i + 1]
            value2Pos = program[i + 2]
            resultPos = program[i + 3]

            if (opcode == 1):
                # add values
                program[resultPos] = program[value1Pos] + program[value2Pos]
            elif (opcode == 2):
                # multiply values
                program[resultPos] = program[value1Pos] * program[value2Pos]

    print(program[0])
    # print(program)

if __name__ == "__main__":
    intcode()
