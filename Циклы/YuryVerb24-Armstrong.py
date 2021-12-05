print("Вербитский Юрий, группа: 14124.\nЭта программа выводит все числа Армстронга от 1 до 10000.")
def armstrong(number: int) -> bool:
   number_list = [int(n) for n in str(number)]
   number_list_power =[n ** len(str(number)) for n in number_list]
   return (sum(number_list_power) == number)
for n in range (1, 10001):
   if armstrong(n):
      print (n)
