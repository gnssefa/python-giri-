#------ 1 -----#
sözlük = {"Apple":"Elma","Banana":"Muz","Phone":"Telefon"}
    
print(sözlük["Phone"]) 

#------2------#
sözlük = {"Apple":"Elma","Banana":"Muz","Phone":"Telefon"}

for isim,deger in sözlük.items():
    print(isim,":",deger)
