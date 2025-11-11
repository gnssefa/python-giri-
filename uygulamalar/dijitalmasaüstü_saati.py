from tkinter import Label,Tk
import time
import locale

locale.setlocale(locale.LC_TIME ,"tr_TR" )

app_window = Tk()


app_window.title (" Sefa için Dijital Saat ")
app_window.geometry("420x220")
app_window.resizable(0,0)
app_window.configure(bg="black")


text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_widht = 20

#saat etiketi

label = Label(app_window,font=text_font , bg=background , fg=foreground)
label.grid(row=0,column=1,padx=10,pady=10)

#Tarih etiketi

date_label = Label(app_window,font=text_font, bg=background , fg=foreground)
date_label.grid(row=1,column=1,padx=10,pady=10)
 
def digital_hour():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    #Tarih alanı
    
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    label.after(200,digital_hour)







digital_hour()


app_window.mainloop()