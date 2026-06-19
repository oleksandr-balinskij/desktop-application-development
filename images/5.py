from customtkinter import *
from PIL import Image

app = CTk()
app.title("Екран входу")
app.geometry("320x350")

img1 = CTkImage(Image.open("dog.jpg"), size=(100, 100))
img2 = CTkImage(Image.open("nik.png"), size=(100, 100))

def show_password():
    if check_var.get() == 1:
        password.configure(show="")
    else:
        password.configure(show="*")

def change_image():
    logo.configure(image=img2)

logo = CTkLabel(app, text="", image=img1)
logo.pack(pady=10)

login = CTkEntry(app, placeholder_text="login", width=180)
login.pack(pady=5)

password = CTkEntry(app, placeholder_text="password", show="*", width=180)
password.pack(pady=5)

check_var = IntVar()

check = CTkCheckBox(
    app,
    text="Показати пароль",
    variable=check_var,
    command=show_password
)
check.pack(pady=5)

btn = CTkButton(
    app,
    text="Sign in",
    command=change_image
)
btn.pack(pady=10)

app.mainloop()