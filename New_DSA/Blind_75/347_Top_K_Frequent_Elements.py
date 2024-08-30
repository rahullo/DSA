def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    print(freq)

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    print(count)

    for n, c in count.items():
        freq[c].append(n)

    print(freq)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # O(n)

print(topKFrequent([5, 5, 4, 5, 4, 8], 2))
# print(topKFrequent([1], 1))