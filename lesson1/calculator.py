from customtkinter import *

def button_callback():
    a = float(ent1.get())
    b = float(ent2.get())
    
    res = a ** b
    
    lbl.configure(text=res)

app = CTk()
app.title("Степінь числа")
app.geometry("300x200")

set_appearance_mode("dark")

ent1 = CTkEntry(app, width=200, placeholder_text="Введи число:")
ent1.pack(pady=10)

ent2 = CTkEntry(app, width=200, placeholder_text="Введи степінь:")
ent2.pack(pady=10)

btn = CTkButton(app, text="Розрахувати", command=button_callback)
btn.pack(pady=10)

lbl = CTkLabel(app, text="0", font=("Arial", 20, "bold"))
lbl.pack(pady=10)

app.mainloop()