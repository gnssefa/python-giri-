#sayı = 1

#while sayı<=15:
    
    #print(sayı)
    #sayı+=1 
     
                                ###         Örnek Çalışma       ###

db_ka = "admin"
db_ps = 123456

while True:

    kullanıcı_adı = input("Lütfen Kullanıcı Adnızı Giriniz :")
    kullanıcı_pw = int(input("Lütfen Şifrenizi Giriniz :"))

    if kullanıcı_adı == db_ka and kullanıcı_pw == db_ps :
        print("Kullanıcı bilgileri doğrulandı !")
        break

    elif kullanıcı_adı != db_ka and kullanıcı_pw == db_ps :
        print("Lütfen Kullanıcı Adınızı Kontrol Ediniz !!!")
        

    elif kullanıcı_pw == db_ka and kullanıcı_pw != db_ps :
        print("Lütfen Şifrenizi Konrtol Ediniz !!!")
        

    else :
        print("Kullanıcı adı Ve şifreniz yanlış . Lütfen 2 bilgiyi tekrar giriniz !!!")

        