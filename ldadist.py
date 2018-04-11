import gensim
import sys
import time
import logging
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

os.environ["PYRO_SERIALIZERS_ACCEPTED"] = 'pickle'
os.environ["PYRO_SERIALIZER"] = 'pickle'

ot = time.time()

id2word = gensim.corpora.Dictionary.load_from_text('_wordids.txt')
mm = gensim.corpora.MmCorpus('_tfidf.mm')

st1 = time.time()
print "Time taken for input + preprocessing is", st1-ot, "seconds."
st2 = time.time()

model = gensim.models.LdaModel(corpus=mm, id2word=id2word, chunksize=100, distributed=True)
et = time.time()
print "Time taken to train model is", et-st2, "seconds."