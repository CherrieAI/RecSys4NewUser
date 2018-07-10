import jieba.analyse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


# sort keywords by weights
def jieba_keywords(sentence):
	kw_dict = {}
	tmp = jieba.analyse.extract_tags(sentence, withWeight=True)
	kw_dict = {key: value for key, value in tmp}
	return sorted(kw_dict.items(), key=lambda x: x[1], reverse=True)


# list of invalid words
def list_invalid_words():
	invalid_words_path = "./invalid_words.txt"
	txt_path = "/Users/hebeiqianrui/Documents/Python/A_data/day02/exercise-第2天.txt"
	file_in = open(txt_path, 'r')
	content = file_in.read()

	try:
		jieba.analyse.set_stop_words(invalid_words_path)
		tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
		for v, n in tags:
			print(v + '\t' + str(int(n * 10000)))

	finally:
		file_in.close()


def remove_invalid_words(txt, invalid_words='./invalid_words.txt'):
	invalid_words = pd.read_table(invalid_words, index_col=False, sep='\n', quoting=3, names=['InvalidWord'],
	                              encoding='utf-8')

	invalid_word_list = invalid_words.InvalidWord.values.tolist()
	txt_clean = []
	word_count = []
	for line in txt:
		line_clean = []
		for word in line:
			if word in invalid_word_list:
				continue
			line_clean.append(word)
			word_count.append(str(word))
		txt_clean.append(line_clean)
	return txt_clean, word_count
