#1. Удвоить каждый элемент коллекции.
a = [12, 139, 99, 9787, 753, 4, 32, 77, 33, 444, 52, 2]
b = list(map(lambda x: 2*x, a))
print(b)

#2. Найти произведение по-элементно элементов из трех коллекций.
l = list(range(0, 30, 3))
l1 = list(range(100, 200, 3))
l2 = list(range(0, 10, 2))
c = zip(l, l1, l2)
print(list(c))

#3. Найти длину каждого элемента из коллекции.
#1 способ:
cities = ["Богота", "Токио", "Москва", "Рим", "Найроби", "Денвер", "Берлин", "Стокгольм"]
mapka = map(len, cities)
listok = list(mapka)
print(listok)
#2 способ:
len_numbers = list(map(lambda x: len(str(x)), a))
print(len_numbers)

#4. Оставить только четные элементы коллекции.
chetnye = list(filter(lambda x: not int(x) % 2, a))
print(chetnye)

#5. Оставить только непустые элементы коллекции.
animals = ['', 'ziraf', 'coska', '', 'slon', '', 'sobaka', '', 'nosorog', 'crocodil']
dvornik = list(filter(lambda x: x != '', animals))
print(dvornik)

#6. Есть три коллекции, нужно упаковать элементы тройками.
Collection1 = [3, 6, 7, 34, 56, 78, 364, 675, 956]
Collection2 = [2, 5, 4, 32, 45, 65, 322, 534, 555]
Collection3 = [9, 8, 7, 43, 77, 54, 211, 533, 222]
troyka = zip(Collection1, Collection2, Collection3)
print(list(troyka))

#7. Есть две коллекции, нужно упаковать элементы двойками при этом элементы второй коллекции должны быть удвоенны.
mozgi1 = [3, 5, 6, 77, 4, 34, 99, 567, 85]
mozgi2 = [1, 2, 4, 65, 13, 45, 89, 75, 31]
dubble = list(map(lambda x: 2*x, mozgi2))
dvoyka = zip(mozgi1, dubble)
print(list(dvoyka))


def f(a): 
    return a[0]*a[1]*a[2] 
cc1 = [int(i) for i in input("Введите равное количество элементов три раза: (1) ").split()]
cc2 = [int(i) for i in input("Введите равное количество элементов три раза: (2) ").split()]
cc3 = [int(i) for i in input("Введите равное количество элементов три раза: (3) ").split()]
c=list(zip(cc1,cc2,cc3))
print(c)
cc4 = list(map(f, list(zip(cc1,cc2,cc3))))
print("2.", cc4)
