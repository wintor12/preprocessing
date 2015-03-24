import os
import shutil
import math

num_training_percentage = 0.7

path = os.getcwd()
files = os.listdir(path)	

path_train = os.path.join(path, 'train')
path_test = os.path.join(path, 'test')
path_data = os.path.join(path, 'data')
if not os.path.exists(path_train):
	os.makedirs(path_train)
if not os.path.exists(path_data):
    os.makedirs(path_data)
if not os.path.exists(path_test):
    os.makedirs(path_test)

categories = [f for f in files if os.path.isdir(os.path.join(path, f)) and f!='train' and f!='data' and f!='test']

for category in categories:	
	src = os.path.join(path, category)
	docs = os.listdir(src)
	num = len(docs)
	num_train = math.floor(num * num_training_percentage)
	num_test = num - num_train
	n = 0
	for doc in docs:
		if not doc.startswith('.') and os.path.isfile(os.path.join(src, doc)):
			shutil.copy(os.path.join(src, doc), path_data)
			n = n + 1
			if n > num_train:
				shutil.copy(os.path.join(src, doc), path_test)
			else:
				shutil.copy(os.path.join(src, doc), path_train)

