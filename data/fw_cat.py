import json
import networkx as nx

f=open('catalans.txt','r')
i=f.readlines()
f1=open('newgraph_dd50.json','r')

sd=json.loads(f1.read())
data={}
k=0


print i
for x in i[1:]:
	#for y in range(0,len(s1)-1):
	#	if x == s1[y][0]:
	#		temp.append(s1[y][:])
	#		k=k+1
	# print x
	k,faltu = x.split()
	data[k]=sd[k]
	
	#if count == 50:
	#	break

fname = 'newcatalans.json'
f = open(fname, 'w')
data = json.dumps(data, indent=4)
f.write(data)
f.close()

h=open("newcatalans.json", 'r')
jd=json.loads(h.read())
G = nx.Graph(jd)

length = nx.floyd_warshall(G, weight='weight')

# print length

bname = 'fw_on_catalans.json'
b = open(bname, 'w')
data = json.dumps(length, indent=4)
b.write(data)
b.close()

