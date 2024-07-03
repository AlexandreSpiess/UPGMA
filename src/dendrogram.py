import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform


def plot(tab, labels):
    # Step 2: Compute the linkage matrix
    Z = linkage(squareform(tab), method='single')  # You can use 'single', 'complete', 'average', etc.

    # Step 3: Create the dendrogram
    plt.figure(figsize=(10, 7))
    dendrogram(Z, labels=labels)
    plt.title('Dendrogram')
    plt.xlabel('Sample index')
    plt.ylabel('Distance')
    plt.show()
