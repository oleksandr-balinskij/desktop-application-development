from customtkinter import *
from PIL import Image

app = CTk()
app.title("Меню")
app.geometry("550x350")

frm = CTkFrame(app)
frm.pack(side="top", pady=15)

img1 = CTkImage(Image.open("ico1.png"), size=(20, 20))
img2 = CTkImage(Image.open("ico2.png"), size=(20, 20))
img3 = CTkImage(Image.open("ico3.png"), size=(20, 20))
img4 = CTkImage(Image.open("ico4.png"), size=(20, 20))

btn1 = CTkButton(frm, text="Головна", image=img1)
btn1.pack(side="left", padx=5)
btn2 = CTkButton(frm, text="Профіль", image=img2)
btn2.pack(side="left", padx=5)
btn3 = CTkButton(frm, text="Налаштування", image=img3)
btn3.pack(side="left", padx=5)
btn4 = CTkButton(frm, text="Вихід", image=img4)

main_img = CTkImage(Image.open("dog.jpg"), size=(150, 150))

lbl = CTkLabel(app, text="", image=main_img)
lbl.pack(pady=25)

app.mainloop()