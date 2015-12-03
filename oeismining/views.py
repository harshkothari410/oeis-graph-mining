from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.dispatch import receiver
from django.db import models
from django.db.models import F, Q
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
	file_path = os.path.join(module_dir, 'graph3.txt')
	
	f = open(file_path)
	
	file_path = os.path.join(module_dir, 'tags.json')

	g = open(file_path)

	tags = json.loads( g.read() )
	graph = create_graph(f)
	path = bfs_paths(graph, seq1, seq2)
	data = convert_json(path, tags)
	jsondata = json.dumps(data)
	return HttpResponse(jsondata, content_type='application/json')

def index( request ):
	# tweets = len(Tweet.objects.all())
	# data = convert_json([2,4,6,9])
	return render(request, 'index.html', locals() )