
import src.upgma as UPGMA
import src.dendrogram as dendrogram


def main():
    print("Début du programme principal")

    labels = ['A', 'B', 'C', 'D']
    data = [[],
            [5],
            [4, 7],
            [7, 10, 7]]

    data = [[float(element) for element in row] for row in data]
    print(f"labels : {labels}")
    print(f"data : \n{data}")

    ####################################################################################################################

    umpga = UPGMA.UPGMA(data, labels)

    print("#"*29)

    umpga.compute()

    print("#" * 29)

    umpga.compute()

    print("#" * 29)

    umpga.compute()

    dendrogram.plot(umpga.dist,labels)

    print("Fin du programme principal")


if __name__ == '__main__':
    main()