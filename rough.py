d = 10
p = 0
t = 0
text = 'RAHULLOHRA'
pattern = 'HRA'
q = 13


for i in range(3):
        p = (d*p + ord(pattern[i])) % q
        # print(ord(pattern[i]), p)
        # print(ord(text[i]))
        t = (d*t + ord(text[i])) % q
        # print('\n')

# print(p, t)
# print(ord('1'))

class RabinKarp:

    d = 10

    def search(self, pattern, text, q):
        lenPatt = len(pattern)
        lenText = len(text)
        p = 0
        t = 0
        h = 1
        i = 0
        j = 0

        for i in range(lenPatt-1):
            h = (h*d) % q
        print("h->",h)

        # Calculate hash value for pattern and text
        for i in range(lenPatt):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q
        print(p, t)
        # Find the match
        for i in range(lenText-lenPatt+1):
            if p == t:
                for j in range(lenPatt):
                    if text[i+j] != pattern[j]:
                        break

                j += 1
                if j == lenPatt:
                    print("Pattern is found at position: " + str(i+1))

            if i < lenText-lenPatt:
                t = (d*(t-ord(text[i])*h) + ord(text[i+lenPatt])) % q

                if t < 0:
                    t = t+q

rabin = RabinKarp()

text = "ABCCDDAEFGDHAODSHFDGFDSFJHASDFIUOAHWHFDSKJBVDSHVGAISHSOFJSADFJDSJKHBVDSVJNAOISDUHGDSHGAJLALDSFJHDS"
pattern = "JBVDSHVGA"
q = 13
# print(rabin.search(pattern, text, q))

mat1 = [[2, 4, 6],[3,5,7],[4,6,8]]
mat2 = [[1,2,3], [3,1,5], [4,5,6]]

def addingTwoMatrixes(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    ans = [[] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            ans[i].append(mat1[i][j] + mat2[i][j])

    return ans

# print(addingTwoMatrixes(mat1, mat2))


# provide the matrix in sequence
def subtractingTwoMatrixes(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    ans = [[] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            ans[i].append(mat1[i][j] - mat2[i][j])

    return ans


def multiplyMmatrices(mat1, mat2):

    if len(mat1[0]) != len(mat2):
        raise ValueError("The two matrices can't be multiplied!!")

    ans = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            product = 0
            for k in range(len(mat1[0])):
                product += mat1[i][k] * mat2[k][j]
            row.append(product)
        ans.append(row)
    return ans

# print(multiply_matrices(mat1, mat2))
def halfPiramid1(rows):
    for i in range(1, rows+1):
        print(i*"*")

# halfPiramid1(5)

def invertedHalfPir(rows):
    for i in range(rows, 0, -1):
        print(i * "*")

    
# invertedHalfPir(5)

def print_full_pyramid(height):
  """Prints a full pyramid of stars.

  Args:
    height: The height of the pyramid.
  """
  for i in range(height):
    for j in range(height - i):
      print(" ", end="")
    for j in range(i + 1):
      print("*", end=" ")
    print()

# print_full_pyramid(5)


# Prefix Sum
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

# print(fn([1,2,3,4,5]))

# arr is a list of characters
def fnString(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)

# print(fnString(["rahullohra"]))

def intToRoman(num):
    valueSymbols = [(1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')]
    ans = []

    for value, symbol in valueSymbols:
        if num == 0:
            break

        count, num = divmod(num, value)
        print(count, num)
        ans.append(symbol * count)

    return ''.join(ans)


# print(intToRoman(45))

def romanToInt(s):
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    for a, b in zip(s, s[1:]):
      if roman[a] < roman[b]:
        ans -= roman[a]
      else:
        ans += roman[a]

    return ans + roman[s[-1]]

# print(romanToInt('MCMXCIV'))

def letterCombinations1(digits):
    letters= {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    pairs = []
    for i in range(len(digits)):
        pairs.append(letters[digits[i]])

    ans = []

    for i in range(len(pairs)):
        print()

    return pairs


def letterCombinations(digits):
    if not digits:
        return []

    ans = ['']
    digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for d in digits:
        temp = []
        for s in ans:
            for c in digitToLetters[ord(d) - ord('0')]:
                temp.append(s + c)
        ans = temp

    return ans

print(letterCombinations("23"))
print(ord('2')- ord('0'))