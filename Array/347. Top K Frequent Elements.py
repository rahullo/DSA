from collections import Counter

def topKFrequent(nums, k):
    dict = Counter(nums)
    for key, value in dict.items():
        print(key, value)
    return dict


print(topKFrequent([1, 1, 1, 2, 2, 4, 4, 4, 4, 4], 2))