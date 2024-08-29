def twoSum( nums, target):
    hashMap = {}
    for i in range(len(nums)):
        toFind = target - nums[i]
        # print(nums[i], toFind, hashMap)

        if toFind in hashMap:
            # print('Entered')
            return [i, hashMap.get(toFind)]
        else:
            hashMap[nums[i]] = i
    return False


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([2, 4, 3, 11, 12], 23))
print(twoSum([3, 0, 3], 3))
