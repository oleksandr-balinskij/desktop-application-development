from customtkinter import *

app = CTk()
app.title("Change mode")
app.geometry("300x100")

def change_mode():
    if switch.get() == 1:
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")

switch = CTkSwitch(app, text="mode", command=change_mode)
switch.pack(pady=20)

app.mainloop()