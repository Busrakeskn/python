from human import Human


faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
#print(int(krediAdi))   => inte çevirilmek isteniyo ama int bir değer yok.
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))     
# pythonda kullanıcıdan alınan input default olarak str değerine sahip olur.
print(type(vade))
vade = vade + 12

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayısı}" .format(vadeSayısı=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade:{vade}")

isim = "Büşra"
metin = "Merhaba {name}" .format(name = isim)
print(metin)


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)



# Listeler
# Döngüler
# Fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]     # Liste elemanlarının tipi birbirinden farklı olabilir.
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

print(len(krediler))   # lenght
# print(krediler[3]) =  hata verir.

krediler.append("Özel Kredi")   # Listenin sonuna elman ekler.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)    # Listeden elaman siler. İndex verilmezse default olarak -1. yani son indexi siler.
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi")  #listeteden eleman siler.(Bulduğu ilk elemanı.)
print(krediler) 

krediler.extend(["Y Kredisi", "Z Kredisi"]) # Birden fazla eleman ekler.
print(krediler)


# for döngüsü
# i=0 i<0 i<10

for i in range(10):
    print(i)        # Aksi belirtilmedikçe default olarak sıfırdan başlar.

print("*******************")

for i in range(5,10):
    print(i)
print("****************")

for i in range(0,51,10):  # range(başlangıç elemanı, varış elemanı, karar elemanı)
    print(i)
print("***************")

#for i in range(0.1, 0.5):   => Hata verir.
#    print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("****************")
for i in range(len(krediler)):
    print(krediler[i])
print("*************")

# While döngüsü

# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i +=1
print("y")
print("***********************")

while True:
    print("X")
    break     # Döngüden çıkarır.
print("*****************")

i = 0
while i < len(krediler):
    print(krediler[i])
    i +=1
print("*******************")

i = 0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break


# Fonksiyonlar 

fiyat = 100
indirim = 20
# definition  define 
def calculate():
    print(100-20)

def calculatewithparams(fiyat,indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculatewithparams(50,10)
sayHello("Büşra")


def calculateAndReturn(price, discount):
    return price - discount

yeniFİyat = calculateAndReturn(200,50)
print(yeniFİyat)


def calculatePrice(price, discount):
    print((price - discount))

def calculatePriceAndReturn(price, discount):
    return price - discount

print("****************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(fonk1)
print(fonk2)
print("*********************")


# Sınıflar => Classlar

# instance => örnek

human1 = Human("Enes")
human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)