import collections

def groupAnagrams_2(strs):
    dict = collections.defaultdict(list)

    for str in strs:
        key = ''.join(sorted(str))
        dict[key].append(str)
    return dict.values()


def groupAnagrams(strs):
    dict = {}

    for str in strs:
        key = ''.join(sorted(str))
        if key in dict:
            dict[key].append(str)
        else:
            dict[key] = [str]
    return dict.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))