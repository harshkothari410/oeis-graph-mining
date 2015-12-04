from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.dispatch import receiver
from django.db import models
from django.db.models import F, Q
import networkx as graphs
from django.core.files.storage import default_storage as storage
import json
import os

def bfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop(0)
		# print path
		if path[-1] == '0':
			continue
		for next in graph[vertex] - set(path):
			if next == goal:
				return path + [next]
				# print count

				# if count  > 10:
				# 	sys.exit()
				print path + [next]
				# yield path + [next]
				# return path + [next]
			else:
				stack.append((next, path + [next]))
	return start

def convert_all_json( nodes, tags ):
	'''
		46', u'11', u'13', u'10', u'178323', u'178325', u'214403', u'131338', u'121690', u'157133', u'157134', u'107595', u'107590', u'155804', u'155806', u'192036', u'125281', u'230323', u'230321', u'230317', '230318
	'''
	l = ['46', u'11', u'13', u'10', u'178323', u'178325', u'214403', u'131338', u'121690', u'157133', u'157134', u'107595', u'107590', u'155804', u'155806', u'192036', u'125281', u'230323', u'230321', u'230317', '230318']

	data = {"nodes": [], "links":[]}

	prev = nodes[0]
	

	count = 0
	for x in l:
		
		try:
			tag = tags[x]

			name = x + str(tag)

		except:
			name = x


		temp = {"name": name, "group":6}
		data["nodes"].append(temp)


		# if count != 1:
		temp = {"source" : count, "target": count+1, "value":1, "weight":1}
		data["links"].append(temp)
		# prev = x
		count = count + 1
	data["links"].pop()

	for node in nodes:
		for x in node:
			print node
			try:
				tag = tags[x]

				name = x + str(tag)

			except:
				name = x


			if x in l:
				temp = {"name": name, "group":6}
			else:
				temp = {"name": name, "group":1}
			data["nodes"].append(temp)


			# if count != 1:
			temp = {"source" : count, "target": count+1, "value":1, "weight":1}
			data["links"].append(temp)
			# prev = x
			count = count + 1
		data["links"].pop()
	return data
	

def tab2search( request ):
	seq1 = request.GET['seq1']
	module_dir = os.path.dirname(__file__)
	print module_dir
	# file_path = os.path.join(module_dir, 'graph3.txt')
	
	# f = open(file_path)
	l = ['46', u'11', u'13', u'10', u'178323', u'178325', u'214403', u'131338', u'121690', u'157133', u'157134', u'107595', u'107590', u'155804', u'155806', u'192036', u'125281', u'230323', u'230321', u'230317', '230318']
	file_path = os.path.join(module_dir, 'tags.json')

	g = open(file_path)

	
	file_path = os.path.join(module_dir, 'newgraph_dd50.json')
	fh=open(file_path, 'r')
	tags = json.loads( g.read() )
	# graph = create_graph(f)
	sd=json.loads(fh.read())
	G = graphs.Graph(sd)

	s = []
	# try:
	for x in l:
		path = graphs.shortest_path(G, seq1, x)
	# path1 = graphs.dijkstra_path(G, seq1, seq2, weight='weight')
		# data = convert_json(path, tags)
	# data1 = convert_json(path1, tags)
		s.append(path)

	data = convert_all_json(s, tags)
		# data = [data, data1]
	
	# print data
	# except:
		# data = {'error': 'No Path Between these two Nodes'}
	jsondata = json.dumps(data)
	return HttpResponse(jsondata, content_type='application/json')


def page2( request ):
	# tweets = len(Tweet.objects.all())
	# data = convert_json([2,4,6,9])
	return render(request, 'tab2.html', locals() )


def convert_json(nodes, tags):
	'''
	"nodes":[
    {"name":"Myriel","group":1},
    {"name":"Napoleon","group":1},
    {"name":"Mlle.Baptistine","group":1},
    {"name":"Mme.Magloire","group":1},
    {"name":"CountessdeLo","group":1},
    ],

    "links":[
    {"source":1,"target":2,"value":1},
    {"source":2,"target":3,"value":8},
    {"source":3,"target":4,"value":1},
    // {"source":4,"target":2,"value":1},
    ]};
	'''
	data = {"nodes": [], "links":[]}

	prev = nodes[0]
	

	count = 0
	for x in nodes:
		
		try:
			tag = tags[x]

			name = x + str(tag)

		except:
			name = x


		temp = {"name": name, "group":1}
		data["nodes"].append(temp)


		# if count != 1:
		temp = {"source" : count, "target": count+1, "value":1, "weight":1}
		data["links"].append(temp)
		# prev = x
		count = count + 1
	data["links"].pop()

	# temp = {"source" : 1, "target": 3, "value":1}
	# data["links"].append(temp)
	return data



def create_graph(f):
	graph = {}
	lines = f.read().splitlines()

	count = 0
	for line in lines:
		l = line.split(' ')
		# graph[l[0]] = set(l[1:])
		graph[l[0]] = set(l[2:])
		# if count == 9:
		# 	return graph

		# count = count  + 1
	return graph

def search( request ):
	# print dir(request)
	# print request.__dict__
	seq1 = request.GET['seq1']
	seq2 = request.GET['seq2']

	# import os
	module_dir = os.path.dirname(__file__)
	print module_dir
	# file_path = os.path.join(module_dir, 'graph3.txt')
	
	# f = open(file_path)
	
	file_path = os.path.join(module_dir, 'tags.json')

	g = open(file_path)

	file_path = os.path.join(module_dir, 'newgraph_dd50.json')
	fh=open(file_path, 'r')
	tags = json.loads( g.read() )
	# graph = create_graph(f)
	sd=json.loads(fh.read())
	G = graphs.Graph(sd)

	try:
		path = graphs.shortest_path(G, seq1, seq2)
		path1 = graphs.dijkstra_path(G, seq1, seq2, weight='weight')
		data = convert_json(path, tags)
		data1 = convert_json(path1, tags)


		data = [data, data1]
	
	except:
		data = {'error': 'No Path Between these two Nodes'}
	jsondata = json.dumps(data)
	return HttpResponse(jsondata, content_type='application/json')



def index( request ):
	# tweets = len(Tweet.objects.all())
	# data = convert_json([2,4,6,9])
	return render(request, 'index.html', locals() )

def centroids( request ):
	return render(request, 'centroids.html', locals() )

def apsp( request ):
	return render(request, 'apsp.html', locals() )

def sssp( request ):
	return render(request, 'sssp.html', locals() )