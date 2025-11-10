import sqlite3
while True:
    # try:
        db = sqlite3.connect("Kitaplar.db")

        yetki = db.cursor()

        kitap_adı = input("Lütfen Kitap Adını Giriniz :").capitalize()
        kitap_Sayfa = int(input("Lütfen Kitabın Sayfa Sayısını Giriniz :"))
        kitap_yılı = int(input("Lütfen Kitabınn Yayımlanma Yılını Giriniz :"))

        yetki.execute("CREATE TABLE IF NOT EXISTS  sefa(isim,sayfa sayısı,kitap çıkış yılı)")
        yetki.execute(f'INSERT INTO sefa VALUES("{kitap_adı}","{kitap_Sayfa}","{kitap_yılı}")')
        yetki.execute("SELECT *FROM sefa WHERE kitap='2003'")

        yazdır =yetki.fetchall()

        for i in yazdır:
                print(i)


        # for i in yazdır:
        #     print("-"*30)
        #     print(f"Kitap adı : {i[0]}\nSayfa sayısı : {i[1]}\nYayım tarihi : {i[2]}")

        # db.commit()
        # print("-"*30)
        # print(f"Eklenen Kitap : {kitap_adı}")
        # print("-"*30)
        # db.close()
    # except ValueError :
    #     print("LÜTFEN RAKAM GİRİNİZ")
