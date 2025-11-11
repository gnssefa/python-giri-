import tkinter as tk
from tkinter import filedialog
import pyqrcode

def qr_olustur():
    url = url_girdi.get()
    if url:
        qr_url = pyqrcode.create(url)
        file_way = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG DOSYALARI", "*.svg")])
        if file_way:
            qr_url.svg(file_way, scale=8)
            durum_etiketi.config(text="QR Kodu Oluşturuldu ve Kaydedildi")

def kapat():
    app_window.destroy()

# Ana pencere
app_window = tk.Tk()
app_window.overrideredirect(True)  # Sistem başlık çubuğunu kaldırır
app_window.geometry("400x200")
app_window.configure(bg="green")

# Özel başlık çubuğu
baslik_cubugu = tk.Frame(app_window, bg="red", relief="raised", bd=0)
baslik_cubugu.pack(fill=tk.X)

baslik_yazi = tk.Label(baslik_cubugu, text="Sefa'nın QR Kod Oluşturucusu", bg="red", fg="white", font=("Arial", 10, "bold"))
baslik_yazi.pack(side=tk.LEFT, padx=10, pady=3)

kapat_butonu = tk.Button(baslik_cubugu, text="X", command=kapat, bg="black", fg="white", bd=0, padx=5, pady=2)
kapat_butonu.pack(side=tk.RIGHT, padx=5, pady=2)

# Taşınabilirlik için
def move_window(event):
    app_window.geometry(f"+{event.x_root}+{event.y_root}")

baslik_cubugu.bind("<B1-Motion>", move_window)

# Uygulama içeriği
etiket = tk.Label(app_window, text="URL'yi Girin", bg="green", fg="white")
url_girdi = tk.Entry(app_window, width=40)
create_button = tk.Button(app_window, text="QR KODU OLUŞTUR", command=qr_olustur)
durum_etiketi = tk.Label(app_window, text="", bg="green", fg="white")

etiket.pack(pady=10)
url_girdi.pack(pady=5)
create_button.pack(pady=10)
durum_etiketi.pack(pady=5)

app_window.mainloop()
