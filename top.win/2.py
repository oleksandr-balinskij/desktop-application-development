from customtkinter import *

app = CTk()
app.geometry("350x220")
app.title("Вікторина")

radio_var = IntVar(value=-1)

def check_answer():
    if radio_var.get() == 2:
        result_label.configure(text="Правильно!")
    else:
        result_label.configure(text="Неправильно!")

    result_window.deiconify()

def close_result():
    radio_var.set(-1)
    result_window.withdraw()

question = CTkLabel(
    app,
    text='print(2 + "2")',
    font=("Arial", 16, "bold")
)
question.pack(pady=20)

rb1 = CTkRadioButton(app, text="4", variable=radio_var, value=0)
rb1.pack()

rb2 = CTkRadioButton(app, text="22", variable=radio_var, value=1)
rb2.pack()

rb3 = CTkRadioButton(app, text="Помилка", variable=radio_var, value=2)
rb3.pack()

btn_answer = CTkButton(
    app,
    text="Відповісти",
    command=check_answer
)
btn_answer.pack(pady=15)

result_window = CTkToplevel(app)
result_window.geometry("300x150")
result_window.title("Результати")

result_label = CTkLabel(
    result_window,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(expand=True)

btn_next = CTkButton(
    result_window,
    text="Далі",
    command=close_result
)
btn_next.pack(pady=10)

result_window.withdraw()

app.mainloop()