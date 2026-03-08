import random

sayi = random.randint(1, 100)
tahmin_sayisi = 0

while True:
    tahmin = int(input("tahminin: "))
    tahmin_sayisi += 1
    
    if tahmin > sayi:
        print("tahminini düşür")
    elif tahmin < sayi:
        print("tahminini yükselt")
    else:
        print("Tahminin doğru, " + str(tahmin_sayisi) + " tahminde buldun!")
        break
