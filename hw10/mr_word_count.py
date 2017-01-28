from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep

import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFrequencyCount(MRJob):
	INPUT_PROTOCOL = JSONValueProtocol

	# def mapper(self, _, line):
	#     yield "chars", len(line)
	#     yield "words", len(line.split())
	#     yield "lines", 1

	# def reducer(self, key, values):
	#     yield key, sum(values)

	def mapper(self, _, record):
			for word in WORD_RE.findall(record['text']):
				yield [ word.lower() , record['review_id']]

	# def reducer1_count_reviews(self, word, review_ids):
	# 	yield [word, sum(review_ids)]

if __name__ == '__main__':
	MRWordFrequencyCount.run()