from customtkinter import*

def button_callback():
    clr = etr.get()
    app.configure(fg_color= clr)

app = CTk()
app.title('Кольори')
app.geometry("400x300")
set_appearance_mode("dark")

lbl = CTkLabel(app, text="Введи колір:")
lbl.pack(padx=20, pady=20)
etr = CTkEntry(app)
etr.pack()

btn = CTkButton(app, text= "Перевірити", command=button_callback)
btn.pack(padx=20, pady=20)

app.mainloop()