with open("input.txt", "r") as f:
    numbers = f.readline().split(",")
    nums = []
    for i in range(len(numbers)):
        nums.append(int(numbers[i]))
    counter = 0
    # print(len(nums))
    while True:
        # print(nums)
        # print(counter)
        # print(nums[:15])
        # print(nums[225])

        if nums[counter] == 1:
            nums[nums[counter + 3]] = nums[nums[counter + 1]] + nums[nums[counter + 2]]
            counter += 4
            continue
        if nums[counter] == 2:
            nums[nums[counter + 3]] = nums[nums[counter + 1]] * nums[nums[counter + 2]]
            counter += 4
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
        if nums[counter] == 99:
            break
        if nums[counter] > 4:
            flags = []
            flags.append(nums[counter] // 100 % 10)
            flags.append(nums[counter] // 1000 % 10)
            if nums[counter] % 10 == 3:
                inp = int(input())
                nums[nums[counter + 1]] = inp
                counter += 2
                continue
            if nums[counter] % 10 == 4:
                print(nums[nums[counter + 1]])
                counter += 2
                continue

            if flags[0] == 1:
                first = nums[counter + 1]
            if flags[0] == 0:
                first = nums[nums[counter + 1]]
            if flags[1] == 1:
                second = nums[counter + 2]
            if flags[1] == 0:
                second = nums[nums[counter + 2]]
            if nums[counter] % 10 == 1:
                nums[nums[counter + 3]] = first + second
            if nums[counter] % 10 == 2:
                nums[nums[counter + 3]] = first * second
            counter += 4
            continue
