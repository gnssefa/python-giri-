import random
import time

users = list()

def add_user(x):
    print("-"*30)
    print("Kullanıcı ekleme ekranına hoşgeldiniz")

    add = input("Lütfen Eklenecek Olan Kullanıcıyı Yazınız :")
    users.append(add)
    print(f"{add} adlı kişi listeye eklendi !")
    input("Devam Etmek İçin Enter'e Basınız ...")


def see_users(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı adı :",i)
        say+=1
        input("Devam Etmek İçin Enter'e Basınız ...")
    print("-"*30)
    

def ch0ise(x):
    print("-"*30)
    say = 1
    choise_user = int(input("Kaç kişi seçilmesini istiyorsunuz ? :"))
    random_choise = random.sample(x,choise_user)

    for i in random_choise:
        print(str(say)+"-Kullanıcı adı :",i)
        say+=1
        print("Sıradaki Kişi Belirleniyor ..")
        time.sleep(3)
    print("-"*30)
    input("Devam Etmek İçin Enter'e Basınız ...")
        
def salla(x):
    print("-"*30)
    say = 1
    random.shuffle(x)
    for i in x :
         print(str(say)+"-Kullanıcı adı :",i)
         say+=1
         input("Devam Etmek İçin Enter'e Basınız ...")
    print("-"*30) 

while True:

    print("*-*-* Çekiliş Uygulamasına Hoşgeldiniz *-*-*")
    options = int(input("1-Kullanıcı Ekle ;\n2-Kullanıcı Gör ;\n3-Kullanıcıları Karıştır ;\n4-Rastgele Seç ;\n"))

    if options == 1:
        add_user(users)
    elif options == 2:
        see_users(users)
    elif options == 3:
        salla(users)
    elif options ==4:
        ch0ise(users)
    else :
        print("-"*30)
        print("! Lütfen Uygun Bir Tercih Yapınız !")
        print("-"*30)
        
