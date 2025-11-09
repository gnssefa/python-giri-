# " read " komutu dosyayı direkt okur
# " readline " komutu dosyanın içeriğini satır satır okur
# " readlines " komutu dosyanın içeriğini array şeklinde sunar

import codecs

# with codecs.open("deneme.txt","r", encoding="utf-8") as dosya:
#     a = dosya.readlines()
#     print(a)
     
#      # dosyanın içerisine veri yazdırma ( sonuna yazılır)

# import codecs

# with codecs.open("deneme.txt","a", encoding="utf-8") as dosya:
#     a = dosya.write("\n3.Kel mahmut")
#     print(a)

    # doyanın başına veri yazdırma 

# with codecs.open("deneme.txt","r+", encoding="utf-8") as dosya:
#     isimler = dosya.read()
#     dosya.seek(0)
#     isimler = "Müvekkil\nSEFAAAAA\n11" + isimler
#     dosya.write(isimler)
    
with codecs.open("deneme.txt","r+", encoding="utf-8") as dosya:
    isimler = dosya.readlines()
    isimler.insert(16,"3060 TI MASAÜSTÜ PC\n")
    dosya.seek(0)
    dosya.writelines(isimler)