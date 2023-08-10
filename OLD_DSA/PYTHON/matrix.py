# mat1 = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
#     ]

# mat2 = [
#     [7, 8, 9], 
#     [4, 5, 6], 
#     [1, 2, 3]
#     ]

# m1 = [
#     [1, 2],
#     [3, 4]
#     ]
# m2 = [
#     [3, 2],
#     [1, 4]
#     ]

# ans = [[0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]]

# m = 2
# n = 2

# def matrixAddition(mat1, mat2):
#     m = len(mat1[0])
#     n = len(mat1)
#     print(m, n)
#     for i in range(m):
#         ans.append([])
#         for j in range(n):
#             ans[i].append(mat1[i][j] + mat2[i][j])
#     return ans

# # print(matrixAddition(mat1, mat2))

# def matrixMultiplication(mat1, mat2):
#     m = len(mat1[0])
#     n = len(mat1)
#     print(m, n)
#     for i in range(len(mat1)):
#         for j in range(len(mat2[0])):
#             for k in range(len(mat2)):
#                 ans[i][j] += mat1[i][k] * mat2[k][j]
#     return ans

# print(matrixMultiplication(m1, m2))

# from rembg import remove
# import math
# print(math.cos(math.pi/4))

def findMinimumCharacters(searchWord, resultWord):
    dic = {}
    for item in resultWord:
        dic[item] = True
    
    ans = []
    for item in searchWord:
        if item not in  dic.keys():
            ans.append(item)

    to = ''.join(ans)
    return to

print(findMinimumCharacters('Rahul', 'Rehil'))