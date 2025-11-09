import time
pw = "14532020"

sifre = input("Lütfen Şifrenizi giriniz :")
def cekilis():
  import codecs
  file_generator = input("Lütfen Oluşturmak İstediğiniz Dosyanın İsmi Belirtiniz :")

  file_new = file_generator + ".txt"

  file_index = input("Lütfen Dosyanın İçerisine Yazdırılacak Olan Veriyi Giriniz :")

  with codecs.open(file_new,"w",encoding="utf-8") as file:
        file.write(file_index+"\n")
        while True:
                quest = input(f"'{file_new}' adlı dosyanız oluşturuldu . Başka Veri Eklemek İster misiniz ?  E/H :").upper()
                
                if quest == "E":
                    open(file_new,"a")
                    new_index = input("Lütfen Yeni Verinizi Yazınız :")
                    new_index = "\n" + new_index
                    file.write(new_index)
                    
                    print("-/-"*10)
                    print("Verileriniz Güncellendi !..")
                    print("-/-"*10)
                elif quest == "H":
                    print("-/-"*10)
                    print("- - İşlem Sonlandırıldı --")
                    print("-/-"*10)
                    break
                elif quest!= "E" and "H" :
                    print("-!-"*30)
                    print("                               Lütfen Geçerli Cevap Veriniz !..")
                    print("-!-"*30)
        while True :
                quest2 = input("Oluşturulan Dosyanızı Görüntülemek İster misiniz ?  E/H :").upper()
                if quest2 == "E":
                        with open(file_new,"r",encoding="utf-8") as q2:
                         print(" --- Dosyanızın İçeriği ---")
                         print(q2.read())
                         print("-"*30)
                         break
                elif quest2 =="H":
                        print("-/-"*10)
                        print("- - İşlem Sonlandırıldı --")
                        print("-/-"*10)
                        break
                elif quest2!= "E" or "H" :
                        print("-!-"*30)
                        print("                               Lütfen Geçerli Cevap Veriniz !..")
                        print("-!-"*30)
if sifre ==pw :
        cekilis()
else:
      kalan_hak = 2
      
      print("!_!_! HATALI ŞİFRE !_!_!")
      time.sleep(1)
      while True :
                
                seç= input("Tekrar denemek istermisiniz ?  E/H :").upper()
                pww = input("Lütfen tekrar şifrenizi giriniz :")
                if seç == "E":
                   
                   if pww == pw :
                        cekilis()
                   else:
                         kalan_hak-=1
                         print(f"Kalan deneme hakkınız :{kalan_hak}")
                         
                         if kalan_hak == 0:
                               print("-"*30)
                               print("Çok fazla hatalı işlem yapıldı . Lütfen daha sonra tekrar deneyiniz !.. ")
                               print("-"*30)
                               print("UYGULAMA KAPATILIYOR")
                               print("Geri Sayım : 3")                               
                               time.sleep(1)
                               print("Geri Sayım : 2")
                               time.sleep(1)
                               print("Geri Sayım : 1")
                               time.sleep(1)


                                
                               
                               break
                         
        
                elif seç == "H":
                  break

                elif seç != "E" and "H":
                     print("Lütfen geçerli cevap giriniz !")
                

     
            
 