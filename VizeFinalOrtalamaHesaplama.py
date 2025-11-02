vize = int(input("Vize Notunuzu Giriniz :"))
final = int(input("Final Notunuzu Giriniz :"))

ortalama = (vize*0.4)+(final*0.6)

print(f"Vize Notunuz : {vize}\nFinal Notuznuz : {final}\nOrtalamanız : {ortalama}")

if ortalama<50:
    print("Kaldınız")
else :
    print("Geçtiniz")
