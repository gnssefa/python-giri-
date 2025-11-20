for i in range(3):
    sifre = input("Lütfen şifrenizi giriniz :")
    if not sifre:
        print("Bu alan boş bırakılamaz ..!")
    elif len(sifre) in range(3,8):
        print("Yeni şifreniz",sifre)
        break
        
    elif i == 2 :
        print("Şifrenizi 3 defa yanlış girdiniz . Lütfen 15 dakika bekleyip tekrar deneyiniz ..")

    else:
        print("Şifreniz 8 karakterden uzun ya da 3 karakterden kısa olamaz !!")
        