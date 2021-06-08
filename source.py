# Q.13
import collections
import gensim

f = open("pmspeech.txt", "r")  # to open a file
c = f.read()  # to read a file

c = c.split()  # to split string
all_stopwords = gensim.parsing.preprocessing.STOPWORDS  # assigning stop words in a veriabl

fil_word = [word for word in c if not word in all_stopwords]  # list without stop words

un_word = set(fil_word)

d = {i: fil_word.count(i) for i in un_word}  # counting words and assigning in dict

emphasized_word = collections.Counter(d).most_common(10)  # getting most 10 emphasized words
for i in range(len(emphasized_word)):
    emphasized_word[i] = list(emphasized_word[i])

emphasized_word.sort(key=lambda x: x[0])
print(emphasized_word)


