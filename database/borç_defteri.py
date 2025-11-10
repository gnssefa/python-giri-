import sqlite3

db = sqlite3.connect("Veresiye Defteri")
yetki = db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borc)")

while True:
    print("---- VERESİYE DEFTERİ EKRANINA HOŞGELDİN ---")
    print("--- Lütfen yapmak istediğiniz işlemin numarasını giriniz ---")
    sor = input("1 -> Borçlu kişi ekle ;\n2 -> Borçlu kişileri listele ;\n3 -> Borçlu kişi sil\n--> Seçilen işlem :")
    if sor == "1":
        isim_al = input("Lütfen borçlu kişinin ismini giriniz :").upper()
        borc_miktar = input("Lütfen kişinin borç miktarını giriniz :")
        yetki.execute(f"INSERT INTO kisiler VALUES ('{isim_al}','{borc_miktar}')")
        db.commit()
        print("-"*80)
        print(f"İşlem Tamamlandı , '{isim_al}' kişisi , {borc_miktar} ₺ borç ile deftere kayıt edildi ...")
        print("-"*80)
    elif sor == "2":
        print("*-*-*-*-* GÜNCEL KAYITLI BORÇLU KİŞİLER *-*-*-*-*")
        yetki.execute("SELECT *FROM kisiler")
        yazdır = yetki.fetchall()
        say = 1
        for i in yazdır:
            print(f" {say}. BORÇLU İSMİ : {i[0]} , BORÇ MİKTARI : {i[1]}₺")
            say+=1
    elif sor == "3":
        sil = input("Lütfen silmek istediğiniz kişinin ismini yazınız :")
        yetki.execute(f"DELETE FROM kisiler  WHERE isim = '{sil}'")
        db.commit()
        print("-"*30)
        print(f"Silinen kişi : {sil}")
        print("-"*30)
        
