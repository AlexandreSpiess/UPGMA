# UPGMA Implementation and Dendrogram Visualization

This repository provides an implementation of the **Unweighted Pair Group Method with Arithmetic Mean (UPGMA)** algorithm for hierarchical clustering and visualizing the resulting dendrogram.

---

## Features

- **UPGMA Algorithm**: Perform hierarchical clustering based on pairwise distance matrices.
- **Dendrogram Visualization**: Visualize the clustering process using a dendrogram.
- **Custom Distance Matrices**: Input custom distance matrices for different datasets.

---

## Requirements

### Prerequisites
The code requires Python 3.x and the following libraries:

- `numpy`
- `matplotlib`
- `scipy`

## Code Structure

### `main.py`
The main entry point of the program:
- **Loads input data**: Initializes labels and the distance matrix.
- **Executes the UPGMA algorithm**: Performs hierarchical clustering step-by-step.
- **Visualizes the resulting dendrogram**: Displays the dendrogram for the hierarchical clustering.

---

### `src/upgma.py`
Implements the UPGMA algorithm with the following key methods:
- **`min`**: Finds the closest clusters based on the minimum distance in the matrix.
- **`join_tabels`**: Updates the distance matrix after merging clusters by recalculating distances.
- **`computeDendrogramMatrix`**: Updates the dendrogram matrix for visualization.
- **`join_labels`**: Merges cluster labels for tracking cluster combinations.
- **`compute`**: Executes the entire clustering process step-by-step.

---

### `src/dendrogram.py`
Generates a dendrogram using `scipy.cluster.hierarchy` and `matplotlib`:
- **`plot`**: Creates and displays the dendrogram based on the clustering results.

## How to Use

### Input Format

The input should include:

1. **Labels**: A list of sample names or identifiers.
2. **Distance Matrix**: A nested list representing pairwise distances in a lower triangular format.

### Example

```python
labels = ['A', 'B', 'C', 'D']
data = [
    [],          # Distances from A
    [2],         # Distances from B
    [6, 5],      # Distances from C
    [10, 9, 8]   # Distances from D
]
```

