def toBASE(ciferka, system):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[ciferka % system] 
    while ciferka >= system:
        ciferka = ciferka // system
        b += alpha[ciferka % system] 
    return b[::-1] 

Number = input("Введите число/Цифру: ")
System_Base = int(input("Из какой системы счисления: "))
System_New = int(input("В какую: "))

a = int(Number,System_Base)
a = toBASE(a,System_New)
 
print(a)