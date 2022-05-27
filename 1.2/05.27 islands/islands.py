cislo_ostrovov = 0
coordinations = dict()
def islands(x, y, fill, matrix):
    global cislo_ostrovov
    global coordinations
    if x >= len(matrix) or y >= len(matrix[x]):
        return
    if fill == 0 and matrix[x][y] > 0:
        cislo_ostrovov += 1
        fill = matrix[x][y]
    if matrix[x][y] == fill and matrix[x][y] > 0:
        if cislo_ostrovov in coordinations:
            coordinations[cislo_ostrovov].append((x,y))
        else:
            coordinations[cislo_ostrovov] = [(x,y)]
        matrix[x][y] *= -1
        islands(x+1, y, fill, matrix)
        islands(x-1, y, fill, matrix)
        islands(x, y+1, fill, matrix)
        islands(x, y-1, fill, matrix)
matrix = []
f = open('matrix.txt','r')
for line in f:
    line = list(map(int, line.split()))
    matrix.append(line)
f.close()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        islands(i, j, 0, matrix)
print('ОСТРОВА:')
for key in coordinations:
    min_x = min(coordinations[key], key=lambda x: x[0])[0]
    min_y = min(coordinations[key], key=lambda x: x[1])[1]
    max_x = max(coordinations[key], key=lambda x: x[0])[0]
    max_y = max(coordinations[key], key=lambda x: x[1])[1]
    for i in range(min_x, max_x+1):
        for j in range(min_y,max_y+1):
            if (i,j) in coordinations[key]:
                print(-matrix[i][j], end=' ')
            else:
                print(" ", end=' ')
        print()
    print()
print()
print("Количество: ",cislo_ostrovov)
print("Координаты: ", coordinations)