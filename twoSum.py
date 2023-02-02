from ast import List

def twoSum(nums, target):
    # n = len(nums)

    # for i in range(n):
    #     # print(i)
    #     tem_num= nums[i:]
    #     print(tem_num)
    #     new_n = len(tem_num)

    #     for j in range(new_n):
    #         print(i, j+1)
    #         if j < new_n-1 and nums[i] + tem_num[j+1] == target:
    #             return [i, j+i+1]

    seen_values = {}

    for index, value in enumerate(nums):
        print(seen_values)
        if target - value in seen_values:
            print(target - value)
            print(index)
            # print(seen_values[target - value], index)
            # print(seen_values)
            return seen_values[target - value], index

        else:
            seen_values[value] = index

    return -1

print(twoSum(nums=[3, 2, 3, 4], target=7))
