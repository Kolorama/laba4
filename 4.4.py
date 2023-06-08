num = input("Номер билета")
x = 0
y = 0
if len(num) % 2 == 0:
    for i in num[0:int(len(num) / 2)]:
        x = x + int(i)
    for i in num[int(len(num) / 2):int(len(num)) + 1]:
        y = y + int(i)
    if x == y:
        print("Lucky")
    else:
        print("unlucky")
else:
    print("Кол-во цифр нечетно")