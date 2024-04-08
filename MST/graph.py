class Graph:
    # Initializes a Graph object with a given number of vertices.
    def __init__(self,number_of_verts):
        self.total_verts=number_of_verts
        self.adj_list=[[] for _ in range(number_of_verts)]

    
    # Adds an additional vertex to the graph.
    def add_vertex(self):
        self.total_verts+=1
        self.adj_list.append([])

    
    # Adds an additional vertex to the graph.
    def add_edge(self,from_idx, to_idx, weight = 1 ):

        # Check if the indices are within valid range
        if from_idx < 0 or from_idx >= self.total_verts or to_idx < 0 or to_idx >= self.total_verts:
            return False
            
        # Check if the edge already exists
        if self.has_edge(from_idx, to_idx):
            return False
            
        # Add the edge from the source vertex to the destination vertex
        self.adj_list[from_idx].append((to_idx, weight))
        return True

    
    #Returns the number of edges in the graph.
    def num_edges(self):
        count = 0
        for edges in self.adj_list:
            count += len(edges)
        return count

    
    #Returns the number of vertices in the graph.
    def num_verts(self):
        return self.total_verts

    
    #Checks if an edge exists between two vertices in the graph.
    def has_edge(self, from_idx,to_idx):

        # Check if the indices are within valid range
        if from_idx < 0 or from_idx >= self.total_verts or to_idx < 0 or to_idx >= self.total_verts:
            return False
            
        # Iterate over the adjacency list of the source vertex
        for vertex, _ in self.adj_list[from_idx]:
            if vertex == to_idx:
                return True
        return False

    
    # Returns the weight of an edge between two vertices in the graph.
    def edge_weight(self, from_idx,to_idx):

        # Check if the indices are within valid range
        if from_idx < 0 or from_idx >= self.total_verts or to_idx < 0 or to_idx >= self.total_verts:
            return None

        # Iterate over the adjacency list of the source vertex
        for vertex, weight in self.adj_list[from_idx]:
            if vertex == to_idx:
                return weight
        return None

    
    # Returns the vertices connected from a given vertex.
    def get_connected(self, v):
        if v < 0 or v >= self.total_verts:
            return []

        # Return the adjacency list of the vertex
        return self.adj_list[v]