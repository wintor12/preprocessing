import os
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

path = 'C:\\Exp\\lda\\20news_test7\\data_sentences'
save_path = 'C:\\Exp\\lda\\20news_test7\\word2vec_model'

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname
	def __iter__(self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname, fname)):
				yield line.split()
				
sentences = MySentences(path)
model = gensim.models.Word2Vec(sentences, min_count = 2)
model.save(save_path)