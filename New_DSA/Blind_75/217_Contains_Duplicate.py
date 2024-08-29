def containsDuplicate_2(nums):
    nums_set = set(nums)
    return len(nums) != len(nums_set)


def containsDuplicate_1(nums):
    hash_Table = {}
    for num in nums:
        if num not in hash_Table:
            hash_Table[num] = True
        else:
            return True
    return False

def containsDuplicate(nums):
    hashmap = set()

    for num in nums:
        if num in hashmap:
            return True
        hashmap.add(num)
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))



# hash_Table[3] = "Rahul"
# print(not hash_Table[1])