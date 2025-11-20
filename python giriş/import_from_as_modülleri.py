#|||||||||||||||||||||||||||||||||||
# Farklı modülden fonksiyon çağırma
#|||||||||||||||||||||||||||||||||||

import tel_rehberi

tel_rehberi.directory_add()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Farklı modülden çağırılan fonksiyonun ismini farklı kaydetme işlemi
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

import karşılaştırma_operatörleri as ko

ko.eşit()

#|||||||||||||||||||||||||||||||||||||||||||||||||||||
# Farklı modülden SADECE BELİRTİLEN fonksiyon çağırma
#|||||||||||||||||||||||||||||||||||||||||||||||||||||

from karşılaştırma_operatörleri import eşit_değil

eşit_değil()
