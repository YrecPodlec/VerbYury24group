print("Вербитский Юрий, группа: 14124.\nЭта программа выводит все дружественные числа от 1 до 10000.")
def frend(n):
    return sum(i for i in range(1, n) if n % i == 0)
for i in range(1, 10001):
    s = frend(i)
    if s > i and frend(s) == i:
        print(i, s)