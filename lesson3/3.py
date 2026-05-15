from customtkinter import *

app = CTk()
app.geometry("400x200")
app.title("Вікторина")

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure((0, 3), weight=1)

question = CTkLabel(app, text="Яка структура даних зберігає пари ключ-значення?", font=("Arial", 15, "bold"))
question.grid(row=0, column=0, columnspan=2, pady=15)

r = IntVar(value=0)

btn1 = CTkRadioButton(app, text="список", variable=r, value=1)
btn1.grid(row=1, column=0, padx=40, pady=5)

btn2 = CTkRadioButton(app, text="словник", variable=r, value=2)
btn2.grid(row=1, column=1, padx=40, pady=5)

btn3 = CTkRadioButton(app, text="кортеж", variable=r, value=3)
btn3.grid(row=2, column=0, padx=40, pady=5)

btn4 = CTkRadioButton(app, text="множина", variable=r, value=4)
btn4.grid(row=2, column=1, padx=40, pady=5)

button = CTkButton(app,text="Відповісти")
button.grid(row=3, column=0, columnspan=2, pady=20)

app.mainloop()