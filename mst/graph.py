import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """

        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat`
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.

        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else:
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """

        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's
        algorithm to construct an adjacency matrix encoding the minimum spanning mst of `self.adj_mat`.

        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists.

        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning mst of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the
        `heapify`, `heappop`, and `heappush` functions.

        Pseudocode：https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/
        prim(graph):
        mst = empty set
        startVertex = first vertex in graph
        mst.add(startVertex)
        edges = edges connected to startVertex

        while mst has fewer vertices than graph:
            minEdge, minWeight = findMinEdge(edges)

            mst.add(minEdge)

            for edge in edges connected to minEdge:
                if edge is not in mst:
                    edges.add(edge)

            # Remove the minimum edge from the set of edges to consider
            edges.remove(minEdge)

        return mst as an array
        """
        num_nodes = len(self.adj_mat) #Count number of nodes in the graph
        his = [-1] * num_nodes #Stores the visited parent nodes in MST
        mst_track = [False] * num_nodes# Track if a node is include in MST or not

        min_heap = [] #Priority queue to store edges with min weight
        key = [float('inf')] * num_nodes #Create a list for keys and initialize all keys as infinite (INF)
        key[0] = 0 #Start from the first vertex
        heapq.heappush(min_heap, (0, 0)) #Push the first min weight and edge in to queues

        while min_heap: #https://www.cnblogs.com/biyeymyhjob/archive/2012/07/30/2615542.html
            weight, u = heapq.heappop(min_heap)
            if mst_track[u]: #If vertex is included, skip
                continue
            mst_track[u] = True #Check mark vertex as included

            #Loop through all nodes to check adjacent edges
            for v in range(num_nodes):
                edge_weight = self.adj_mat[u][v]
                #If there is an edge, vertex v is not in MST, and the edge is smaller than current key
                if edge_weight > 0 and not mst_track[v] and edge_weight < key[v]:
                    key[v] = edge_weight #Update the min weight
                    heapq.heappush(min_heap, (edge_weight, v)) #Push the updated wieight and nodes to heap
                    his[v] = u #Update visited nodes

        #Creat the MST adjacency matrix
        #https://www.geeksforgeeks.org/prims-algorithm-in-python/
        self.mst = np.zeros((num_nodes, num_nodes))
        for v in range(1, num_nodes):
            u = his[v]
            if u != -1:
                self.mst[u][v] = self.adj_mat[u][v]
