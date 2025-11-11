import random


olasılıklar = [ "TAŞ" , "KAĞIT" , "MAKAS"]

isim = input("Lütfen isminizi Giriniz :").upper()
status = 2
while status > 1:
    def taskagıt():
        rnd = random.randint(0,2)
        pc_tahmin =  olasılıklar[rnd]
        print("-"*50)
        benim_tahminim = input("Senin Tahminin :").upper()
        print(f"Bilgisayarın Tahmini : {pc_tahmin}")
        
        
        if benim_tahminim == pc_tahmin:
            print("*"*50)
            print("BERABER BİTTİ")
            print("*"*50)
            return
        elif benim_tahminim == "TAŞ" or benim_tahminim == "KAĞIT" or benim_tahminim == "MAKAS":
            if pc_tahmin == "TAŞ":
                if benim_tahminim =="MAKAS":
                    print("-"*50)
                    print(f"Bilgisayar Kazandı ...<>...{isim} Kaybetti ")
                    print("-"*50)
                    return
                else:
                    print("-"*50)
                    print(f"{isim} Kazandı ...<>...Bilgisayar Kaybetti ")
                    print("-"*50)
                    return
            elif pc_tahmin == "KAĞIT":
                if benim_tahminim =="TAŞ":
                    print("-"*50)
                    print(f"Bilgisayar Kazandı ...<>...{isim} Kaybetti ")
                    print("-"*50)
                    return
                else:
                    print("-"*50)
                    print(f"{isim} Kazandı ...<>...Bilgisayar Kaybetti ")
                    print("-"*50)
                    return 
            elif pc_tahmin == "MAKAS":
                if benim_tahminim =="KAĞIT":
                    print("-"*50)
                    print(f"Bilgisayar Kazandı ...<>...{isim} Kaybetti ")
                    print("-"*50)
                    return
                else:
                    print("-"*50)
                    print(f"{isim} Kazandı ...<>...Bilgisayar Kaybetti ")
                    print("-"*50)
                    return 
        
        else:
            print("*"*50)
            print("GEÇERLİ BİR DEĞER GİR ")
            print("*"*50)
            return
            


    
    taskagıt() 
    
    while True:
        ask = input("DEVAM EDİLSİNMİ ?  E/H  :").upper()
        if ask == "E":
            taskagıt()
        elif ask == "H":
            print("-"*30)
            print("OYUN KAPATILIYOR ..")
            print("-"*30)
            status = -1 
            break
        else:
            print("Geçerli bir değer gir ")    
        
        
        
            


