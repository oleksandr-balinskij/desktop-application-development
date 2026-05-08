from customtkinter import*

app = CTk()

app.geometry("300x220")
app.title("Password generator")

lbl = CTkLabel(app, text="___________", font=("Arial", 20, "bold"))
lbl.pack()

frame = CTkFrame(app)
frame.pack(fill="x")

lbl2 = CTkLabel(frame, text="Введи довжину паролю:")
lbl2.pack(side="left")

ent = CTkEntry(frame, width=100)
ent.pack(side="left")

btn1 = CTkCheckBox(app, text="Використовувати цифри")
btn1.pack(fill="x")

btn2 = CTkCheckBox(app, text="Використовувати спеціальні символи")
btn2.pack(fill="x")

btn = CTkButton(app, text="Згенерувати")
btn.pack()

app.mainloop()