import sys; import os
sys.path.insert(0, os.path.abspath('..'))

import math
import json
from collections import Counter
from graph import *

f = open('../data/data_referenceTitle_WordCounts.txt','r')
g = open('../data/data_comment_words.txt','r')

waste = {}
waste_seq = []
def get_comment_data(file1):
	comment_data = {}
	lines = file1.read().splitlines()
	# print len(lines)
	count = 0
	for line in lines:
		l = line.split(' ')
		# for x in range(2, len(l), 2):
		# 	reference_data[l[x]] = l[x+1]
		comment_data[l[0]] = l[2:]
		# print comment_data
	file1.close()

	return comment_data

def get_reference_data(file1):
	reference_data = {}
	lines = file1.read().splitlines()
	count = 0
	for line in lines:
		l = line.split(' ')
		# for x in range(2, len(l), 2):
		# 	reference_data[l[x]] = l[x+1]
		reference_data[l[0]] = l[2:]
	file1.close()
	return reference_data

def get_doc_dict(data ,seq):
	reference_dict = {}
	for x in range(0, len(data), 2):
		reference_dict[data[x]] = data[x+1]
	return reference_dict

def update_dict( dict1, dict2 ):
	for k, v in dict2.items():
		if k in dict1.keys():
			dict1[k] = str(int(dict1[k]) + int(v))
		else:
			dict1[k] = v
	return dict1


def find_doc_dis(reference_dict, comment_dict, seq1, seq2):
	seq1_dict_r = get_doc_dict(reference_dict[seq1], seq1)
	seq2_dict_r = get_doc_dict(reference_dict[seq2], seq2)

	seq1_dict_c = get_doc_dict(comment_dict[seq1], seq1)
	seq2_dict_c = get_doc_dict(comment_dict[seq1], seq1)

	# seq1_dict = seq1_dict_c.copy()
	# seq1_dict.update(seq1_dict_r)

	# seq2_dict = seq2_dict_c.copy()
	# seq2_dict.update(seq2_dict_r)

	seq1_dict = update_dict(seq1_dict_c, seq1_dict_r)
	seq2_dict = update_dict(seq2_dict_c, seq2_dict_r)
	# print seq1_dict
	distance = 0

	l1 = 0
	l2 = 0
	product = 0

	# print seq1_dict_r
	# print seq1_dict_c

	# print seq1_dict
	for k,v in seq2_dict.items():
		if k in seq1_dict.keys():
			# print k
			product = product + ( int(seq1_dict[k]) * int(seq2_dict[k]) )
			l1 = l1 + ( int(seq1_dict[k]) * int(seq1_dict[k]) )
			l2 = l2 + ( int(seq2_dict[k]) * int(seq2_dict[k]) )

			print product, l1, l2


	l1 = math.sqrt(l1)
	l2 = math.sqrt(l2)

	print seq1, seq2,product, l1*l2

	if product == 0:
		distance = math.acos(0)
	else:
		# if float(product / math.round(( l1 * l2 ))) == 1.0:
			# distance = math.acos(1)
		# else:
		distance = math.acos( float(product / round(( l1 * l2 ),2)) )

		# distance = math.acos(1)
		# waste[seq1] = seq2
	return (int(distance*1000) + 50)

# def new_graph( graph, reference_data, comment_data ):
	newgraph = {}
	count = 0
	for k, v in graph.items():
		# print k, v
		seq1 = k
		temp = {}
		
		try:
			if v[0] == '0' or v[0] == 0:
				newgraph[k] = {}
			else:
				for seq2 in v[1:]:
					weight = find_doc_dis(reference_data, comment_data, seq1, seq2)
					temp[seq2] = weight
					# print temp
				newgraph[k] = temp
				# print count
				count = count + 1
				# if count == 10:
				# 	return newgraph
		except:
			newgraph[k] = {}
			waste_seq.append(seq2)
			# if count == 2:
			# 	return newgraph
	return newgraph

# def write_json( graph ):
	newgraph = open('../data/newgraph_dd50.json', 'w')
	json1 = json.dumps(graph, sort_keys=True, indent=4)
	newgraph.write(json1)
	newgraph.close()

graph = graph.create_graph('../data/graph3.txt')


# test = open('testgraph.json','w')
# j = json.dumps(graph, indent=4, sort_keys=True)
# test.write(j)
# test.close()
reference_data = get_reference_data(f)
comment_data = get_comment_data(g)
seq1 = graph['1']

print find_doc_dis(reference_data, comment_data, '252666','252666')

# newgraph = new_graph( graph, reference_data, comment_data )

# write_json( newgraph )

# print waste
# print waste_seq
# w = open('wasted.json','w')
# j = json.dumps(waste, indent=4)
# w.write(j)
# w.close()
# print reference_data['1']
# print comment_data['1']

# [’100492’, ’108’, ’984’, ’8459’]
# [’100492’, ’94638’, ’984’, ’8459’]
