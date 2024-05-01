import numpy as np

import src.umpga as UMPGA


def main():
    print("Début du programme principal")


    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    
    UMPGA.hello()

    umpga = UMPGA.UMPGA(arr)


    print("Fin du programme principal")


if __name__ == '__main__':
    main()