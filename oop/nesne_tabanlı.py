class galeri:
    araca_ismi = "Reanult"
    km_degeri = 300000
    renk = "Lacivert"

    def araba_özellikleri(self):
         print("-"*40)
         print("SEFANIN GALERİSİNE HOŞGELDİNİZ")
         
         print(f"ARAÇ İSMİ : {self.araca_ismi}\nKM DEĞERİ : {self.km_degeri}\n ARAÇ RENGİ : {self.renk}")
         print("-"*40)

class galeri2:
     arac_ismi = "TOROS"
     KM = 900000
     renk="BEYAZ"

     def araba_özellikleri(self):
          print("-"*40)
          print("ZAFERİN GALERİSİNE HOŞGELDİNİZ")
          
          print(f"ARAÇ İSMİ : {self.arac_ismi}\nKM DEĞERİ : {self.KM}\nARAÇ RENGİ : {self.renk}")        
          print("-"*40)


sefanın_galerisi = galeri()
sefanın_galerisi.araba_özellikleri()
zaferin_galerisi = galeri2()
zaferin_galerisi.araba_özellikleri()
