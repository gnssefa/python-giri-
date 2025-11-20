import random
import time
kişiler = list()
def kullanıcılar_ekle(x):
    print("-"*30)
    kullanıcı_al = input("Eklemek istediğiniz kişiyi yazınız :").upper()
    kişiler.append(kullanıcı_al)
    print(f"{kullanıcı_al} Kişisi Listeye Eklendi")
    print("-"*30)
    input("Devam Etmek İçin LÜtfen Enter'e Basınız...")

def kullanıcıları_gör(x):
    say =1
    print("-"*30)
    for i in x :
        print(str(say)+". Kişi Adı :",i)
        say+=1
    print("-"*30) 

def salla_liste(x):
    say = 1
    print("-"*30)
    print("---- Yeni Düzen ----")
    random.shuffle(kişiler)
    for i in x:
         
        print(str(say)+". Kişi",i)
        say+=1
    print("-"*30)

def kullanıcı_seç(x):
    say = 1
    print("-"*30)
    kaç_kişi = int(input("Kaç Kişi Seçilsin ? :"))
    rastgele  = random.sample(x,kaç_kişi)
    for i in rastgele:
        print("-"*30)
        print(str(say)+". Seçilen Kişi :",i)
        time.sleep(1)
        say+=1
    print("-"*30)

    
while True:
    print("*-*-*  ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ *-*-*")
    print(" -- Lütfen Yapmak İstediğiniz İşlemi Belirtiniz --")
    seçenekler = int(input("1 -> Kişi Ekle ;\n2 -> Kişileri Gör ;\n3 -> Listeyi Karıştır ;\n4 -> Rastgele Kişi Seç ;\n-> Yapılacak işlem :"))

    if seçenekler == 1:
        kullanıcılar_ekle(kişiler)
    elif seçenekler==2:
        kullanıcıları_gör(kişiler)
    elif seçenekler == 3:
        salla_liste(kişiler)
    elif seçenekler == 4:
        kullanıcı_seç(kişiler)
    else :
        print("Lütfen Geçerli İşlem giriniz ..")   