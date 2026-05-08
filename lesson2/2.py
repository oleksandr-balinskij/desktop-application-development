from customtkinter import *

app = CTk()
app.title("Викторина")
app.geometry("300x300")

lbl = CTkLabel(app, wraplength=300, text="Яка структура даних зберігає пари ключ-значення?")
lbl.pack(pady=10)

var = IntVar()

rb1 = CTkRadioButton(app, text="список", variable=var, value=1)
rb1.pack(anchor="w", padx=20)

rb2 = CTkRadioButton(app, text="словник", variable=var, value=2)
rb2.pack(anchor="w", padx=20)

rb3 = CTkRadioButton(app, text="кортеж", variable=var, value=3)
rb3.pack(anchor="w", padx=20)

rb4 = CTkRadioButton(app, text="множина", variable=var, value=4)
rb4.pack(anchor="w", padx=20)

lbl_result = CTkLabel(app, text="")
lbl_result.pack(pady=10)

def check():
    if var.get() == 2:
        lbl_result.configure(text="Правильно!")
    else:
        lbl_result.configure(text="Неправильно!")

btn = CTkButton(app, text="Відповісти", command=check)
btn.pack(pady=10)

app.mainloop()
