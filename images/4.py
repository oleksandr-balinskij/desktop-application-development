from customtkinter import *
from PIL import Image

app = CTk()
app.title("Галерея картинок")
app.geometry("500x500")

app.iconbitmap("ico1.png")

lbl = CTkLabel(app, text="Обери гравця:", font=("Arial", 30))
lbl.grid(row=0, column=0, columnspan=2, pady=20)

nik = CTkImage(light_image=Image.open("nik.png"), size=(120, 120))
spaik = CTkImage(light_image=Image.open("spaik.png"), size=(120, 120))
tom = CTkImage(light_image=Image.open("tom.png"), size=(120, 120))
vuhastik = CTkImage(light_image=Image.open("vuhastik.png"), size=(120, 120))

btn1 = CTkButton(app, text="Нік", image=nik, compound="bottom", width=180, height=180)
btn1.grid(row=1, column=0, padx=10, pady=10)

btn2 = CTkButton(app, text="Спайк", image=spaik, compound="bottom", width=180, height=180)
btn2.grid(row=1, column=1, padx=10, pady=10)

btn3 = CTkButton(app, text="Том", image=tom, compound="top", width=180, height=180)
btn3.grid(row=2, column=0, padx=10, pady=10)

btn4 = CTkButton(app, text="Вухастик", image=vuhastik, compound="top", width=180, height=180)
btn4.grid(row=2, column=1, padx=10, pady=10)

app.mainloop()