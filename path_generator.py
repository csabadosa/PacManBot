import numpy as np
import random as rand
# 1 = up, 2 = left, 3 = down, 4 = right
map = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 4, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 4, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 4, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]


def anybodyLeftAlive(alive, population):
    for i in range(population):
        if (alive[i] != 1):
            return False
    return True


def firstGoodDir(possibilities):
    for i in range(4):
        if (possibilities[i] != 0):
            return i


def move(thing):
    if (thing[2] == 1):
        thing[0] -= 1
    elif (thing[2] == 2):
        thing[1] -= 1
    elif (thing[2] == 3):
        thing[0] += 1
    elif (thing[2] == 4):
        thing[1] += 1


def isCaught(pacman, blinky):
    if (pacman[0] == blinky[0] and pacman[1] == blinky[1]):
        return True
    if (pacman[0] == blinky[0] - 1 and pacman[1] == blinky[1]):
        return True
    if (pacman[0] == blinky[0] + 1 and pacman[1] == blinky[1]):
        return True
    if (pacman[0] == blinky[0] and pacman[1] == blinky[1] - 1):
        return True
    if (pacman[0] == blinky[0] and pacman[1] == blinky[1] + 1):
        return True
    return False


def checkAll(pacmans, blinkys, alive, population):
    for i in range(population):
        if (isCaught(pacmans[i], blinkys[i])):
            alive[i] = 0


def addIfPoint(pacmans, points, maps, population):
    for i in range(population):
        if (maps[i][pacmans[i][0]*28+pacmans[i][1]] == 1):
            maps[i][pacmans[i][0]*28+pacmans[i][1]] = 2
            points[i] += 10
        elif (maps[i][pacmans[i][0]*28+pacmans[i][1]] == 4):
            maps[i][pacmans[i][0]*28+pacmans[i][1]] = 2
            points[i] += 40


def movePacman(pacman, map, moves):
    possibilities = []
    if (pacman[1] > 1):
        if (map[pacman[0] * 28 + pacman[1] - 1] != 0):
            if (pacman[2] != 4):
                possibilities.append(2)
    if (pacman[1] < 26):
        if (map[pacman[0] * 28 + pacman[1] + 1] != 0):
            if (pacman[2] != 2):
                possibilities.append(4)
    if (pacman[0] > 1):
        if (map[(pacman[0] - 1) * 28 + pacman[1]] != 0):
            if (pacman[2] != 3):
                possibilities.append(1)
    if (pacman[0] < 29):
        if (map[(pacman[0] + 1) * 28 + pacman[1]] != 0):
            if (pacman[2] != 1):
                possibilities.append(3)
    print(possibilities)
    print(pacman[0], pacman[1])
    if (len(possibilities) > 1):
        index = rand.randint(0, len(possibilities) - 1)
        direction = possibilities[index]
    else:
        direction = possibilities[0]
    if (direction != pacman[2]):
        moves.append((pacman[0], pacman[1], direction))
    pacman[2] = direction

    move(pacman)


def moveBlinky(pacman, blinky, map, blinkyMoves):
    array = []

    array.append((1, np.sqrt((pacman[0] - blinky[0])
                 ** 2 + (pacman[1] - blinky[1] + 1)**2)))

    array.append((2, np.sqrt(
        (pacman[0] - blinky[0] + 1)**2 + (pacman[1] - blinky[1])**2)))

    array.append((3, np.sqrt((pacman[0] - blinky[0])
                 ** 2 + (pacman[1] - blinky[1] - 1)**2)))

    array.append((4, np.sqrt(
        (pacman[0] - blinky[0] - 1)**2 + (pacman[1] - blinky[1])**2)))

    possibilities = []
    if (map[(blinky[0] - 1) * 28 + blinky[1]] != 0):
        possibilities.append(1)
    else:
        possibilities.append(0)

    if (map[blinky[0] * 28 + blinky[1] - 1] != 0):
        possibilities.append(1)
    else:
        possibilities.append(0)

    if (map[(blinky[0] + 1) * 28 + blinky[1]] != 0):
        possibilities.append(1)
    else:
        possibilities.append(0)

    if (map[blinky[0] * 28 + blinky[1] + 1] != 0):
        possibilities.append(1)
    else:
        possibilities.append(0)

    for k in range(3):
        for l in range(4 - k - 1):
            if (array[l][1] > array[l+1][1]):
                s = array[l]
                array[l] = array[l+1]
                array[l+1] = s

                p = possibilities[l]
                possibilities[l] = possibilities[l+1]
                possibilities[l+1] = p

    ind = firstGoodDir(possibilities)
    print(array[ind][0])
    if (blinky[2] != array[ind][0]):
        blinkyMoves.append((pacman[0], pacman[1], array[ind][0]))
    blinky[2] = array[ind][0]

    move(blinky)


def move_things(pacmans, blinkys, pinkys, inkys, clydes, maps, moves, blinkyMoves, population, alive):
    for i in range(population):
        if (alive[i] == 1):
            movePacman(pacmans[i], maps[i], moves[i])
            moveBlinky(pacmans[i], blinkys[i], maps[i], blinkyMoves[i])


def pickBest(moves, pop):
    best = 0
    for i in range(pop):
        if (len(moves[i]) > len(moves[best])):
            best = i
    return best


pacmans = []
blinkys = []
pinkys = []
inkys = []
clydes = []
maps = []

population = 1
desired_points = 3000

moves = []
blinkyMoves = []
points = []
alive = []


for _ in range(population):
    pacmans.append([17, 14, 2])
    blinkys.append([5, 5, 4])
    pinkys.append([5, 21, 2])
    inkys.append([29, 21, 4])
    clydes.append([29, 5, 4])
    maps.append(map)
    moves.append([])
    blinkyMoves.append([])
    points.append(0)
    alive.append(1)
print(pacmans[0][0])
print(pacmans[0][1])
print("Map ertek: ", map[pacmans[0][0]*28+pacmans[0][1]])
i = 0

while (i < 100 and max(points) < desired_points and anybodyLeftAlive(alive, population)):
    print("Points :", max(points))
    checkAll(pacmans, blinkys, alive, population)
    addIfPoint(pacmans, points, maps, population)
    move_things(pacmans, blinkys, pinkys, inkys,
                clydes, maps, moves, blinkyMoves, population, alive)
    i += 1

best = pickBest(moves, population)
print("Best: ", moves[best])
print("Blinky: ", blinkyMoves[best])

f = open("opti_project/src/path.txt", "w")
for i in moves[best]:
    f.write((str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"))
