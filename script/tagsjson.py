f = open('../data/1.csv')

lines = f.readlines()
import json
data = {}
for line in lines:
	# print line
	index = line.find(',,')
	line = line[:index]
	line = line.split(',')
	data[line[0]] = line[1:]

print len(list(data.keys()))
g = open('../data/tags.json', 'w')
j = json.dumps(data)
g.write(j) 