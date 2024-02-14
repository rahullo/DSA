# def longestConsecutive(nums):
#     ans = 0
#     seen = set(nums)

#     for num in nums:
#         if num - 1 in seen:
#             continue
#         length = 0
#         while num in seen:
#             num += 1
#             length += 1
#         ans = max(ans, length)

#     return ans

# print(longestConsecutive([1, 2, 3, 4]))



# x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
# y = x[0:6]                     # Statement 2
# z = x                          # Statement 3
# w = y                          # Statement 4
# x[1] = x[1][0:3] + 'd'         # Statement 5
# y[2] = 4                       # Statement 6
# z[1][1:3] = 'yzw'              # Statement 7
# z[0] = 0                       # Statement 8
# w[4][0] = 1000                 # Statement 9
# a = (x[4][1] == 4) 


# x = [423,'b',37,'f']
# u = x[1:]
# y = u
# w = x
# u = u[0:]
# u[1] = 53
# x[2] = 47

# print(x[2], y[1], w[2], u[1])

# first = "tarantula"
# second = ""
# for i in range(len(first)-1,-1,-1):
#   second = first[i] + second

# print(second)

# def mystery(l):
#   l = l[0:5]
#   print(l)
#   return()

# list1 = [44,71,12,8,23,17,16]
# mystery(list1)

# print(list1)

# def f(x):
#   d=0
#   while x > 1:
#     (x,d) = (x/2,d+1)
#   return(d)

# print(f(27182818))

# def h(n):
#     s = 0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+i
#     return(s)

# print(h(60))
# print(h(45))
# print(h(60)-h(45))

# def g(m,n):
#     res = 0
#     while m >= n:
#         (res,m) = (res+1,m/n)
#     return(res)

# print(g(375, 4))

# def mys(m):
#     if m == 1:
#         return(1)
#     else:
#         return(m*mys(m-1))
    
# print(mys())

# def threesquares(m):

#   if m <= 0:
#     return False

#   for a in range(int(m**0.5) + 1):
#     for b in range(int(m**0.5) + 1):
#       for c in range(int(m**0.5) + 1):
#         if a**2 + b**2 + c**2 == m:
#           return True

#   return False



# def repfree(s):
#   seen = set()

#   for char in s:
#     if char in seen:
#       return False
#     seen.add(char)

#   return True


# def hillvalley(l):
#     if len(l) < 3:
#         return False

#     is_hill = False
#     for i in range(1, len(l) - 1):
#         if l[i - 1] < l[i] > l[i + 1]:
#             is_hill = True
#             break

#     is_valley = False
#     for i in range(1, len(l) - 1):
#         if l[i - 1] > l[i] < l[i + 1]:
#             is_valley = True
#             break

#     return is_hill or is_valley


# # Test cases
# print("True", threesquares(6))  # True
# print("False ", threesquares(188))  # False
# print("True", threesquares(1000))  # True
# print("True", threesquares(6)) #True
# print("False", threesquares(143)) #False
# print("True", threesquares(1024)) #True
# print('\n')


# print("True", repfree("qwerty!@#2")) #True
# print("False", repfree("(x+6)(y-5)")) #False
# print("True", repfree("94templars")) #True
# print("False", repfree("siruseri")) #False
# print('\n')


# print("True", hillvalley([1,2,3,5,4,3,2,1])) #True
# print("False",hillvalley([1, 2, 3, 4, 5, 3, 2, 4, 5, 3, 2, 1])) # False
# print("True", hillvalley([9,5,4,-1,-2,3,7])) #True
# print("False", hillvalley([5,4,3,2,1,0,-1,-2,-3])) #False


# def remdup(l):
  
#   seen = set()
#   unique_elements = []
#   for num in l:
#     if num not in seen:
#       seen.add(num)
#       unique_elements.append(num)
#   return unique_elements

# Example usage
# print(remdup([3,1,3,5]))
# [3, 1, 5]

# print(remdup([7,3,-1,-5]))
# [7, 3, -1, -5]

# print(remdup([3,5,7,5,3,7,10]))
# [3, 5, 7, 10]

# l = [1, 2, 2, 3, 4, 1, 5]
# unique_list = remdup(l)
# print(unique_list)  # Output: [1, 2, 3, 4, 5]



# def sumsquare(l):
#     odd_sum = 0
#     even_sum = 0

#     for num in l:
#         if num % 2 == 0:  # even number
#             even_sum += num ** 2
#         else:  # odd number
#             odd_sum += num ** 2

#     return [odd_sum, even_sum]

# Example usage:
# l = [1, 2, 3, 4, 5]
# print(sumsquare(l))  # Output: [35, 20]


# print(sumsquare([1,3,5]))
# # [35, 0]

# print(sumsquare([2,4,6]))
# # [0, 56]

# print(sumsquare([-1,-2,3,7]))
# [59, 4]


# def transpose(m):
#   transposed_matrix = []

#   for col in range(len(m[0])):
#     new_row = []

#     for row in range(len(m)):
#       new_row.append(m[row][col])

#     transposed_matrix.append(new_row)

#   return transposed_matrix


# print(transpose([[1,2,3],[4,5,6]]))
# # [[1, 4], [2, 5], [3, 6]]

# print(transpose([[1],[2],[3]]))
# # [[1, 2, 3]]

# print(transpose([[3]]))
# # [[3]]


# def mystery(l,v):
#   if len(l) == 0:
#     return (v)
#   else:
#     return (mystery(l[:-1],l[-1]+v))
  
# print(mystery([22,14,19,65,82,55],1))

# triples = [ (x,y,z) for x in range(2,4) for y in range(2,5) for z in range(5,7) if 2*x*y > 3*z ]

# print(triples)

# runs = {
#     "Test":{
#         "Rahul":[90,14,35],
#         "Kohli":[3,103,73,42],
#         "Pujara":[53,15,133,8]
#         },
#     "ODI":{
#         "Sharma":[37,99],
#         "Kohli":[63,47]
#         }
# }


# print(runs)

# # runs["ODI"]["Rahul"].append([74])
# # runs["ODI"]["Rahul"].extend([74])
# # runs["ODI"]["Rahul"][0]=74
# runs["ODI"]["Rahul"]=[74]
# print(runs)


# inventory = {}

# inventory["Amul"] = ["Mystic Mocha",55]
# inventory["Amul, Mystic Mocha"] = 55
# inventory[["Amul","Mystic Mocha"]] = 55
# inventory[("Amul","Mystic Mocha")] = 55