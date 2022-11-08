print("Задача 1")
a = 10
b = 15
c = 5
a, b, c = b, c, a
print(a, b , c, '\n')
print("Задача 2.1")
try:
    numb_1 = int(input("Введите число: "))
    numb_2 = int(input("Введите 2 число: "))
    print(numb_1+numb_2, "\n")
except ValueError:
    print("Вы ввели не числа!")
print("Задача 3.1")
for x in range(0, 101):
    print("X в 5 степени: ", x**5)
print("\n")
print("Задача 3.2")
for x in range(0, 101):
    print("X в 5 степени: ", x*x*x*x*x)
print("\n")
print("Задача 4")
fibonachi = int(input("Введите число от 0 до 250: "))
if fibonachi < 0:
    print("Это число меньше нуля")
elif fibonachi > 250:
    print("Это число больше 250")
match fibonachi:
    case 0 | 1 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233:
        print("Это число фибоначи")
    case default:
        print("Это просто число")
print("\n")
print("Задача 5")
print("Способ 1")
def season(number: int) -> str:
    match number:
        case 1 | 2 | 12:
            return "Зима"
        case 3 | 4 | 5:
            return "Весна"
        case 6 | 7 | 8:
            return "Лето"
        case 9 | 10 | 11:
            return "Осень"
        case _:
            return "Нет такого месяца"
print(season(int(input("Введите месяц числом: "))))
print("Способ 2")
vremena = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
month = int(input("Введите месяц числом: "))
for key in vremena.keys():
    if month in vremena[key]:
        print(key)
print("\n")
print("Задача 6")
nomer = int(input("Введите число: "))
cislo_1 = 0
cislo_2 = 0
while cislo_2 <= nomer:
    if cislo_2 % 2 == 0:
        cislo_1 += cislo_2
    cislo_2 += 1
print(cislo_1)
print("\n")
print("Задача 7")
cifra = int(input("Введите целое число до 250: "))
if cifra <= 250:
    setchik = 0
    for i in range(cifra - 1, 1, -1):
        if cifra % i == 0:
            setchik += 1
    print("Количество:", setchik)
else:
    print("Это число больше чем 250")
print("\n")
print("Задача 8")
def troyka(a, b, c = None):
    return ((a if b == 0 else troyka(b, a % b)) if c is None
            else troyka(troyka(a, b), troyka(a, c)))
n = int(input("Введите последнее число: "))
search = [i * i for i in range(2, n + 1)]
zero = set()
for iii in range(n):
    for j in range(iii + 1, n - 1):
        if search[iii] + search[j] in search:
            aaa = iii + 2
            bbb = j + 2
            ccc = search.index(search[iii] + search[j])+2
            ddd = troyka(aaa, bbb, ccc)
            zero.add((aaa // ddd, bbb // ddd, ccc // ddd))
res = list(zero)
res.sort()
for iii in res:
    print(iii)
print("\n")
print("Задача 9")
def nahodilka(number_i):
    number_j = number_i
    while(number_j):
        dom = number_j % 10
        number_j //= 10
        if (dom == 0 or number_i % dom):
            return False
    return True
for number_i in range(1, int(input("Введите последнее число: ")) + 1):
    if (nahodilka(number_i)):
        print(number_i)
print("\n")
print("Задача 10")
porog = int(input("Введите последнее число: "))
nachalo = 0
for big_range in range(0, porog):
    edenica = 1
    for small_range in range(2, big_range // 2 + 1):
        if big_range % small_range == 0:
            edenica += small_range
    if edenica == big_range:
        nachalo += 1
        if nachalo < 5:
            print(big_range)
print("\n")
print("Задача 11")
massive = ['frukt', 'pirog', 'drakon', 'last']
massive_rev = reversed(massive)
print(next(massive_rev))
print(massive[-1:])
print(massive.pop())
print("\n")
print("Задача 12")
massive_2 = ['ryba', 'knyaz', 'cat', 'dog', 'dvornik']
massive_2_rev = massive_2[::-1]
print("Обчный: ", massive_2)
print("Обратный: ", massive_2_rev)
print("\n")
print("Задача 13")
massive_3 = [1, 99, 45, 354, 4]
start_sum = 0
def plus(x):
    global start_sum
    if x == len(massive_3):
        return
    start_sum += massive_3[x]
    plus(x+1)
plus(0)
print("Массив: ", massive_3)
print('Сумма элементов: ', start_sum)
print("\n")
print("Задача 15")
tablitsa = int(input("Введите размер от 5 до 20: "))
if 5 <= tablitsa <= 20:
    for i in range(1, tablitsa + 1):
        for j in range(1, tablitsa):
            print(i * j, end='\t')
        print(i * tablitsa)
else:
    print("Вы нарушили правило")
print("\n")
print("Задача 14.1 и 14.2")
from tkinter import *
from tkinter import ttk
import sys
root = Tk()
root.title("Конвертер валют")
spysok_knopok = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9", "В RU", "В USD", "Exit", "C"]
r = 1
c = 0
for i in spysok_knopok:
    cmd = lambda x=i: schitalka_money(x)
    ttk.Button(root, text=i, command=cmd, width=7).grid(row=r, column=c)
    c += 1
    if c > 6:
        c = 0
        r += 1
raschoyt = Entry(root, width=55)
raschoyt.grid(row=0, column=0, columnspan=9)
def schitalka_money(key):
    global memory
    if key == "C":
        raschoyt.delete(0, END)
    elif key == "В RU":
        raschoyt.insert(END, "=" + str(63 * (int(raschoyt.get()))))
        pass
    elif key == "В USD":
        raschoyt.insert(END, "=" + str(0.016 * (int(raschoyt.get()))))
        pass
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit()
    else:
        raschoyt.insert(END, key)
root.mainloop()