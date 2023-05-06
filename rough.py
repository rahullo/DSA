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


a = 144

print(a >> 3)