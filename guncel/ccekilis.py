import customtkinter as ctk
from tkinter import messagebox
import random

# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

kişiler = []

# Fonksiyonlar
def kullanıcı_ekle():
    girdi = entry_kisi.get()
    kişi = girdi.strip()
    if kişi:
        kişiler.append(kişi.upper())
        entry_kisi.delete(0, ctk.END)
        güncelle_liste()
        messagebox.showinfo("Başarılı", f"{kişi.upper()} listeye eklendi!")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir isim girin!")

def kişi_sil():
    kişi = entry_kisi.get().strip().upper()
    if not kişi:
        messagebox.showwarning("Uyarı", "Silmek için bir isim girin!")
        return
    if kişi in kişiler:
        kişiler.remove(kişi)
        entry_kisi.delete(0, ctk.END)
        güncelle_liste()
        messagebox.showinfo("Silindi", f"{kişi} listeden silindi.")
    else:
        messagebox.showerror("Hata", f"{kişi} listede bulunamadı!")

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

def rastgele_seç(event=None):  # <-- Enter tuşu da çalışsın diye event=None eklendi
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
    sonuç_pencere = ctk.CTkToplevel(root)
    sonuç_pencere.title("Seçilen Kişiler 🎉")
    sonuç_pencere.geometry("350x400")
    ctk.CTkLabel(sonuç_pencere, text="🎯 Rastgele Seçilenler", font=("Arial", 18, "bold")).pack(pady=15)
    for s in seçilenler:
        ctk.CTkLabel(sonuç_pencere, text=s, font=("Arial", 14)).pack(pady=5)

# Arayüz
root = ctk.CTk()
root.title("🎲 Sefa'nın Çekiliş Uygulaması ")
root.geometry("480x650")

ctk.CTkLabel(root, text="ÇEKİLİŞ UYGULAMASI", font=("Arial", 24, "bold")).pack(pady=12)

# --- Kişi Ekleme Alanı ---
frame_ekle = ctk.CTkFrame(root, corner_radius=15)
frame_ekle.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_ekle, text="Kişi Ekle / Sil:", font=("Arial", 14)).pack(pady=6)

entry_kisi = ctk.CTkEntry(
    frame_ekle,
    placeholder_text="İsim giriniz...",
    width=300,
    corner_radius=8,
    border_width=1,
    state="normal"
)
entry_kisi.pack(pady=6)
entry_kisi.focus_set()
entry_kisi.bind("<Button-1>", lambda e: entry_kisi.focus_set())

buton_frame = ctk.CTkFrame(frame_ekle)
buton_frame.pack(pady=5)

ctk.CTkButton(buton_frame, text="Listeye Ekle ➕", corner_radius=20, width=120, command=kullanıcı_ekle).pack(side="left", padx=5)
ctk.CTkButton(buton_frame, text="Kişi Sil ❌", corner_radius=20, width=120, fg_color="#d9534f", hover_color="#c9302c", command=kişi_sil).pack(side="left", padx=5)

# --- Liste Alanı ---
frame_liste = ctk.CTkFrame(root, corner_radius=15)
frame_liste.pack(pady=10, padx=20, fill="both", expand=True)
ctk.CTkLabel(frame_liste, text="Kişiler Listesi:", font=("Arial", 14, "bold")).pack(pady=5)
listbox = ctk.CTkTextbox(frame_liste, width=400, height=200, corner_radius=10)
listbox.pack(pady=10)
listbox.configure(state="disabled")

# Karıştırma butonu
ctk.CTkButton(root, text="Listeyi Karıştır 🔀", corner_radius=20, command=liste_karıştır).pack(pady=6)

# Rastgele seçim alanı
frame_sec = ctk.CTkFrame(root, corner_radius=15)
frame_sec.pack(pady=6, padx=20, fill="x")
ctk.CTkLabel(frame_sec, text="Kaç kişi seçilsin?", font=("Arial", 14)).pack(pady=6)
entry_sayi = ctk.CTkEntry(frame_sec, width=80)
entry_sayi.pack(pady=6)

# Enter tuşuna basınca rastgele_seç fonksiyonu çalışsın
entry_sayi.bind("<Return>", rastgele_seç)

ctk.CTkButton(frame_sec, text="Rastgele Seç 🎯", corner_radius=20, command=rastgele_seç).pack(pady=8)

# --- Çıkış Butonları ---
ctk.CTkButton(root, text="Çıkış 🚪", fg_color="#d9534f", hover_color="#c9302c", corner_radius=20, command=root.destroy).pack(pady=6)
ctk.CTkButton(root, text="Uygulamadan Çık ❌", fg_color="#b52b27", hover_color="#8a1e1b", corner_radius=20, command=root.destroy).pack(pady=10)

# Başlangıç verisi
# kişiler.extend(["ALİ", "AYŞE", "MEHMET", "SEFA"])
güncelle_liste()

root.mainloop()
