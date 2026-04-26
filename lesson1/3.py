from customtkinter import*

def button_callback():
    set_appearance_mode("light")
def button_dark():
    set_appearance_mode("dark")
win = CTk()
win.title('Зміна режиму')
win.geometry("350x250")
set_appearance_mode("light")

btn_l = CTkButton(win, text="light", command=button_callback)
btn_d = CTkButton(win, text="dark", command=button_dark)
btn_l.pack(padx=20, pady=20)
btn_d.pack(side="bottom", padx=10, pady=10)

win.mainloop()