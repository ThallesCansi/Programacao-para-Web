import nltk

string = input('Write a sentence: ')

words = nltk.word_tokenize(string)
articles = ['a', 'as', 'o', 'os', 'uma', 'umas', 'um', 'uns']

for i in words:
    for j in articles:
        if (i == j):
            words.remove(j)

print(' '.join(words))