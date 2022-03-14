from tkinter import *
#функция калькулятора
def calculation():
    try:
        num = int(a.get())
        num2 = int(b.get())
        num3 = num2 + num
        c.set(str(num3))
    except ValueError:
        print("Вводите только числа!")
#настройки окна
windows = Tk()
windows.title("СЛОЖЕНИЕ")
windows.geometry("400x400")
#изменение переменных
a = StringVar()
b = StringVar()
c = StringVar()
#окошки и надписи к ним
Label(windows, text="1 число").place(x=5, y=20)
Entry(windows, textvariable=a).place(x=90, y=20)
Label(windows, text="2 число").place(x=5, y=55)
Entry(windows, textvariable=b).place(x=90, y=55)
Label(windows, text="РЕЗУЛЬТАТ").place(x=5, y=90)
Entry(windows, textvariable=c).place(x=90, y=90)
#кнопка сложения
but = Button(text="Сложить", command=calculation).place(x=90, y=125)

windows.mainloop()