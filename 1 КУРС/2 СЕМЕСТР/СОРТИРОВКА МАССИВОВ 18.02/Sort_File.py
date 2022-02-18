i = input('Введите путь к файлу: ')
with open(i, 'r') as file:
    must = [int(row) for row in file]
n = len(i)
def chan(r):
    swag = True
    while swag:
        for s in range(n - 1):
            if r[s] > r[s + 1]:
                r[s], r[s + 1] = r[s + 1], r[s]
                continue
            if r[s - 1] < r[s]:
                continue
            if r[s] < r[s + 1]:
                swag = False
                break
            else:
                continue
chan(i)
print(i)