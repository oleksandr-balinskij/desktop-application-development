from customtkinter import*

win = CTk()
win.geometry("330x220")

def open_top():
    top = CTkToplevel(win)
    top.attributes("-topmost", True)
    pole = CTkEntry(top, placeholder_text="колір (назва або HEX)")
    def poisk():
        win.configure(fg_color = pole.get())
        top.destroy()
    pole.pack(pady=15, padx=15)
    btn1 = CTkButton(top, text="Зберегти", command=poisk)
    btn1.pack(pady=15, padx=15)

btn = CTkButton(win, text="Обрати колір фону", command=open_top)
btn.place(anchor="center", rely=0.5, relx=0.5)

win.mainloop()
