from math import inf

first = {}
second = {}

with open("input.txt", "r") as f:
    indexx = 0
    for line in f:
        if indexx == 0:
            index = 1
            x = 0
            y = 0
            line = line.split(",")
            for zoz in line:
                if zoz[0] == "R":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        x += 1
                        first[(x, y)] = index
                        index += 1
                if zoz[0] == "D":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        y -= 1
                        first[(x, y)] = index
                        index += 1
                if zoz[0] == "L":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        x -= 1
                        first[(x, y)] = index
                        index += 1
                if zoz[0] == "U":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        y += 1
                        first[(x, y)] = index
                        index += 1
            indexx += 1
        else:
            index = 1
            x = 0
            y = 0
            line = line.split(",")
            for zoz in line:
                if zoz[0] == "R":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        x += 1
                        second[(x, y)] = index
                        index += 1

                if zoz[0] == "D":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        y -= 1
                        second[(x, y)] = index
                        index += 1
                if zoz[0] == "L":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        x -= 1
                        second[(x, y)] = index
                        index += 1
                if zoz[0] == "U":
                    zoz = zoz[1:]
                    for i in range(int(zoz)):
                        y += 1
                        second[(x, y)] = index
                        index += 1

firstt = set(first.keys())
secondd = set(second.keys())
final = firstt & secondd
minimal = inf

for (x, y) in final:
    if minimal > (abs(x) + abs(y)):
        minimal = abs(x) + abs(y)

print(minimal)
