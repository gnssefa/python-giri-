def su_hesapla(kilo):
     e_hesapla = kilo*0.04
     k_hesapla = kilo*0.03

     cinsiyet = input("Lütfen cinsiyetnizi belirtiniz ; ERKEK / KADIN :").lower()
     
     if cinsiyet == "erkek":
          print("-"*30)
          print("Cinsiyetiniz :",cinsiyet)
          print(e_hesapla,"Litre su içmelisiniz")
          print("-"*30)
    
     elif not cinsiyet:
          print("Lütfen cinsiyetinizi belirtiniz !!")  

     elif cinsiyet == "kadın" :
          print("*"*30)

          print("Cinsiyetiniz :",cinsiyet)
          print(k_hesapla,"Litre su içmelisiniz")
          print("*"*30) 


kilo_al = int(input("Lütfen kilonuzu giriniz :"))

su_hesapla(kilo_al)






          