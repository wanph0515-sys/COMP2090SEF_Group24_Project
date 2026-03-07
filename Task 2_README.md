[Task 2-README(1).md](https://github.com/user-attachments/files/25815026/Task.2-README.1.md)

# Task 2 - Graph Structure & Heap Sort

## Project Overview
This project is implemented in Python, focusing on two core functions:
1. Basic operations of undirected graph (vertex/edge addition, neighbor query, DFS traversal) based on adjacency list storage
2. Heap sort algorithm implementation for numerical array sorting

#### Author:HUANG Leiming, TAN Guangxi
## Functional Description
### Graph Class
| Method | Function Description | Parameter Explanation |
|--------|----------------------|-----------------------|
| `__init__()` | Initialize the adjacency list of the graph (empty dictionary) | None |
| `add_vertex(vertex)` | Add a vertex to the graph (skip if the vertex already exists) | `vertex`: Hashable identifier of the vertex (e.g., number, string) |
| `add_edge(v1, v2)` | Add an undirected edge between two vertices (automatically create non-existent vertices) | `v1`/`v2`: Identifiers of the two vertices of the edge |
| `get_neighbors(vertex)` | Get all neighbor vertices of the specified vertex | `vertex`: Target vertex identifier; Return value: List of neighbor vertices (empty list if the vertex does not exist) |
| `dfs_traversal(start_vertex)` | Depth-first traversal of the graph starting from the specified vertex | `start_vertex`: Starting vertex of traversal; Return value: List of vertices in traversal order |
| `__str__()` | Custom string output of the graph (display adjacency list) | None |

### Heap Sort Related Methods
| Method | Function Description | Parameter Explanation |
|--------|----------------------|-----------------------|
| `heapify(arr, n, i, key=None)` | Heapify operation (build max-heap) | `arr`: Array to be heapified; `n`: Size of the heap; `i`: Index of current heapified node; `key`: Reserved parameter (not used) |
| `heap_sort(arr, key=None)` | Main function of heap sort (ascending sort) | `arr`: Array to be sorted; `key`: Reserved parameter (not used); Return value: Sorted array |

## Installation & Running Requirements
- Running environment: Python (No additional third-party dependencies are required)

## Usage Examples
### Heap Sort Usage
```python
# Test heap sort for numerical array
test_nums = [5, 2, 9, 1, 5, 6]
sorted_nums = Graph.heap_sort(test_nums)
print("Heap sort result of numerical array:", sorted_nums)
```

## Key Notes
1. Vertices of the graph must be hashable types (e.g., numbers, strings, tuples), unhashable objects like lists are not allowed
2. Adding duplicate vertices will be skipped; adding duplicate edges will be checked to avoid repeated storage in the adjacency list
3. The `key` parameter in heap sort methods is a reserved parameter and has no actual effect on the current sorting logic
4. DFS traversal only covers the connected component reachable from the starting vertex; other vertices of the disconnected graph will not be included in the traversal result
