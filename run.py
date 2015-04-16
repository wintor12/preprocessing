import tools
import os
from os.path import join

path = 'C:\\Exp\\lda\\nips\\data_words'
# path_removed = "C:\\Exp\\lda\\removed\\"
old_path ='C:\\Exp\\lda\\nips\\data_words_old'

# if not os.path.exists(old_path):
	# os.rename(path, old_path)
# if not os.path.exists(path):
    # os.makedirs(path)

# print os.listdir('C:\\Exp\\lda\\nips\\data_words_old')
# tools.listFiles(old_path)	
# tools.keepEnglishWords(old_path, path)
tolls.removeLen2Words(old_path, path)



# docs = tools.listFiles(path_removed)
# tools.removeDocs(docs, join(path, 'data_words'))
# tools.removeDocs(docs, join(path, 'data_trees'))
# tools.removeDocs(docs, join(path, 'data_edges'))