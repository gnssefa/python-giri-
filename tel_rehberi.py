tel_rehberi = dict()
while True:
    def add_number(x):
        print("*Rehber Düzenleme Ekranına Hoşgeldiniz")
        take_name = input("Lütfen Kaydedilecek Kişinin İsmini Giriniz :")
        take_num = input("Lütfen Kişinin Numarasını Giriniz :")

        # if take_num.isdigit():
        #     if len(take_num)==11:
        #      pass
        #     else :
        #      print("Lütfen 11 Haneli numara girdiğinizden emin olunuz !!!")
        # else:
        #      print("Lütfen sadece rakam giriniz")
        #      break        

        x = tel_rehberi.setdefault(take_name,take_num)
        print(f"{take_name} adlı kişi telefon rehberine eklendi")


    add_number(tel_rehberi)


