# Intcode Computer
#
# Instructions:
#   - Opcode 1 (3 params)
#   - Opcode 2 (3 params)
#   - Opcode 3 (1 param)
#   - Opcode 4 (1 param)

FILE_PATH = "diagnosticProgram.txt"

def intcode():
    file = open(FILE_PATH, "r")
    # convert file from list of strings to integers
    program = list(map(lambda x: int(x) , file.read().strip().split(',')))
    # print("Before:", program)

    # program will always start at position 0
    currPos = 0
    instructionLength = 5
    while (True):
        instruction = str(program[currPos]).zfill(instructionLength)
        # two-digit opcode
        opcode = int(instruction[3:])
        # paramater modes (either 0 or 1)
        # 0 == position mode
        # 1 == immediate mode
        param1Mode = int(instruction[2])
        param2Mode = int(instruction[1])
        param3Mode = int(instruction[0])

        # Exit program
        if (opcode == 99):
            print("Code 99: Exiting...")
            break
        
        # Add or Multiply Values
        elif (opcode == 1 or opcode == 2):
            value1 = program[program[currPos + 1]] if param1Mode == 0 else program[currPos + 1]
            value2 = program[program[currPos + 2]] if param2Mode == 0 else program[currPos + 2]
            storePosition = program[currPos + 3] if param3Mode == 0 else currPos + 3
            
            # store value based on opcode
            program[storePosition] = value1 + value2 if opcode == 1 else value1 * value2
            currPos += 4

        # Get User Input
        elif (opcode == 3):
            value = input("Enter ID: ")
            storePosition = program[currPos + 1] if param1Mode == 0 else currPos + 1

            program[storePosition] = int(value)
            currPos += 2

        # Output Diagnostic Code
        elif (opcode == 4):
            valPos = program[currPos + 1] if param1Mode == 0 else currPos + 1
            value = program[valPos]
            
            print("DIAGNOSTIC CODE:", value)
            currPos += 2

        # Jump-if-true
        elif (opcode == 5):
            value1 = program[program[currPos + 1]] if param1Mode == 0 else program[currPos + 1]
            value2 = program[program[currPos + 2]] if param2Mode == 0 else program[currPos + 2]

            if (value1 != 0):
                currPos = value2
            else:
                currPos += 3
        
        # Jump-if-false
        elif (opcode == 6):
            value1 = program[program[currPos + 1]] if param1Mode == 0 else program[currPos + 1]
            value2 = program[program[currPos + 2]] if param2Mode == 0 else program[currPos + 2]

            if (value1 == 0):
                currPos = value2
            else:
                currPos += 3

        # Less than
        elif (opcode == 7):
            value1 = program[program[currPos + 1]] if param1Mode == 0 else program[currPos + 1]
            value2 = program[program[currPos + 2]] if param2Mode == 0 else program[currPos + 2]
            storePosition = program[currPos + 3] if param3Mode == 0 else currPos + 3

            program[storePosition] = 1 if value1 < value2 else 0

            currPos += 4

        # Equals
        elif (opcode == 8):
            value1 = program[program[currPos + 1]] if param1Mode == 0 else program[currPos + 1]
            value2 = program[program[currPos + 2]] if param2Mode == 0 else program[currPos + 2]
            storePosition = program[currPos + 3] if param3Mode == 0 else currPos + 3

            program[storePosition] = 1 if value1 == value2 else 0

            currPos += 4

    # print("After:", program)

if __name__ == "__main__":
    intcode()
