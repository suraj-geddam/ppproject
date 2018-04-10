import gensim
import sys
import time

sentences = []
ot = time.perf_counter()
corpus = open('final.txt', 'r', encoding='utf8', errors='ignore').read().replace('\n', ' ').replace('!', '.').replace('?', '.').split('.')

for line in corpus:
    initsen = line.split()
    finalsen = [string for string in initsen if string.isalpha()]
    sentences.append(finalsen)

sentences = [s for s in sentences if s]

st1 = time.perf_counter()
print("Time taken for input + preprocessing is", st1-ot, "seconds.")
st2 = time.perf_counter()

model = gensim.models.Word2Vec(sentences, workers = sys.argv[1])
et = time.perf_counter()
print("Time taken to train model is", et-st2, "seconds.")