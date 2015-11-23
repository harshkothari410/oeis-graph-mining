import requests
import json
import sys

# class NoIndent(object):
#     def __init__(self, value):
#         self.value = value

# def default(o, encoder=json.JSONEncoder()):
#     if isinstance(o, NoIndent):
#         return json.dumps(o.value)
#     return encoder.default(o)


g = open('catalans.txt')
h = open('sequence.txt','w')
f = open('graph3.txt','r')

def create_graph():
	graph = {}
	lines = f.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		# graph[l[0]] = set(l[1:])
		graph[l[0]] = set(l[1:])
		# if count == 9:
		# 	return graph

		# count = count  + 1
	return graph

def get_series(seq_id):
	# print seq_id
	url = 'https://oeis.org/A'+ seq_id +'/list'
	s = requests.get(url).text

	start = s.find('<pre>')
	end = s.find('</pre>')

	seq = s[start + 6: end-1]
	
	# Here if I use as string
	# seq = seq.replace('\n',' ')
	# seq = seq.replace('\\','')
	seq = map(int,seq.split(','))

	return seq[:20]

# data = {}
# data['1'] = get_series('A000040')

graph = create_graph()

lines = g.read().splitlines()

data= {}
count = 1
length = 0
temp = {}
unwanted = []

for seq in lines[1:]:
	seq = seq.split(' ')[0]

	if count == 50:
		break
	for x in graph[seq]:
		if x in data.keys():
			continue
		else:
			print str(count) + ' ' + x
			count = count + 1
			
			try:
				data[x] = get_series(x)
			except KeyboardInterrupt:
				json = json.dumps(data, sort_keys = True)
				h.write(json)
				sys.exit()
			except:
				unwanted.append(x)
			# temp[x] = data[x]
			# json = json.dumps(temp)
			# h.write(temp)
			# h.write('\n')

	length = length + len(graph[seq])
# with open('sequence.json', 'a') as outfile:

print unwanted
json = json.dumps(data, sort_keys = True)
h.write(json)
# print length
# print length + 213 