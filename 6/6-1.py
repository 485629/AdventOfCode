
def count_roads(prvy, key):
    if key not in prvy.keys():
        return 0
    else:
        return 1 + count_roads(prvy, prvy[key])



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
    summ = 0
    for keys in inp.keys():
        summ += count_roads(inp, keys)
    print(summ)
