# super_lig = {"Galatasaray":"63 Puan" , "Fenerbahçe":"79 Puan", "Beşiktaş":"95 Puan"}

# super_lig.setdefault("Trabzonspor","83 Puan")

# print(super_lig)

#**********************************************************************************************************#

super_lig1 = {"Galatasaray":"63 Puan" , "Fenerbahçe":"69 Puan", "Beşiktaş":"44 Puan"}

add_team=input("Lütfen Listeye Eklemek İstediğiniz Takımı Belirtiniz :")
add_point=int(input("Lütfen Belirttiğiniz Takımın Puanını Giriniz :"))

super_lig1.setdefault(add_team,add_point)
print(f"{add_point} Puan")
print("Eklenen Takımınız :",add_team)
print("Eklenen Puan durumu :",add_point)

print("Güncel liste durumu :",super_lig1)

#******************************************************************************************************


# super_lig1 = {"Galatasaray":"63 Puan" , "Fenerbahçe":"69 Puan", "Beşiktaş":"44 Puan"}
# s = 0 
# while s<=3:
#     if s==3:
#         print("Hakkın doldu")
#     add_team=input("Lütfen Listeye Eklemek İstediğiniz Takımı Belirtiniz :")
#     add_point=int(input("Lütfen Belirttiğiniz Takımın Puanını Giriniz :"))

#     super_lig1.setdefault(add_team,add_point)
#     s = s +1    
#     for i,j in super_lig1.items():
#         print(i,j)





#******************* Sözlük veri silme ********************#

# super_lig1 = {"Galatasaray":"63 Puan" , "Fenerbahçe":"69 Puan", "Beşiktaş":"44 Puan"}

# super_lig1.pop("Galatasaray")

# print(super_lig1)

