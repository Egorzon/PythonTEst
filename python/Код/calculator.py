#Калькулятор
from colorama import init
from colorama import Fore,Back,Style
init()

print(Back.GREEN)

what = input("Что делаем?(+,-,/,*):")
print(Fore.RED)
a=float (input('ВВеди первое число: '))
b=float (input('ВВеди второе число: '))
if what == "+":
    c = a + b
    print ('Результат: ' + str(c))
elif what == "/":
    c = a / b
    print ('Результат: ' + str(c))
elif what == "*":
    c = a * b
    print ('Результат: ' + str(c))
else:
    print('Выбрана неверная операция')
input()
