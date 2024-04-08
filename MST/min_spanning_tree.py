from graph import Graph
from disjoint import DisjointSet

#Function uses DisjoinSet and Graph classes to sort edges and assemble a MST using Kruskal's algorithm.
def minimum_spanning_tree(graph):
	graph_edges = []
	ds = DisjointSet()
	
	#Retrieving vertices using DisjointSet class method and making list of edges by passing from, to, and weight.
	for v in range(graph.num_verts()):
		ds.make_set(v)
		
		for u in graph.adj_list[v]:
			graph_edges.append((v, u[0], u[1]))
			
	graph_edges = sort_list(graph_edges)
		
	#Assemble the MST by adding all the edges in proper order.
	mst_result = []

	for i in graph_edges:
		edge_set1 = ds.find_set(i[0])
		edge_set2 = ds.find_set(i[1])
		
		if edge_set1 != edge_set2:
			ds.union_set(edge_set1,edge_set2)
			mst_result.append(i[:-1])
			
	return mst_result
		
#Sort a given list of edges from the Graph and then merge two sorted halves together.			
def sort_list(graph_edges):
	if len(graph_edges) == 1:
		return graph_edges

	mid = round(len(graph_edges) / 2)
	left_edges = sort_list(graph_edges[0:mid])
	right_edges = sort_list(graph_edges[mid:])

	merged_edges = []
	right_idx = 0
	left_idx = 0	

	#Sort and combine the edges in two halves into sorted_edges list
	while left_idx < len(left_edges) and right_idx < len(right_edges):
		if left_edges[left_idx][2] < right_edges[right_idx][2]:
			merged_edges.append(left_edges[left_idx])
			left_idx += 1
		else:
			merged_edges.append(right_edges[right_idx])
			right_idx += 1
			
	while left_idx < len(left_edges):
		merged_edges.append(left_edges[left_idx])
		left_idx += 1
		
	while right_idx < len(right_edges):
		merged_edges.append(right_edges[right_idx])
		right_idx += 1

	return merged_edges
	