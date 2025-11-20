super_lig = {"Galatasaray":"63 Puan" , "Fenerbahçe":"69 Puan", "Beşiktaş":"44 Puan"}

team = input("Lütfen Puanını öğrenmek istediğiniz takımın ismini yazınız :").capitalize()

print(team,":",super_lig.get(team,"Belirttiğiniz takım Süper Lig Kümesinde Değil !"))