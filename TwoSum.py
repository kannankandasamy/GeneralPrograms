###
Given an array of integers, return indices of the two numbers such that they add up to a specific target number.

Example:
Given nums = [5, 3, 2, 12, 7, 11], target = 10,

Because nums[0] + nums[1] = 3 + 7 = 10,
return [1, 4].
###
def twoSum(nums, target):
    dic,lis = {},[]
    for i,n in enumerate(nums):
        if target - n in dic:
            lis.append(dic[target-n])
            lis.append(i)
        else:
            dic[n]=i
    return lis
