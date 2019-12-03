FILE_PATH = "wires.txt"
ROWS = 1000
COLUMNS = 1000
C_PORT_X = 10
C_PORT_Y = COLUMNS - 500
BOARD_DEF_CHAR = "."
BOARD = [[BOARD_DEF_CHAR for x in range(ROWS)] for y in range(COLUMNS)]

def manhattanDistance(point1, point2):
    return (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def findIntersections():
    # initial board setup
    # central port of board is at pos 1,1
    BOARD[C_PORT_Y][C_PORT_X] = 'O'
    printCircuitBoard()
    wire1, wire2 = readFile(FILE_PATH)

    # Draw Wire 1
    drawPath(C_PORT_X, C_PORT_Y, wire1, False)
    # Draw Wire 2 and check for intersections
    intersections = drawPath(C_PORT_X, C_PORT_Y, wire2, True)

    printCircuitBoard()
    return intersections

def drawPath(X, Y, wire, checkIntersection):
    if (checkIntersection):
        intersections = []
        for v in wire:
            direction = v[0]
            distance = int(v[1:])

            if (direction == "R"):
                for i in range(1, distance + 1):
                    if (BOARD[Y][X + i] != BOARD_DEF_CHAR):
                        intersections.append((X + i, Y))
                        BOARD[Y][X + i] = "+"
                    else:
                        BOARD[Y][X + i] = "A"
                X += distance
            elif (direction == "L"):
                for i in range(1, distance + 1):
                    if (BOARD[Y][X - i] != BOARD_DEF_CHAR):
                        intersections.append((X + i, Y))
                        BOARD[Y][X - i] = "+"
                    else:
                        BOARD[Y][X - i] = "A"
                X -= distance
            elif (direction == "U"):
                for i in range(1, distance + 1):
                    if (BOARD[Y - i][X] != BOARD_DEF_CHAR):
                        intersections.append((X + i, Y))
                        BOARD[Y - i][X] = "+"
                    else:
                        BOARD[Y - i][X] = "A"
                Y -= distance
            elif (direction == "D"):
                for i in range(1, distance + 1):
                    if (BOARD[Y + i][X] != BOARD_DEF_CHAR):
                        intersections.append((X + i, Y))
                        BOARD[Y + i][X] = "+"
                    else:
                        BOARD[Y + i][X] = "A"
                Y += distance
        return intersections
    else:
        for v in wire:
            direction = v[0]
            distance = int(v[1:])

            if (direction == "R"):
                for i in range(1, distance + 1):
                    BOARD[Y][X + i] = "X"
                X += distance
            elif (direction == "L"):
                for i in range(1, distance + 1):
                    BOARD[Y][X - i] = "X"
                X -= distance
            elif (direction == "U"):
                for i in range(1, distance + 1):
                    BOARD[Y - i][X] = "X"
                Y -= distance
            elif (direction == "D"):
                for i in range(1, distance + 1):
                    BOARD[Y + i][X] = "X"
                Y += distance

def printCircuitBoard():
    for row in BOARD:
        for col in row:
            print(col, end=" ")
        print()

def readFile(filename):
    file = open(filename, "r")
    wires = []
    for line in file:
        wires.append(list(line.strip().split(',')))
    
    return wires

if __name__ == "__main__":
    intersections = findIntersections()
    print(min(list(map(lambda x: manhattanDistance((C_PORT_X, C_PORT_Y), x), intersections))))
