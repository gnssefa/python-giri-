import customtkinter as ctk
from tkinter import messagebox
import random
import time
import threading

# Tema ayarları
ctk.set_appearance_mode("dark")  # "light" da deneyebilirsin
ctk.set_default_color_theme("green")  # "blue", "dark-blue", "green" gibi temalar var

kişiler = []

# --- Fonksiyonlar ---
def kullanıcı_ekle():
    kişi = entry_kisi.get().strip().upper()
    if kişi:
        kişiler.append(kişi)
        entry_kisi.delete(0, ctk.END)
        güncelle_liste()
        messagebox.showinfo("Başarılı", f"{kişi} listeye eklendi!")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir isim girin!")

def güncelle_liste():
    listbox.configure(state="normal")
    listbox.delete("1.0", ctk.END)
    for idx, kişi in enumerate(kişiler, start=1):
        listbox.insert(ctk.END, f"{idx}. {kişi}\n")
    listbox.configure(state="disabled")

def liste_karıştır():
    if not kişiler:
        messagebox.showwarning("Uyarı", "Liste boş!")
        return
    random.shuffle(kişiler)
    güncelle_liste()
    messagebox.showinfo("Karıştırıldı", "Liste karıştırıldı!")

def rastgele_seç():
    if not kişiler:
        messagebox.showwarning("Uyarı", "Liste boş!")
        return
    try:
        adet = int(entry_sayi.get())
        if adet > len(kişiler) or adet <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin!")
        return

    seçilenler = random.sample(kişiler, adet)

    def göster():
        sonuç_pencere = ctk.CTkToplevel(root)
        sonuç_pencere.title("Seçilen Kişiler 🎉")
        sonuç_pencere.geometry("350x400")
        lbl = ctk.CTkLabel(sonuç_pencere, text="🎯 Rastgele Seçilenler", font=("Arial", 18, "bold"))
        lbl.pack(pady=15)
        for s in seçilenler:
            ctk.CTkLabel(sonuç_pencere, text=s, font=("Arial", 14)).pack(pady=5)
            sonuç_pencere.update()
            time.sleep(0.8)

    threading.Thread(target=göster).start()

# --- Arayüz Tasarımı ---
root = ctk.CTk()
root.title("🎲 Çekiliş Uygulaması")
root.geometry("450x600")

# Başlık
ctk.CTkLabel(root, text="ÇEKİLİŞ UYGULAMASI", font=("Arial", 24, "bold")).pack(pady=15)

# Kişi Ekleme Alanı
frame_ekle = ctk.CTkFrame(root, corner_radius=15)
frame_ekle.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_ekle, text="Kişi Ekle:", font=("Arial", 14)).pack(pady=5)
entry_kisi = ctk.CTkEntry(frame_ekle, placeholder_text="İsim giriniz...", width=250)
entry_kisi.pack(pady=5)
ctk.CTkButton(frame_ekle, text="Listeye Ekle", corner_radius=20, command=kullanıcı_ekle).pack(pady=10)

# Liste Alanı
frame_liste = ctk.CTkFrame(root, corner_radius=15)
frame_liste.pack(pady=10, padx=20, fill="both", expand=True)
ctk.CTkLabel(frame_liste, text="Kişiler Listesi:", font=("Arial", 14, "bold")).pack(pady=5)
listbox = ctk.CTkTextbox(frame_liste, width=300, height=200, corner_radius=15)
listbox.pack(pady=10)
listbox.configure(state="disabled")

ctk.CTkButton(root, text="Listeyi Karıştır 🔀", corner_radius=20, command=liste_karıştır).pack(pady=10)

# Rastgele Seçim Alanı
frame_sec = ctk.CTkFrame(root, corner_radius=15)
frame_sec.pack(pady=10, padx=20, fill="x")
ctk.CTkLabel(frame_sec, text="Kaç kişi seçilsin?", font=("Arial", 14)).pack(pady=5)
entry_sayi = ctk.CTkEntry(frame_sec, width=80)
entry_sayi.pack(pady=5)
ctk.CTkButton(frame_sec, text="Rastgele Seç 🎯", corner_radius=20, command=rastgele_seç).pack(pady=10)

# Çıkış Butonu
ctk.CTkButton(root, text="Çıkış 🚪", fg_color="#d9534f", hover_color="#c9302c", corner_radius=20, command=root.destroy).pack(pady=20)

root.mainloop()
