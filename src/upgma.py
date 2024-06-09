import numpy as np


class UPGMA(object):

    def __init__(self, tab, labels):
        self.labels = [[i] for i in labels]
        self.labels_rep = [[i] for i in range(len(labels))]
        self.tab = tab
        self.dist = np.zeros((len(self.tab), len(self.tab)))

        print("INIT")

        print(self.labels)
        print(self.tab)
        print(self.dist)

    def min(self):

        min_cell = float("inf")
        x, y = -1, -1

        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i][j] < min_cell:
                    min_cell = self.tab[i][j]
                    x, y = i, j

        return x, y

    def join_tabels(self, index):

        x, y = index

        if y < x:
            x, y = y, x

        row = []

        for i in range(0, x):

            sizeA = len(self.labels[x]) * len(self.labels[i])
            sizeB = len(self.labels[y]) * len(self.labels[i])

            row.append((self.tab[x][i] * sizeA + self.tab[y][i] * sizeB) /
                       (len(self.labels[i]) * (len(self.labels[x]) + len(self.labels[y]))))

        for i in range(x + 1, y):
            sizeA = len(self.labels[x]) * len(self.labels[i])
            sizeB = len(self.labels[y]) * len(self.labels[i])

            row.append((self.tab[i][x] * sizeA + self.tab[y][i] * sizeB) /
                       (len(self.labels[i]) * (len(self.labels[x]) + len(self.labels[y]))))

            del self.tab[i][x]

        for i in range(y + 1, len(self.tab)):
            sizeA = len(self.labels[x]) * len(self.labels[i])
            sizeB = len(self.labels[y]) * len(self.labels[i])

            row.append((self.tab[i][x] * sizeA + self.tab[i][y] * sizeB) /
                       (len(self.labels[i]) * (len(self.labels[x]) + len(self.labels[y]))))

            del self.tab[i][y]
            del self.tab[i][x]

        del self.tab[y]
        del self.tab[x]

        self.tab.append(row)

    def computeDistanceMatrix(self, index):
        x, y = index

        if y < x:
            x, y = y, x

        dist = self.tab[y][x] / 2

        for i in self.labels_rep[x]:
            for j in self.labels_rep[y]:
                self.dist[i,j] = dist
                self.dist[j, i] = dist



    def join_labels(self, index):
        x, y = index

        if y < x:
            x, y = y, x

        a = self.labels.pop(y)
        b = self.labels.pop(x)
        self.labels.append(b + a)

        a = self.labels_rep.pop(y)
        b = self.labels_rep.pop(x)
        self.labels_rep.append(b + a)

    def compute(self):

        index = self.min()

        self.computeDistanceMatrix(index)

        self.join_tabels(index)

        self.join_labels(index)

        print(index)
        print(self.tab)
        print(self.labels_rep)
        print(self.labels)
        print(self.dist)

