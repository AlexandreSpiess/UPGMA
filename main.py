
import src.upgma as UPGMA
import src.dendrogram as dendrogram


def main():
    print("Début du programme principal")

    labels = ['1', '2', '3', '4','5','6']
    data = [[],
            [6],
            [14, 14],
            [15, 17, 14],
            [12, 12, 10, 11],
            [13, 15, 12, 8, 11]]

    data = [[float(element) for element in row] for row in data]
    print(f"labels : {labels}")
    for s in data:
        print(s)

    ####################################################################################################################

    umpga = UPGMA.UPGMA(data, labels)

    while len(umpga.labels) > 1:
        print("#" * 29)
        umpga.compute()

    dendrogram.plot(umpga.dist,labels)

    print("Fin du programme principal")


if __name__ == '__main__':
    main()