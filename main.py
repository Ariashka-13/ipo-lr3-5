y=int(input("Введите год: ")) #ввод года
if y%4==0 and y%100!=0 or y%400==0: #если год кратен 4, но не кратен 100 или год кратен 400
    print(y, " - високосный год") #вывод: данный год является високосным
else: #если год не соответствуем условиям
    print(y, " - невисокосный год") #вывод: данный год не является високосным