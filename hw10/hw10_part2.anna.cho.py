###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/


from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep


class UserSimilarity(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	def mapper1_extract_user_business(self,_,record):
		"""Taken a record, yield <user_id, business_id>"""
		yield [record['user_id'], record['business_id']]

	def reducer1_compile_businesses_under_user(self,user_id,business_ids):
		###
		# TODO_1: compile businesses as a list of array under given user_id,after remove duplicate business, yield <user_id, [business_ids]>
		unique_business_ids = set(business_ids)
		yield [ user_id, list(unique_business_ids) ]
		##/

	def mapper2_collect_businesses_under_user(self, user_id, business_ids):
		###
		# TODO_2: collect all <user_id, business_ids> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [business_ids]]>
		yield [ "LIST", [user_id, business_ids] ]
		##/

	def reducer2_calculate_similarity(self,stat,user_business_ids):
		def Jaccard_similarity(business_list1, business_list2):
			###
			# TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
			# Source: http://stackoverflow.com/questions/2151517/pythonic-way-to-create-union-of-all-values-contained-in-multiple-lists
			both_lists = [business_list1, business_list2]
			union = set().union(*both_lists)
			# Source: http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
			intersection = list(set(business_list1) & set(business_list2))
			return len(intersection) / len(union)
			##/

		###
		# TODO_4: Calulate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
		pair_list = []
		for pair in user_business_ids:
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
