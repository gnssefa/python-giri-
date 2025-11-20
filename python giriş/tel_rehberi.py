# tel_rehberi = dict()
# while True:
#     def add_number(x):
#         print("* Rehber Düzenleme Ekranına Hoşgeldiniz *")
#         take_name = input("Lütfen Kaydedilecek Kişinin İsmini Giriniz :")
#         take_num = input("Lütfen Kişinin Numarasını Giriniz :")

#         if take_num.isdigit():
#             if len(take_num)==11:
#              pass
#             else :
#              print("Lütfen 11 Haneli numara girdiğinizden emin olunuz !!!")
#         else:
#              print("Lütfen sadece rakam giriniz")
#              break        

#         x = tel_rehberi.setdefault(take_name,take_num)
#         print(f"{take_name} adlı kişi telefon rehberine eklendi")


#     add_number(tel_rehberi)


# tel_rehberi = dict()

# def add_number():
#     print("* Rehber Düzenleme Ekranına Hoşgeldiniz *")
#     take_name = input("Lütfen kaydedilecek kişinin ismini giriniz: ")
#     take_num = input("Lütfen kişinin numarasını giriniz: ")

#     # Rakam kontrolü
#     if not take_num.isdigit():
#         print(" Lütfen sadece rakam giriniz!")
#         return  # fonksiyondan çık

#     # Uzunluk kontrolü
#     if len(take_num) != 11:
#         print(" Lütfen 11 haneli numara girdiğinizden emin olunuz!")
#         return

#     # Kaydetme işlemi
#     tel_rehberi[take_name] = take_num
#     take_name= take_name.capitalize()
#     print(f" {take_name} adlı kişi telefon rehberine eklendi.")

# # Ana döngü
# while True:
#     add_number()
#     devam = input("Başka kişi eklemek ister misiniz? (E/H): ").strip().lower()
#     if devam != 'e':
#         break

# print("\n--- Rehber ---")
# for isim, numara in tel_rehberi.items():
#     print(f"{isim}: {numara}")
#-------------------------------------------
phone_directory = dict()


#İşlevsel Fonksiyonlar Başlangıç
#Numara ekleme 
def directory_add():
    take_name = input("Lütfen isim yazınız :").lower()
    take_num = input("Lütfen numara yazınız :").lower()

    phone_directory.setdefault(take_name,take_num)
    print(f"{take_name} adlı kişi rehbere eklendi ! ")
 
 # Numaraları Listeleme
def directory_printer():
    print("--- GÜNCEL REHBER ---")

    for i,j in phone_directory.items():
        print(i,":",j)

# Numara silme
def rmv_numbers(): 
        
        remove_people = input("Lütfen silmek istediğiniz kişiyi belirtiniz :")
        
        if remove_people not in phone_directory :
            print("\nRehberinizde bu kişi bulunmamaktadır !!\n","*"*30)
            
        else :
            trust = input("Silme işlemini oyalıyormusun ?"f"Silinecek olan kişi :{remove_people}  :  E/H ? :").upper()
            if trust == "E":
                phone_directory.pop(remove_people) 
                print("Silme işlemi başarılı oldu !")
                
            else :
                print("Silme işleminden vazgeçildi !")

# Kişi bilgisi düzenleme
 
def nums_update():
    updatelenecek = input("Değişkirmek istediğiniz kişinin adını giriniz :").lower()
    if updatelenecek not in phone_directory:
        print("Bu kişi rehberinizde bulunmamaktadır !!")
        return
    else :
        choose=input("İsim değiştirmek için 1'i tuşlayınız\nNumara değiştirmek için 2'yi tuşlayınız \nHem isim hem numara değiştirmek için 3'ü tuşlayınız")
        if choose == "1" :
            new_name = input("Lütfen kişinin yeni ismini giriniz :").lower()
            for i,j in phone_directory.items():
                if i == updatelenecek:
                    phone_directory.setdefault(new_name,j)
                    phone_directory.pop(updatelenecek)
                    break
        elif choose == "2":
            new_num = input("Lütfen yeni numarayı giriniz :")
            for i,j in phone_directory.items():
                if i==updatelenecek:
                    phone_directory.update({updatelenecek:new_num})
                    break
        elif choose =="3":
            new_name = input("Lütfen yeni ismi giriniz :").lower()
            new_num = input("Lütfen yeni ismi giriniz :").lower()

            for i,j in phone_directory.items():
                if i == updatelenecek:
                    phone_directory.setdefault(new_name,new_num)
                    phone_directory.pop(updatelenecek)
                    break



       
       



                
        
             
           
#İşlevsel fonskiyonlar bitişi


while True :
    print("*"*30)
    y = input("Numara eklemek istiyorsanız : 1'i tuşlayın\n Numara Silmek istiyorsan 2'yi tuşla\n Rehberi görmek isterseniz 3'ü tuşlayın\nKişi bilgisi düzenlemek istiyorsan 9'u tuşla\nİşlem yapmak istemiyorsanız 4'ü tuşlayınız\n --Ne yapmak istersiniz(1,2,3,4): ")
    if y == "1":
        print("Ekleme işlemine yönlendirildiniz")
        directory_add()
        directory_printer()
    elif y=="2":
        rmv_numbers()
    elif y == "3":
        directory_printer()
    elif y == "9":
        nums_update()

    elif y == "4":
        print("İşlem sonlandırıldı !")
        break
    else:
        print("*"*30,"\nYanlış karakter girdiniz ! ")
    
        

                  
           
           
                     

    




    
    
