# kullanıcıdan bir sayı alınacak , eğer kullanıcıdan alınan sayı 3e tam bölünüyorsa sayınız 3e tam bölünebiliyor . 
# 5e tam bölünüyor ise sayınız 5e bölünebiliyor , hem 3e hem 5e gölünebiliyorsa sayınızı 3,5 e bölünebiliyor. 

kullaici_sayi = int(input("Lütfen sayı giriniz :"))

if kullaici_sayi % 3 == 0 and kullaici_sayi % 5 == 0:
    print("Tebrikler sayınız '3 ve 5' e tam bölünebiliyor !!")

elif kullaici_sayi % 3 == 0 :
    print("Tebrikler sayınız 3'e tam bölünebiliyor !!")

elif kullaici_sayi % 5== 0:
    print("Tebrikler sayınız 5'e tam bölünebiliyor !!")    

else:
    print("Üzgünüm , sayınızı 3 ve 5 e tam bölünemiyor , lütfen rakam giriniz !!")
