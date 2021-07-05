from collections import Counter
def word_Frequency(filename):
        with open(filename) as f:
                return Counter(f.read().split())

print(word_Frequency("Word.txt"))