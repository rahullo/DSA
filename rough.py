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
print(rabin.search(pattern, text, q))