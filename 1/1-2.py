def fuel_check(fuels):
    return fuels // 3 - 2


with open("input.txt", "r") as f:
    fuel_sum = 0
    for line in f:
        fuel = int(line)
        while True:
            fuel = fuel_check(fuel)
            if fuel > 0:
                fuel_sum += fuel
            else:
                break
    print(fuel_sum)
