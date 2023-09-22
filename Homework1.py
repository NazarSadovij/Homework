print ("Вітаю!")
print ("Ця програма стане твоїм другом")
print ("Вона вміє рахувати і загадувати загадки")
a1 = input ("Вибери варіант 1)Калькулятор 2)Загадки")
if a1 == "1":
    print ("Вітаю у calculator")
    a = input ("Введи перше число")
    b = input ("Введи друге число")
    a = int (a)
    b = int (b)
    operation = input ("Вибери дію + - * /: ")
    if operation == "+":
        print (a + b)
    if operation == "-":
        print (a - b)
    if operation == "*":
        print (a * b)
    if operation == "/":
        print (a / b)
elif a1 == "2":
    print ("Я буду задавати тобі загадки")