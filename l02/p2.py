"""

Macierze!

https://www.mathsisfun.com/algebra/matrix-multiplying.html


Macierze są bardzo powszechne, np obrazek mapa bitowa to :

[
   [[r,g,b], [r,g,b] ...razy 800..],
   [[r,g,b], [r,g,b] ...razy 800..],
   [[r,g,b], [r,g,b] ...razy 800..],
   [[r,g,b], [r,g,b] ...razy 800..],
   ...razy 600....
]

Jeśli chcecie pisać gry, macierz translacji rotacji ... etc
Lub w grafice komputerowej, obracanie/skalowanie obrazka
"""


def print2d_array(array2d):
    cols, rows = len(array2d[0]), len(array2d)
    print(f"(Array size {cols} x {rows})")
    for row in array2d:
        for el in row:
            print(f'{el}\t', end='')
        print()


def transpose(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize a new matrix with the transposed dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Fill in the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# def transpose(matrix):
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# def transpose(matrix):
#     return list(map(list, zip(*matrix)))

def add_two_matrixes(m1, m2):
    cols, rows = len(m1[0]), len(m1)
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = m1[i][j] + m2[i][j]

    return result


if __name__ == "__main__":
    # tak można zapisać macierz, jako tablica 2d albo lista list
    array2d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print2d_array(array2d)
    print('--transposed-->')
    print2d_array(transpose(array2d))

    print("add two matrixes:")
    print2d_array(array2d)
    print("+")
    print2d_array(array2d)
    print("=")
    result = add_two_matrixes(array2d, array2d)
    print2d_array(result)


    # dla chętnych ... zaimplementujcie mnożenie macierzy(nie jest tak jak w przypadku dodawania, nie każdy z każdym)
    # zaawansowane operacje na macierzach, biblioteka numpy, ma to wbudowane, nie trzeba pisać tych funkcji samemu
    # biblioteka do operacji na obrazkach, video https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
