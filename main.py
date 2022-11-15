class Square:
    def __init__(self, x, y, hoppers, isObstacle):
        self.x = x
        self.y = y
        self.hoppers = hoppers
        self.isObstacle = isObstacle

class Hopper:
    def __init__(self, square, numHops, speed):
        self.square = square
        self.numHops = numHops
        self.speed = speed
 
def isValidSquare(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def hasBeenVisitedByHopper(square, speed):
    for hopper in square.hoppers:
        if hopper.speed == speed:
            return True 
    return False

def solution(startingPosition, targetPosition, width, height, obstacles):
    speedChanges = [[-1,-1], [-1, 0], [-1, 1], [0,-1], [0, 0], [0, 1], [1,-1], [1, 0], [1, 1]]

    grid = [
        [Square(x=i, y=j, hoppers=[], isObstacle=False) for i in range(width)] for j in range(height)
    ]

    for obstacle in obstacles:
        for y in range(obstacle[2], obstacle[3] + 1):
            for x in range(obstacle[0], obstacle[1] + 1):
                grid[y][x] = Square(x=x, y=y, hoppers=[], isObstacle=True)

    startingSquare = grid[startingPosition[1]][startingPosition[0]]
    initialHopper = Hopper(square=startingSquare, numHops=0, speed=[0,0])
    queue = [initialHopper]
    startingSquare.hoppers.append(initialHopper)
    while(len(queue) > 0):
        hopper = queue.pop(0)
        if(hopper.square.x == targetPosition[0] and hopper.square.y == targetPosition[1]):
            return f"Optimal solution takes {hopper.numHops} hops."

        for speedChange in speedChanges:
            hopperSpeed = hopper.speed
            newSpeed = [hopperSpeed[0] + speedChange[0], hopperSpeed[1] + speedChange[1]]
            x = hopper.square.x + newSpeed[0]
            y = hopper.square.y + newSpeed[1]
            if isValidSquare(x, y, width, height):
                landingSquare = grid[y][x]
                if landingSquare.isObstacle == False and hasBeenVisitedByHopper(landingSquare, newSpeed) == False:
                    newHopper = Hopper(square=landingSquare, numHops=hopper.numHops + 1, speed=newSpeed)
                    landingSquare.hoppers.append(newHopper)
                    queue.append(newHopper)
    return "No solution"




# Input
# 1: Number of test cases
# 2: Width height
# 3: Starting point, ending point
# 4: Number of obstacles (P)
# P lines: x1, x2, y1, y2 (obstacle area)
# Example:
#2
#5 5
#4 0 4 4
#1
#1 4 2 3
#3 3
#0 0 2 2
#2
#1 1 0 2
#0 2 1 1
if __name__ == '__main__':
    print("Enter input. To solve simply input a blank line.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print("Input received. Solving...\n")
    for _ in range(int(lines.pop(0))):
        gridSize = [int(i) for i in lines.pop(0).split()]
        positions = [int(i) for i in lines.pop(0).split()]
        numObstacles = int(lines.pop(0))
        obstacles = []
        for _ in range(numObstacles):
            obstacle = [int(i) for i in lines.pop(0).split()]
            obstacles.append(obstacle)
        print(solution(
            startingPosition=[positions[0], positions[1]], 
            targetPosition=[positions[2], positions[3]],
            width=gridSize[0],
            height=gridSize[1],
            obstacles=obstacles))