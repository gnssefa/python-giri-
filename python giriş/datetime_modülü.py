from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL,"tr_TR")
a = datetime.now()
# a = a.year
tam_tarih = datetime.strftime(a,"%B")

# %a -> hafta gününün kısaltılmış adı
# %A -> hafta gününün tam adı
# %b -> ayın kısaltılmış adı
# %B -> ayın tam adı
# %c -> tam tarih ,saat ve zaman bilgisi
# %d -> sayı değerli bir karakter olarak gün
# %j -> belli bir tarihin , yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
# %m -> sayı değerli bir karakter dizisi olarak ay
print(tam_tarih)

# Local değiştirme


