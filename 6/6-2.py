
def count_roads(prvy, key):
    if key not in prvy.keys():
        return []
    else:
        return count_roads(prvy, prvy[key]) + [key]



with open("input.txt", "r") as f:
    mapa = {}
    inp = {}
    coun = 0
    for line in f:
        first = line.strip().split(")")
        if first[0] not in mapa.keys():
            mapa[first[0]] = [first[1]]
        else:
            mapa[first[0]].append(first[1])
        inp[first[1]] = first[0]
    print(count_roads(inp, "YOU"))
    print(count_roads(inp, "SAN"))
    # print(count_roads(inp, "D"))
    print(count_roads(inp, 'YVD'))
    print(len(count_roads(inp, "YOU")))
    print(len(count_roads(inp, "SAN")))
    # print(len(count_roads(inp, "D")))
    print(len(count_roads(inp, 'YVD')))
    print((280-67) + 313 - 67)
    # print(7-3+5-3)
