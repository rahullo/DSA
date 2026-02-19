def threeSum(nums):
    nums.sort()
    ans = set()

    for  i in range(len(nums) - 2):
        firtNum = nums[i]
        j = i+1
        k = len(nums) - 1

        while j < k:
            secondNum = nums[j]
            thirdNum = nums[k]

            sum = firtNum + secondNum + thirdNum

            if sum > 0:
                j+=1
            elif sum < 0:
                k-=1
            else:
                ans.add((firtNum, secondNum, thirdNum))
                j += 1
                k -= 1
    return list(ans)

print(threeSum([-1,0,1,2,-1,-4]))