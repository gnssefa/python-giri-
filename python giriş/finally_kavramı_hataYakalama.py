import time
try:
  sayı = int(input("Lütfen Rakam Giriniz :"))
  sayı2 = int(input("Lütfen 2. Rakamı Giriniz :"))

  topla = sayı+sayı2

  print(topla)

except (ZeroDivisionError,ValueError):
  print("Lütfen Girilen Verilerin ' SADECE RAKAM ' OLDUĞUNDAN EMİN OLUNUZ ")

finally:
  sayaç = 5

  for i in range(5):
    print("Geri Sayım :",sayaç)
    time.sleep(1)
    sayaç-=1

