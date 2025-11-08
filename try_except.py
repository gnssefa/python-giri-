
try:
  sayı = int(input("Lütfen Rakam Giriniz :"))
  sayı2 = int(input("Lütfen 2. Rakamı Giriniz :"))

  böl = sayı/sayı2

  print(böl)

except (ZeroDivisionError,ValueError):
  print("Lütfen Girilen Verilerin ' SADECE RAKAM ' OLDUĞUNDAN EMİN OLUNUZ ")
