def maxProfit(nums):
    minimum = nums[0]
    profit = 0
    for i in range(len(nums)):
        minimum = min(minimum, nums[i])
        currentProfit = nums[i] - minimum
        profit = max(profit, currentProfit)

    return profit

print(maxProfit([7,1,5,3,6,4]))