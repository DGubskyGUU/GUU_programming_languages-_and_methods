num = int(input("Введите число:"))
sym = input("Введите букву:")
if num < 0 or num > 9 or not (sym == "a" or sym =="b"or sym =="c"or sym =="d" or sym =="e" or sym =="f" or sym =="g" or sym =="h"):
    print("ошибка")
	# проверка условия на существование клетки
else:
 if sym =="a" or sym =="c" or sym =="e" or sym =="g":
     a=0
 else:
     a=1
	 # проверка на цвет нижнего квадрата на цвет 0- черный, 1-белый
 a = a + num
 if (a%2) == 0:
     print("клетка белая")
 else:
     print("клетка черная")
