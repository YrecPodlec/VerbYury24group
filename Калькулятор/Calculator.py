try:
    what = input("Выберите действие: +, -, *, /")
    a = float(input("Введите число: "))
    b = float(input("Введите 2 число: "))
except ValueError:
    print("Просьба вводить только числа!")

what = input("Выберите действие: +, -, *, /")
a = float(input("Введите число: "))
b = float(input("Введите 2 число: "))

try:
    a / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")

what = input("Выберите действие: +, -, *, /")
a = float(input("Введите число: "))
b = float(input("Введите 2 число: "))

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Резульат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
    
    
else:
    print("Этой операции, нет в списке")
what = input("Выберите действие: +, -, *, /")
a = float(input("Введите число: "))
b = float(input("Введите 2 число: "))
