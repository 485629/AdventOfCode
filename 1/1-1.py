def fuel_check(fuel):
    return fuel // 3 - 2


with open("input.txt", "r") as f:
    fuel_sum = 0
    for line in f:
        fuel_sum += fuel_check(int(line))
    print(fuel_sum)
