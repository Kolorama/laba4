try:
    s = int(input("Ваше число"))
    v = 100 / s
except ValueError:
    print("Number exists")
except ZeroDivisionError:
    print("Введен 0")
else:
    print(f"100 : {s} = {v}")