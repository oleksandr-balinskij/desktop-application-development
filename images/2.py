from customtkinter import*
from PIL import Image

app = CTk()
app.title("Картка профілю")
app.geometry("400x400")

img = CTkImage(light_image=Image.open("murzik_crop.png"), size=(300, 200))
txt = CTkLabel(app, text="мурзик мурзикович", font=("Courier new", 24, "bold"))
lbl = CTkLabel(app, image=img, text="")
lbl.pack(pady=20, padx=20)
txt.pack(pady=10, padx=10)

btn = CTkButton(app, text="Написати", font=(None, 20), height=50, corner_radius=20)
btn.pack(pady=20, padx=20)

app.mainloop()