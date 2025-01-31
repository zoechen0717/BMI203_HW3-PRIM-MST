import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances
from scipy.sparse.csgraph import connected_components

def check_mst(adj_mat: np.ndarray,
              mst: np.ndarray,
              expected_weight: int,
              allowed_error: float = 0.0001):
    """

    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot
    simply check for equality against a known MST of a graph.

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
    assert approx_equal(total, expected_weight)

    #Check if MST has exactly (n-1) edges
    num_nodes = mst.shape[0]
    num_edges = np.sum(mst > 0) // 2  # the adjacency matrix is symmetric
    assert num_edges == num_nodes - 1

    #Check if MST is connected
    n_components, _ = connected_components(mst, directed=False)
    assert n_components == 1

    #Check if MST matrix is symmetric
    assert np.allclose(mst, mst.T)

def test_mst_small():
    """

    Unit test for the construction of a minimum spanning tree on a small graph.

    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """

    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """

    TODO: Write at least one unit test for MST construction.

    """
    #Load and test Small Custom Graph
    small_graph_path = "./data/small_graph.csv"
    adj_mat = np.loadtxt(small_graph_path, delimiter=",")
    g = Graph(adj_mat)
    g.construct_mst()
    assert np.isclose(np.sum(g.mst) / 2, 16), "Incorrect MST weight for small graph"

    #Load and test Single-Node Graph
    single_node_mat = np.array([[0]])
    g_single = Graph(single_node_mat)
    g_single.construct_mst()
    assert np.sum(g_single.mst) == 0, "MST for single-node graph should have no edges"

    #Load and test Fully Connected Graph with Identical Weights
    fully_connected_path = "./data/fully_connected.csv"
    full_adj_mat = np.loadtxt(fully_connected_path, delimiter=",")
    g_full = Graph(full_adj_mat)
    g_full.construct_mst()
    expected_weight = (full_adj_mat.shape[0] - 1) * 10
    assert np.isclose(np.sum(g_full.mst) / 2, expected_weight), "Incorrect MST weight for fully connected graph"
