from math import *  # импортируем все функции из модуля math

print("Ruudu karakteristikud")
try:
    a = int(input('Sisesta ruudu külje pikkus => '))  
    if a > 0:
        print("Õige number")
        S = a**2
        print("Ruudu pindala", S)
        P = 4 * a
        print("Ruudu ümbermõõt", P)
        di = a * sqrt(2)  
        print("Ruudu diagonaal", round(di, 2))
        print()
    else:
        print("Kirjutage number mitte taht")
except ValueError:  
    print("Valed andmed")

print("Ristküliku karakteristikud")  
try:
    b = int(input("Sisesta ristküliku 1. külje pikkus => "))  
    c = int(input("Sisesta ristküliku 2. külje pikkus => "))  
    if b > 0 and c > 0:
        print("Õigesti sisestatud number")
        S = b * c
        print("Ristküliku pindala", S)  
        P = 2 * (b + c)  
        print("Ristküliku ümbermõõt", P)
        di = sqrt(b**2 + c**2)  
        print("Ristküliku diagonaal", round(di, 2))  
        print()
    else:
        print("Kirjutage number mitte taht")
except ValueError:
    print("Valed andmed")

print("Ringi karakteristikud")
try:
    r = float(input("Sisesta ringi raadiusi pikkus => "))  
    if r > 0:
        print("Õigesti sisestatud number")
        d = 2 * r  
        print("Ringi läbimõõt", d)  
        S = pi * r**2  
        print("Ringi pindala", round(S, 2))
        C = 2 * pi * r  
        print("Ringjoone pikkus", round(C, 2))  
    else:
        print("Kirjutage andmed õigesti")
except ValueError:
    print("Valed andmed")

