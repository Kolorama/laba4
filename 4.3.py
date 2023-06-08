d = input("Дата")
d = d.split(",")
if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
    print ("Не существует")
else:
    print("Существует")
