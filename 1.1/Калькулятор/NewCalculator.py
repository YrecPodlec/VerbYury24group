#Калькулятор
try:
    what = input("Выберите действие: +, -, *, /: ")
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
    if what != "+" and "-" and "*" and "/":
        print('Выбирать надо только то, что даёт выбрать программа!')
except (ZeroDivisionError, ValueError):
    print("Просьба на 0 не делить И выбирать только то, что даёт выбрать программа!")
