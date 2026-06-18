from customtkinter import*
from PIL import Image

app = CTk()
app.title("Моє перше зображення в вікні")

img = CTkImage(light_image=Image.open("cat.png"), size=(300, 200))

lbl = CTkLabel(app, image=img, text="")
lbl.pack(pady=10, padx=10)

app.mainloop()