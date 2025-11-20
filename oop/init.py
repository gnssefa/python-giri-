class okul :
    def __init__(self,sube,öğretmen,bölüm,maaş,mevcut):
        self.sube = sube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut
        self.maaş = maaş

    def bilgileri_göster(self):
        print("-"*30)
        print("SINIF BİLGİLERİ")
        print(f"Şube ismi : {self.sube}\nŞube öğretmeni : {self.öğretmen}\nBölüm adı : {self.bölüm}\nSınıf mevcudu : {self.mevcut}\n")
        print("-"*30)

    def branş_değiştir(self):
        print("-"*35)
        print("Branş değiştirme işlemine başlanıyor ...")
        print("-"*35)
        yeni_branş = input("Lütfen yeni branşı belirtiniz : ")
        self.bölüm = yeni_branş
        print("-"*30)
        print(f" Yeni Branş : {yeni_branş}")
        print("-"*30)
        print(" - - - GÜNCEL SINIF BİLGİLERİ - - -")
        print(f"Şube ismi : {self.sube}\nŞube öğretmeni : {self.öğretmen}\nBölüm adı : {self.bölüm}\nSınıf mevcudu : {self.mevcut}\n")
    def maaş_göster(self):
        print("-"*30)
        print(f"{self.öğretmen}' adlı öğretmenin maaşı : {self.maaş} ₺")
        print("-"*30)

class müdür(okul):
    print("- Y Ö N E T İ C İ  --  P A N E L İ -")
    def __init__(self, sube, öğretmen, bölüm, mevcut,kıdem,maaş):
        super().__init__(sube, öğretmen, bölüm, mevcut,maaş)
        self.kıdem =kıdem
    def bilgileri_göster(self):
        print("-"*30)
        print("YÖNETİCİ PANELİ")
        print(f"Şube ismi : {self.sube}\nŞube öğretmeni : {self.öğretmen}\nBölüm adı : {self.bölüm}\nSınıf mevcudu : {self.mevcut}\nKıdem Bilgisi : {self.kıdem}")
        print("-"*30)

    def zam_yap(self):
        print(f"Zam Ekranına Hoşgeldiniz Sayın : {self.öğretmen}")
        zam_miktarı = int(input("Lütfen Zam Mıktarını TL Cinsinden Yazınız :"))
        self.maaş = int(self.maaş) + int(zam_miktarı)
        print("-"*30)
        print(f"{self.öğretmen}' adlı öğretmene {zam_miktarı} ₺ Zam yapıldı ..")
        print(f"{self.öğretmen} ' adlı öğretmenin güncel maaşı : {self.maaş}")
        print("-"*30)


sınıf_adı =input("Lütfen Şube Numarası Giriniz :")
ögretmen_bilgisi = input("Lütfen Öğretmen Adı Giriniz :")
bölüm_al = input("Lütfen Bölüm İsmi Giriniz :")
mevcut = int(input("Lütfen Sınıf Mevcutunu Giriniz :"))
maaş_gir = int(input("Lütfen Maaş Bilgisi Giriniz :"))
print(" -- BU ALANI SADECE YÖNETİCİ İSENİZ DOLDURUNUZ --")

kıdem_al = input("Lütfen Kıdem Bilgisi Giriniz :")
if not kıdem_al:
    print(" -- Öğretmen Modundasınız --")

sınıf_olustur = ("Lütfen Oluşturulacak Olan Sınıfın İsmini Giriniz :")

while True:
    if not kıdem_al:
        sınıf_olustur = okul(sınıf_adı,ögretmen_bilgisi,bölüm_al,mevcut,maaş_gir)
        soru = input("1-> Bilgileri Göster\n2->Branş Değiştir\n3->Maaş Bilgisi Göster\n--> Seçilen işlem : ")
        if soru == "1":
            sınıf_olustur.bilgileri_göster()
            input("Devam etmek için Enter'e basınız !")
        elif soru == "2":
            sınıf_olustur.branş_değiştir()
            input("Devam etmek için Enter'e basınız !")
        elif soru == "3":
            sınıf_olustur.maaş_göster()
            input("Devam etmek için Enter'e basınız !")
        else:
            print("Lütfen geçerli işlem giriniz  !!")
            input("Devam etmek için Enter'e basınız !")
    else:
        print("-"*30)
        print("YÖNETİCİ MODUNDASINIZ")
        print("-"*30)
         
        sınıf_olustur = müdür(sınıf_adı,ögretmen_bilgisi,bölüm_al,mevcut,maaş_gir,kıdem_al,)
        soru2 = input("1-> Bilgileri Göster\n2-> Zam Yap\n-->Seçilen İşlem : ")
        if soru2 == "1":
            sınıf_olustur.bilgileri_göster()
            input("Devam etmek için Enter'e basınız !")
        elif soru2 =="2":
            sınıf_olustur.zam_yap()
            input("Devam etmek için Enter'e basınız !")
        else:
            print("-"*30)
            print("İŞLEM SONLANDIRILIYOR ..")
            print("-"*30)
            input("Devam etmek için Enter'e basınız !")























# while True:
#     sube_al = input("Lütfen Şube İsmini Giriniz : ")
#     ögretmen_al = input("Lütfen Öğretmen İsmi Belirtiniz :")
#     bölüm_al = input("Lütfen Branş Bilgisini Giriniz :")
#     mevcut_al = input("Lütfen Sınıf Mevcutunu Giriniz :")
#     sınıf_olustur = input("Lütfen Oluşturulacak olan sınıfın ismini belirleyiniz : ")
#     sınıf_olustur = okul(sube_al,ögretmen_al,bölüm_al,mevcut_al)

    
#     print("- - - HOŞGELDİNİZ - - -")
#     seçim = input("Branş Değiştirmek İçin 1'e basınız : ")
#     if seçim == "1":
#         sınıf_olustur.branş_değiştir()
#     else:
#         print("-"*30)
#         print("İŞLEM SONLANDIRILDI ...")
#         print("-"*30)
#         break 