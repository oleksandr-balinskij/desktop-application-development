from customtkinter import *
from PIL import Image

app = CTk()
app.title("Екран входу")
app.geometry("270x270")

image = CTkImage(
    light_image=Image.open("dog.jpg"),
    dark_image=Image.open("dog.jpg"),
    size=(100, 100)
)

logo = CTkLabel(app, text="", image=image)
logo.pack(pady=10)

login = CTkEntry(
    app,
    placeholder_text="login",
    width=180
)
login.pack(pady=5)

password = CTkEntry(
    app,
    placeholder_text="password",
    show="*",
    width=180
)
password.pack(pady=5)

button = CTkButton(
    app,
    text="Sign in"
)
button.pack(pady=10)

app.mainloop()