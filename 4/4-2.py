counter = 0
for i in range(245182, 790572):
    flag = [0, 0]
    num = str(i)
    nums = [int(x) for x in num]
    minimal = 0
    for j in range(6):
        if nums[j] >= minimal:
            minimal = nums[j]
        else:
            flag[0] = 2
    coun = [0 for _ in range(10)]
    for j in range(6):
        for k in range(10):
            if k == nums[j]:
                coun[k] += 1
    for i in range(10):
        if coun[i] == 2:
            flag[1] = 1
    if flag[0] == 0 and flag[1] == 1:
        counter += 1

print(counter)
