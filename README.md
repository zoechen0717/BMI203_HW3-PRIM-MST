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

- **Initialize the MST** by selecting an arbitrary starting node. Keep track of visited nodes and the minimum edge weights needed to connect each node to the MST.
- **Use a priority queue (min heap)** to efficiently select the smallest edge that connects a new node to the MST.
- **Expand the MST step by step** by adding the minimum-weight edge, marking the new node as visited, and updating the smallest known edges for its neighbors.
- **Repeat the process until all nodes are included**, ensuring that exactly \(n-1\) edges are in the MST.
- **Construct the MST adjacency matrix**, ensuring it correctly represents the final tree and maintains symmetry for the undirected graph.

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
