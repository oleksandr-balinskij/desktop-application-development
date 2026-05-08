from customtkinter import *

set_appearance_mode("light")

app = CTk()
app.geometry("400x200")
app.title("Вікторина")

question = CTkLabel(app, text="Яка структура даних зберігає пари ключ-значення?", font=("Arial", 15, "bold"))
question.grid(row=0, column=0, columnspan=2, pady=15)

btn1 = CTkRadioButton(app, text="список", value=1)
btn1.grid(row=1, column=0, padx=40, pady=5, sticky="w")

btn2 = CTkRadioButton(app, text="словник", value=2)
btn2.grid(row=1, column=1, padx=40, pady=5, sticky="w")

btn3 = CTkRadioButton(app, text="кортеж", value=3)
btn3.grid(row=2, column=0, padx=40, pady=5, sticky="w")

btn4 = CTkRadioButton(app, text="множина", value=4)
btn4.grid(row=2, column=1, padx=40, pady=5, sticky="w")

button = CTkButton(app,text="Відповісти")
button.grid(row=3, column=0, columnspan=2, pady=20)

app.mainloop()