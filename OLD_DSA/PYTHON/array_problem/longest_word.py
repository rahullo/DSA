string = 'fun!@#$# times'

def naive_longest_word(string):
    count = 0
    maximum = 0
    words = []
    word = []
    for char in string:
        if char.isalnum:
            word.append(char)
            count+=1
        else:
            if word not in words and word:
                words.append(''.join(word))
                print("else", words)
                print("else", word)
                word = []
        
            maximum = max(count, maximum)
            word = []

    maximum = max(count, maximum)
    if word not in words and word:
        words.append(''.join(word))
        print("second", words)
        print("second", word)

    for item in words:
        if len(item) == maximum:
            return item

# print('hello')
print(naive_longest_word(string))