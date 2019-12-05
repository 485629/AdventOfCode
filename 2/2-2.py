from copy import deepcopy


def lol(num):
    for i in range(0, len(num), 4):
        if num[i] == 1:
            num[num[i + 3]] = num[num[i + 1]] + num[num[i + 2]]
        if num[i] == 2:
            num[num[i + 3]] = num[num[i + 1]] * num[num[i + 2]]
        if num[i] == 99:
            break
    if num[0] == 19690720:
        print(num[1], num[2])


with open("input.txt", "r") as f:
    numbers = f.readline().split(",")
    nums = []
    for i in range(len(numbers)):
        nums.append(int(numbers[i]))
    for i in range(100):
        for j in range(100):
            new_nums = deepcopy(nums)
            new_nums[1] = i
            new_nums[2] = j
            lol(new_nums)
