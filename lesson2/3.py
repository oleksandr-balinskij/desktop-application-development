from customtkinter import *

app = CTk()
app.geometry("300x370")
app.title("Вікторина")

lbl = CTkLabel(app, text="Які типи данних мови Пайтон є незмінними?", font=("Arial", 16))
lbl.pack(pady=10)

cb1 = CTkCheckBox(app, text="числа")
cb1.pack(anchor="w", padx=20)

cb2 = CTkCheckBox(app, text="рядки")
cb2.pack(anchor="w", padx=20)

cb3 = CTkCheckBox(app, text="списки")
cb3.pack(anchor="w", padx=20)

cb4 = CTkCheckBox(app, text="словники")
cb4.pack(anchor="w", padx=20)

cb5 = CTkCheckBox(app, text="кортежі")
cb5.pack(anchor="w", padx=20)

cb6 = CTkCheckBox(app, text="множини")
cb6.pack(anchor="w", padx=20)

lbl_result = CTkLabel(app, text="")
lbl_result.pack(pady=10)

def check():
    if cb1.get() == 1 and cb2.get() == 1 and cb5.get() == 1:
        lbl_result.configure(text="Правильно!")
    else:
        lbl_result.configure(text="Неправильно!")

btn = CTkButton(app, text="Відповісти", command=check)
btn.pack(pady=10)

app.mainloop()