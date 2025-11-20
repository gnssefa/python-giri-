isim = "sefa güneş"
isim = isim.split()

print(isim[1])

tarih = "04/11/2025"
tarih = tarih.split("/")

print(tarih)
print(tarih[1])


#veri_al = input("Lütfen parçalanmasını istediğiniz cümleyi yazın :")

#for i in veri_al.split():
  #  print(i)


#veri_al = input("Lütfen parçalanmasını istediğiniz cümleyi yazın :")

#for i in veri_al:
 #   print(i)    

veri_al = input("Lütfen parçalanmasını istediğiniz cümleyi yazın :")

for i in veri_al.split():
    print(i[2] , end="")