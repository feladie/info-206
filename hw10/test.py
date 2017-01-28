def Jaccard_similarity(business_list1, business_list2):
	###
	# TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
	# Source: http://stackoverflow.com/questions/2151517/pythonic-way-to-create-union-of-all-values-contained-in-multiple-lists
	both_lists = [business_list1, business_list2]
	union = set().union(*both_lists)
	# Source: http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
	intersection = list(set(business_list1) & set(business_list2))
	return len(intersection) / len(union)

print(Jaccard_similarity(['WIcDFpHEnC3ihNmS7-6-ZA'], ['WIcDFpHEnC3ihNmS7-6-ZA']))