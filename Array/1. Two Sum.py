def twoSum(nums, target):
    dic = {}

    for i in range(len(nums)):
        if target - nums[i] in dic:
            return (dic[target - nums[i]], i)
        else:
            dic[nums[i]] = i

print(twoSum([2, 7, 10, 11], 21))