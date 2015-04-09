import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

path = ''
save_path = ''

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname
	def __iter__(self):
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname, fname)):
				yield line.split()
				
sentences = MySentences(path)
model = gensim.models.Word2Vec(sentences)
model.save(save_path)