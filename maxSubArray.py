# https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [5, 4, -1, 7, 8]
# nums = [-2, 1]
# nums = [-2, 2, -3]

current_sum = nums[0]
max_sum = nums[0]

for i in range(1, len(nums)):
    print(nums[i], current_sum)

    current_sum = max(nums[i], current_sum + nums[i])
    print(current_sum)
    max_sum = max(max_sum, current_sum)

    print(max_sum)

# print(max_sum)


# largSumArr = []
# signalIndx = []
# # for i, num in enumerate(nums):
# #     if len(nums) == 1:
# #         print(nums[0])
# #     elif i+1 < len(nums):
# #         print(num)
# #         if num + nums[i+1] > 0 and num > 0:
# #             print(num)
# #             signalIndx.append(i)
# for i, num in enumerate(nums):
#     print(i)
#     if len(nums) == 1:
#         print(nums[0])
        
#     elif i+ 1 < len(nums) and num + nums[i+1] >= 0 and num >= 0:
#         print(num)
#         signalIndx.append(i)

# print(signalIndx)
# start, end = signalIndx[0], signalIndx[-1]+2
# # print(start, end)
# # print(nums[start: end])
# nums = nums[start: end]
# print(sum(nums))