def firstsecond(counter, nums, flag):
    first = 0
    second = 0
    if flag[0] == 1:
        first = nums[counter + 1]
    if flag[0] == 0:
        first = nums[nums[counter + 1]]
    if flag[1] == 1:
        second = nums[counter + 2]
    if flag[1] == 0:
        second = nums[nums[counter + 2]]
    return first, second


def opcode12(counter, nums, flag, opcode):
    first, second = firstsecond(counter, nums, flag)
    if opcode == 1:
        nums[nums[counter + 3]] = first + second
    if opcode == 2:
        nums[nums[counter + 3]] = first * second
    return counter + 4


def opcode56(counter, nums, flag, opcode):
    first, second = firstsecond(counter, nums, flag)
    if (opcode == 5 and first != 0) or (opcode == 6 and first == 0):
        return second
    else:
        return counter + 3


def opcode78(counter, nums, flag, opcode):
    first, second = firstsecond(counter, nums, flag)
    if opcode == 7:
        if first < second:
            nums[nums[counter + 3]] = 1
        else:
            nums[nums[counter + 3]] = 0
    if opcode == 8:
        if first == second:
            nums[nums[counter + 3]] = 1
        else:
            nums[nums[counter + 3]] = 0
    return counter + 4


with open("input.txt", "r") as f:
    numbers = f.readline().split(",")
    nums = []
    for i in range(len(numbers)):
        nums.append(int(numbers[i]))
    counter = 0
    while True:
        if nums[counter] == 99:
            break

        if nums[counter] == 1:
            counter = opcode12(counter, nums, [0, 0], 1)
            continue
        if nums[counter] == 2:
            counter = opcode12(counter, nums, [0, 0], 2)
            continue
        if nums[counter] == 3:
            inp = int(input())
            nums[nums[counter + 1]] = inp
            counter += 2
            continue
        if nums[counter] == 4:
            print(nums[nums[counter + 1]])
            counter += 2
            continue
        if nums[counter] == 5:
            counter = opcode56(counter, nums, [0, 0], 5)
            continue
        if nums[counter] == 6:
            counter = opcode56(counter, nums, [0, 0], 6)
            continue
        if nums[counter] == 7:
            counter = opcode78(counter, nums, [0, 0], 7)
            continue
        if nums[counter] == 8:
            counter = opcode78(counter, nums, [0, 0], 8)
            continue

        if nums[counter] > 8:
            flags = []
            flags.append(nums[counter] // 100 % 10)
            flags.append(nums[counter] // 1000 % 10)
            if nums[counter] % 10 == 1:
                counter = opcode12(counter, nums, flags, 1)
                continue
            if nums[counter] % 10 == 2:
                counter = opcode12(counter, nums, flags, 2)
                continue
            if nums[counter] % 10 == 3:
                inp = int(input())
                nums[nums[counter + 1]] = inp
                counter += 2
                continue
            if nums[counter] % 10 == 4:
                if flags[0] == 0:
                    print(nums[nums[counter + 1]])
                else:
                    print(nums[counter + 1])
                counter += 2
                continue
            if nums[counter] % 10 == 5:
                counter = opcode56(counter, nums, flags, 5)
                continue
            if nums[counter] % 10 == 6:
                counter = opcode56(counter, nums, flags, 6)
                continue
            if nums[counter] % 10 == 7:
                counter = opcode78(counter, nums, flags, 7)
                continue
            if nums[counter] % 10 == 8:
                counter = opcode78(counter, nums, flags, 8)
                continue

