# HW 3: Prim's algorithm

![BuildStatus](https://github.com/zoechen0717/BMI203_HW3-PRIM-MST/workflows/badge.svg?event=push)

## **📌 Project Overview**
This project implements **Prim’s Algorithm** to construct a **Minimum Spanning Tree (MST)** from a given adjacency matrix representation of a **connected, undirected graph**. The MST is represented as an adjacency matrix, ensuring the lowest possible sum of edge weights.

The implementation includes:
- **Graph class** for loading and processing adjacency matrices.
- **Prim’s Algorithm** for MST construction.
- **Unit tests** to verify correctness using sample graphs.

---

## **📖 Method Description**
This method is implemented based on **Prim’s Algorithm**. The pseudocode used in this project is adapted from **[freeCodeCamp](https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/)**, while the Python implementation of the MST adjacency matrix is developed based on **[GeeksforGeeks](https://www.geeksforgeeks.org/prims-algorithm-in-python/)**.

1. **Initialize Variables**  
   - `num_nodes`: Get the number of nodes from the adjacency matrix.
   - `his`: A list to store the **parent node** of each vertex in the MST.
   - `mst_track`: A boolean list to track whether a node is already in the MST.
   - `min_heap`: A **priority queue** (min heap) to keep track of **edges with the smallest weight**.
   - `key`: A list that holds the **minimum edge weight** required to connect each node to the MST.  
   - **Start from Node `0`**:
     - Set `key[0] = 0` (indicating it is included in MST first).
     - Push `(0, 0)` into `min_heap`, where `0` is the weight, and `0` is the node.

2. **Iterate Until All Nodes are Added to the MST**  
   - **Extract the minimum-weight edge** from the heap.
   - **If the node is already included in MST, skip it**.
   - **Mark the node as visited** (`mst_track[u] = True`).
   - **Check all its neighbors**:
     - If there is an edge (`edge_weight > 0`).
     - If the neighbor **is not already in the MST** (`not mst_track[v]`).
     - If the edge weight is **smaller** than the current stored weight (`edge_weight < key[v]`):
       - **Update `key[v]`** to `edge_weight` (select the smallest edge).
       - **Push `(edge_weight, v)` into the min heap**.
       - **Record `u` as the parent of `v`** in `his[v]`.

3. **Build the MST Adjacency Matrix**  
   - **Create an empty matrix** (`self.mst = np.zeros((num_nodes, num_nodes))`).
   - **Loop through the `his` parent array**:
     - For each node `v` (starting from `1`), find its parent `u`.
     - **Set the edge in the MST matrix**:
       ```python
       self.mst[u][v] = self.adj_mat[u][v]
       self.mst[v][u] = self.adj_mat[u][v]  # Ensure symmetry
       ```
   - The final `self.mst` matrix represents the **Minimum Spanning Tree**.

#### **💡 Key Features**
- Uses **Prim's Algorithm** with a **priority queue (heap)** for efficiency.
- Ensures **correct MST structure** by tracking **parent nodes**.
- Constructs an **undirected** MST (symmetric adjacency matrix).
- **Time Complexity**: **O(E log V)** using a heap for edge selection.

---
## Grading

### Code (6 points)

* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1)
    * Produces expected output on single cell data (1)

### Unit tests (3 points)

* Complete function "check_mst" (1)
* Write at least two unit tests for MST construction (2)

### Style (1 points)

* Readable code with clear comments and method descriptions (1)

### Extra credit (0.5)

* Github actions/workflow (0.5)
