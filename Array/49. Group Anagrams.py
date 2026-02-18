import collections

def groupAnagrams(strs):
    dict = collections.defaultdict(list)

    for str in strs:
        key = ''.join(sorted(str))

        dict[key].append(str)
    return dict.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])