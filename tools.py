from os import listdir
from os.path import isfile, join
import enchant
from nltk.stem.lancaster import LancasterStemmer

def listFiles(path):
	return [ f for f in listdir(path) if isfile(join(path,f)) and not f.startswith('.')]

def checkWord(word):
	d = enchant.Dict("en_US")
	st = LancasterStemmer()
	return d.check(word) or d.check(word.capitalize()) or d.check(st.stem(word))

def keepEnglishWords(path, output):
	word_dict = []
	filenames = listFiles(path)
	for name in filenames:
		print '=====processing: ' + name + '======='
		filepath = join(path, name)
		p = open(filepath, 'r')
		content = p.read()
		p.close()
		words = content.strip().split(' ')
		res = []
		for word in words:
			if word in word_dict:
				res.append(word)
			else:
				if checkWord(word):
					word_dict.append(word)
					res.append(word)
				else:
					print word + ', false'
		res = ' '.join(res)
		p = open(join(output, name), 'w')
		p.write(res)
		p.close()


path = '/Users/tongwang/Desktop/exp/lda/20news_test/data_words'
output = '/Users/tongwang/Desktop/exp/lda/20news_test/data_words_clean'
keepEnglishWords(path, output)
# print checkWord('Germany')
