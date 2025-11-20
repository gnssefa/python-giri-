#def topla():
 #   a = int(input("Lütfen ilk sayınızı giriniz :"))
  #  b = int(input("Lütfen ikinci sayınızı giriniz :"))

   # toplam = a+b
   # print(toplam)


#topla()


def kullanıcı_bilgileri(ad,soyad,yaş,meslek):
    print("*"*30)
    print(f"Adınız :{ad}\nSoyadınız :{soyad}\nYaşınız :{yaş}\nMesleğiniz :{meslek}")
    print("*"*30)
    
    
adınız = input("Lütfen Adınızı Giriniz :")
soyadınız = input("Lütfen Soyadınızı Giriniz :")
yaşınız = int(input("Lütfen Yaşınızı Giriniz :"))
mesleğiniz = input("Lütfen Mesleğinizi Giriniz :")

kullanıcı_bilgileri(adınız,soyadınız,yaşınız,mesleğiniz)
      
    