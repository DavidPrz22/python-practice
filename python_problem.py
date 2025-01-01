"""
El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.

detectBombs([
    [true, false, false],
    [false, true, false],
    [false, false, false]
])
// [
//   [1, 2, 1],
//   [2, 1, 1],
//   [1, 1, 1]
// ]

detectBombs([
    [true, false],
    [false, false]
])
// [
//   [0, 1],
//   [1, 1]
// ]

detectBombs([
    [true, true],
    [false, false],
    [true, true]
])

// [
//   [1, 1],
//   [4, 4],
//   [1, 1]
// ]

Nota: ¿Quieres una pista? Seguro que has jugado al juego de buscaminas antes… 😉

"""


def main():

    bombs = [
                [True, False, False],
                [False, True, False],
                [False, False, False]
            ]
    
    for i in detectBombs(bombs):
        print(i)


def detectBombs(bombs: list):
    width = len(bombs[0])
    height = len(bombs)
    
    numbers = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):

        for j in range(width):
            
            if bombs[i][j] == True:

                # TOP LEFT CORNER - DONE
                if i == 0 and j == 0:

                    for yx in range(2):
                        for (ix, val) in enumerate(bombs[i + yx][j: j + 2]):
                            
                            if not (yx == 0 and ix == 0):
                                
                                if val == False or val == True:
                                    numbers[i + yx][j + ix] += 1

                
                # TOP RIGHT CORNER - DONE
                if i == 0 and j == (width - 1):

                    for yx in range(2):
                        for (ix, val) in enumerate(bombs[i + yx][j - 1: j + 1]):

                            if not (yx == 0 and ix == 1):

                                if val == False or val == True:
                                    
                                    if ix == 0:
                                        numbers[i + yx][j - 1] += 1
                                    else:
                                        numbers[i + yx][j] += 1

                # BOTTOM LEFT CORNER - DONE
                if i == (height - 1) and j == 0:

                    for yx in range(-1, 1):
                        for (ix, val) in enumerate(bombs[i + yx][j: j + 2]):

                            if not (yx == 0 and ix == 0):

                                if val == False or val == True:
                                    
                                        numbers[i + yx][j + ix] += 1

                # BOTTOM RIGHT CORNER - DONE
                if i == (height - 1) and j == (width - 1):

                    for yx in range(-1, 1):
                        for (ix, val) in enumerate(bombs[i + yx][j - 1: j + 2]):

                            if not (yx == 0 and ix == 1):

                                if val == False or val == True:
                                    if ix == 0:
                                        numbers[i + yx][j - 1] += 1
                                    else:
                                        numbers[i + yx][j] += 1

                # TOP CENTER
                if i == 0 and (j > 0 and j < width - 1):

                    for yx in range(2):
                        for (ix, val) in enumerate(bombs[i + yx][j - 1: j + 2]):

                            if not (yx == 0 and ix == 1):
                                
                                if val == False or val == True:

                                    numbers[i + yx][j + ix - 1] += 1

                # BOTTOM CENTER
                if i == (height - 1) and (j > 0 and j < width - 1):

                    for yx in range(-1, 1):
                        for (ix, val) in enumerate(bombs[i + yx][j - 1: j + 2]):

                            if not (yx == 0 and ix == 1):
                                if val == False or val == True:

                                    numbers[i + yx][j + ix - 1] += 1

                # LEFT CENTER
                if j == 0 and (i > 0 and i < height - 1):

                    for yx in range(-1, 2):
                        for (ix, val) in enumerate(bombs[i + yx][j: j + 2]):

                            if not (yx == 0 and ix == 0):

                                if val == False or val == True:
                                        numbers[i + yx][j + ix] += 1

                # RIGHT CENTER
                if j == (width - 1) and (i > 0 and i < height - 1):

                    for yx in range(-1, 2):
                        temp = -1
                        for (ix, val) in enumerate(bombs[i + yx][j - 1: j + 2]):
                            if not (yx == 0 and ix == 1):

                                if val == False or val == True:
                                    if yx == -1 or yx == 1:
                                        numbers[i + yx][j + temp] += 1
                                        temp += 1
                                    else:
                                        numbers[i][j - 1] += 1
                
                # MIDDLE IF PRESENT

                if (i > 0 and i < height - 1) and (j > 0 and j < width - 1):

                    for yx in range(-1, 2):
                        for (ix, val) in enumerate(bombs[i + yx][j - 1 : j + 2]):

                            if not (yx == 0 and ix == 1):

                                if val == False or val == True:
                                    numbers[i + yx][j + ix - 1] += 1

    return numbers


if __name__ == "__main__":
    main()
