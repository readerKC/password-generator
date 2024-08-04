import random

karakter_deposu = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

kul_girdiuzunlugu = int(input("Parolanın uzunluğunu giriniz:"))

parolasaklama = ""

for i in range(uzunluk):
    karakter = random.choice(karakter_deposu)
    parola += karakter

print(parola)



