import unittest
import src.upgma as UPGMA
import src.dendrogram as dendrogram


class MyTestCase(unittest.TestCase):
    def test_baseCase(self):
        labels = ['A', 'B', 'C', 'D']
        data = [[],
                [5],
                [4, 7],
                [7, 10, 7]]
        data = [[float(element) for element in row] for row in data]

        umpga = UPGMA.UPGMA(data, labels)

        while len(umpga.labels) > 1 :
            umpga.compute()

        dendrogram.plot(umpga.dist, labels)

    def test_MediumCase(self):
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        data = [[],
                [19],
                [27, 31],
                [8, 18, 26],
                [33, 36, 41, 31],
                [18, 1, 32, 17, 35],
                [13, 13, 29, 14, 28, 12]]
        data = [[float(element) for element in row] for row in data]

        umpga = UPGMA.UPGMA(data, labels)

        while len(umpga.labels) > 1 :
            umpga.compute()

        dendrogram.plot(umpga.dist, labels)


if __name__ == '__main__':
    unittest.main()
