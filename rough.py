d = 10
p = 0
t = 0
text = 'RAHULLOHRA'
pattern = 'HRA'
q = 13


for i in range(3):
        p = (d*p + ord(pattern[i])) % q
        print(ord(pattern[i]), p)
        # print(ord(text[i]))
        t = (d*t + ord(text[i])) % q
        print('\n')

print(p, t)
print(ord('H'))