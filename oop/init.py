class okul :
    def __init__(self,sube,öğretmen,bölüm,mevcut):
        self.sube = sube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut

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

class müdür(okul):
    print("- Y Ö N E T İ C İ  --  P A N E L İ -")
    def __init__(self, sube, öğretmen, bölüm, mevcut,kıdem):
        super().__init__(sube, öğretmen, bölüm, mevcut)
        self.kıdem =kıdem
    def bilgileri_göster(self):
        print("-"*30)
        print("YÖNETİCİ PANELİ")
        print(f"Şube ismi : {self.sube}\nŞube öğretmeni : {self.öğretmen}\nBölüm adı : {self.bölüm}\nSınıf mevcudu : {self.mevcut}\nKıdem Bilgisi : {self.kıdem}")
        print("-"*30)


yönetici = müdür("11-A","SEFA","YAZILIM","22","BAŞKAN YARD.")



yönetici.bilgileri_göster()























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