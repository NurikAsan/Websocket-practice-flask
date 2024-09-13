x = int(input("Введите число от 1 до 9: "))

if x < 1 or x > 9:
    print("Ошибка ввода")
else:
    if 1 <= x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов строки: "))
        print(s *n)    
        
    elif 4 <= x <= 6:
        m = int(input("Введите степень: "))
        print(f"Результат возведения в степень: {x ** m} ")
    
    elif 7 <= x <= 9:
        for i in range(10):
            x += 1
            print(x)
    else:
        print("Ошибка ввода")




#2 Task

# Вывод названия программы
print("Общество в начале XXI века")

while True:
    try:
        age = int(input("Введите ваш возраст: "))
        if 0 <= age <= 7:
            print("Вам в детский сад")
        elif 8 <= age < 18:
            print("Вам в школу")
        elif 18 <= age < 25:
            print("Вам в профессиональное учебное заведение")
        elif 25 <= age < 60:
            print("Вам на работу")
        elif 60 <= age <= 120:
            print("Вам предоставляется выбор")
        elif age < 0 or age > 120:
            for _ in range(5):
                print("Ошибка! Это программа для людей!")
        else:
            print("Ошибка ввода")
        
        break
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числовое значение.")


