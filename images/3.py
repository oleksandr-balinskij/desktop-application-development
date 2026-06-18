from customtkinter import *
from PIL import Image

app = CTk()
app.title("Меню")
app.geometry("350x175")

frm = CTkFrame(app)
frm.pack(side="left", padx=15, pady=15)

img1 = CTkImage(Image.open("ico1.png"), size=(20, 20))
img2 = CTkImage(Image.open("ico2.png"), size=(20, 20))
img3 = CTkImage(Image.open("ico3.png"), size=(20, 20))
img4 = CTkImage(Image.open("ico4.png"), size=(20, 20))

CTkButton(frm, text="Головна", image=img1, anchor="w").pack(pady=5)
CTkButton(frm, text="Профіль", image=img2, anchor="w").pack(pady=5)
CTkButton(frm, text="Налаштування", image=img3, anchor="w").pack(pady=5)
CTkButton(frm, text="Вихід", image=img4, anchor="w").pack(pady=5)

main_img = CTkImage(Image.open("dog.jpg"), size=(120, 120))

CTkLabel(app, text="", image=main_img).pack(side="right", padx=15, pady=15)

app.mainloop()
