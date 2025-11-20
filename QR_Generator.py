import tkinter as tk
from tkinter import filedialog

import pyqrcode
from pyqrcode import QRCode


#temel kodlar

def qr_olustur():
    url = url_girdi.get()

    if url:
        qr_url = pyqrcode.create(url)
        file_way = filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG DOSYALARI","*.svg")])

        if file_way:
            qr_url.svg(file_way, scale=8)
            durum_etiketi.config(text="QR Kodu Oluşturuldu ve Kaydedildi")

# Tasarım

app_window =tk.Tk()
app_window.title("Sefa'nın QR Kod Oluşturucusu")
app_window.configure(bg="green")


etiket = tk.Label(app_window,text="URL'yi Girin")
url_girdi = tk.Entry(app_window,width=40)
create_button = tk.Button(app_window,text="QR KODU OLUŞTUR",command=qr_olustur)
durum_etiketi =tk.Label(app_window,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
create_button.grid(row=1,column=0,columnspan=2 ,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)














app_window.mainloop()


