eşit = 5 == 5

print(eşit)

eşit = 5 == 6

print(eşit)

### Eşit ###

pw = 14532020

kullanıcı_pw =int(input("Şifrenizi Giriniz :"))

kontrol = pw == kullanıcı_pw

print(kontrol)

### Eşit Değil ###

eşit_değil = 5 != 5

print(eşit_değil)

sg = 1453
zg = 2020

kontrol1 = sg != zg
print(kontrol1)

### Küçük mü ? ### 

yaş = 22

kontrol2 = yaş<23
print(kontrol2)

### Küçük ve Eşittir ###

yaş = 22

kontrol3 = yaş<=23
print(kontrol3)

### Büyük mü ? ###

yaş = 22

kontrol4 = yaş>23
print(kontrol4)

### Büyük ve Eşittir ###

yaş = 22

kontrol5 = yaş>=23
print(kontrol5)

### lenght ###

liste = [1,2,3,4]
liste2 = [1,2,3,4,5]

kontrol_liste = len(liste) > len(liste2)
print(kontrol_liste)

# AND  == &&   OR == ||

kullanıcı_name = "sefagunes"
kullanıcı_sifre = 123456

kullanıcının_name = input("Lütfen Kullanıcı Adınızı Giriniz :")
kullanıcının_sifre = int(input("Lütfen Şifrenizi Giriniz :"))

kontrol_asaması = kullanıcı_name==kullanıcının_name and kullanıcı_sifre==kullanıcının_sifre

print(kontrol_asaması)