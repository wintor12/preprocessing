import os
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

save_path = 'C:\\Exp\\lda\\20news\\word2vec_model'
voc_path = 'C:\\Exp\\lda\\20news_test10\\idAndWord_50_1000'
matrix_path = 'C:\\Exp\\lda\\20news_test10\\sim_matrix'

if not os.path.exists(matrix_path):
	os.makedirs(matrix_path)

model = gensim.models.Word2Vec.load(save_path)
p = open(voc_path, 'r')
content = p.read().rstrip()
p.close()

id2word = {}
word2id = {}

content = content.split('\n')
for item in content:
	id = item[:item.index(':')]
	word = item[item.index(':') + 1:]
	id2word[id] = word
	word2id[word] = id
	
size = len(id2word)

#sim = np.zeros((size, size))  memory error

for i in xrange(size):
	print i
	sim = np.zeros((1, size))
	word1 = id2word[str(i)]	
	for j in xrange(size):
		word2 = id2word[str(j)]
		sim[0][j] = model.similarity(word1, word2)
	filepath = os.path.join(matrix_path, str(i))
	np.savetxt(filepath,sim)

