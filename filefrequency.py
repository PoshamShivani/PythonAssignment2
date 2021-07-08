from collections import Counter


def word_frequency(filename):
        with open(filename) as f:
                return Counter(f.read().split())


print(word_frequency("Word.txt"))
