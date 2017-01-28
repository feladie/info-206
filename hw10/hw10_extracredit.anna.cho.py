###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/


from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep

import re

WORD_RE = re.compile(r"[\w']+")

class UserSimilarity(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	def mapper1_extract_user_business(self,_,record):
		"""Taken a record, yield <user_id, word>"""
		for word in WORD_RE.findall(record['text']):
			yield [record['user_id'], word.lower()]

	def reducer1_compile_businesses_under_user(self,user_id,word):
		###
		unique_words = set(word)
		yield [ user_id, list(unique_words) ]
		##/

	def mapper2_collect_businesses_under_user(self, user_id, unique_words):
		###
		yield [ "LIST", [user_id, unique_words] ]
		##/

	def reducer2_calculate_similarity(self,stat,user_words):
		def Jaccard_similarity(list1, list2):
			###
			# Source: http://stackoverflow.com/questions/2151517/pythonic-way-to-create-union-of-all-values-contained-in-multiple-lists
			both_lists = [list1, list2]
			union = set().union(*both_lists)
			# Source: http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
			intersection = list(set(list1) & set(list2))
			return len(intersection) / len(union)
			##/

		###
		pair_list = []
		for pair in user_words:
			pair_list.append(pair)

		for i in range(len(pair_list) - 1):
			for j in range(i + 1, len(pair_list)):
				similarity = Jaccard_similarity(pair_list[i][1], pair_list[j][1])
				if similarity >= 0.5:
					yield [ [pair_list[i][0], pair_list[j][0]], similarity ]
		##/


	def steps(self):
		return [
		    MRStep(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
		    MRStep(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)
		]


if __name__ == '__main__':
	UserSimilarity.run()
