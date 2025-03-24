def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."
    for i in range(2, sayi):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."
        
    return f"{sayi} bir asal sayıdır."

sayi = int(input("Bir sayı giriniz: "))
print(asal_mi(sayi))