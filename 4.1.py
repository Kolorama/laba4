try:
    number = int(input("Ваше число"))
except ValueError:
    print("Это не число")
else:
    if number % 3 == 0 :
        print(f"{number} can del 3")
    elif number == 0:
        print("Введен 0")
    else:
        print(f"{number} can't del 3")
