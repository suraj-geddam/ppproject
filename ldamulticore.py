import gensim
import sys
import time
import logging

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

ot = time.perf_counter()

id2word = gensim.corpora.Dictionary.load_from_text('_wordids.txt')
mm = gensim.corpora.MmCorpus('_tfidf.mm')

print("Corpus is ", mm)

st1 = time.perf_counter()
print("Time taken for input + preprocessing is", st1-ot, "seconds.")
st2 = time.perf_counter()

model = gensim.models.LdaMulticore(corpus=mm, id2word=id2word, chunksize=100, eval_every=1, workers=int(sys.argv[1]))
et = time.perf_counter()
print("Time taken to train model is", et-st2, "seconds.")