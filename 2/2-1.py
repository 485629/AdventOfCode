def lol(num):
    for i in range(0, len(num), 4):
        if num[i] == 1:
            num[num[i + 3]] = num[num[i + 1]] + num[num[i + 2]]
        if num[i] == 2:
            num[num[i + 3]] = num[num[i + 1]] * num[num[i + 2]]
        if num[i] == 99:
            break
    return num


with open("input.txt", "r") as f:
    numbers = f.readline().split(",")
    nums = []
    for j in range(len(numbers)):
        nums.append(int(numbers[j]))

    nums[1] = 12
    nums[2] = 2
    print(lol(nums)[0])
