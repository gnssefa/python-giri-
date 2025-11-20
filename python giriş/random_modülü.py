# Random modülü 0-1 arasında sayı üretir
# import random

# print(dir(random))

# " uniform " modülü random modülünün parametre alınabilir halidir 

import random

a = random.uniform(1.5,2.5)

print(a)

# " randint " modülü belirtilern değerler arasında tam sayı verir

import random

b = random.randint(20,80)

print(b)

# " cohise " modülü belirtilen liste vb. içerisinden veri seçer 

import random

liste = [ "Sefa","Güneş","Muğla","Yazılım","22"]

L =random.choice(liste)

print(L)

# " shuffle " modülü belirtilen liste içerisindeki verilerin yerlerini karıştırır

import random

listeler = [ "Sefa","Güneş","Muğla","Yazılım","22"]

random.shuffle(listeler)

for i in listeler :
    print(i)

# " sample " modülü belirtilern liste içerisindeki verilerden istenilen kadar numune verir

listeler89 = [ "Sefa","Güneş","Muğla","Yazılım","22"]

u =random.sample(listeler89,2)
print(u)