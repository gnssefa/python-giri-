import subprocess as sp
psw = "14532020"
user_pw = input("Lütfen Şifrenizi Giriniz :")

if user_pw == psw:


    while True :
        print("*-*-* Uygulama Kestirmelerine Hoşgeldiniz *-*-*")
        print("Lütfen Açmak istediğiniz Uygulamayı Seçiniz")

        seçim_yap = input("1-NotePad\n2-Hesap Makinası\n3-Tarayıcı\n4-Steam\n")

        if seçim_yap =="1":
            sp.call("notepad.exe")
        elif seçim_yap =="2":
            sp.call("calc.exe")
        elif seçim_yap =="3":
            sp.call("C:/Program Files/Google/Chrome/Application/chrome.exe")
        elif seçim_yap =="4":
            sp.call("C:/Program Files (x86)/Steam/steam.exe")
        else:
            print("Lütfen Geçerli İşlem Numarası Giriniz ")

else :
    print("Hatalı Şifre !")