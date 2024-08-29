from collections import Counter


def topKFrequent( nums, k):
    counter = Counter(nums)
    ans = []
    for i in range(k):
        ans.append(counter)

print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([1], 1))