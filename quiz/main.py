from customtkinter import *  # імпорт бібліотеки

app = CTk()  # створення головного вікна
app.geometry("400x300")  # розмір вікна
app.title("quiz")  # назва вікна

def open_menu():
    frm_menu.lift()  # відкрити меню

def close_menu():
    frm_main.lift()  # повернути головний екран

frm_menu = CTkFrame(app)  # створення фрейму меню
frm_menu.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)  # розміщення

frm_main = CTkFrame(app)  # створення головного фрейму
frm_main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)  # розміщення

btn_menu = CTkButton(frm_main, text="Меню", command=open_menu)  # кнопка відкриття меню
btn_menu.grid(row=0, column=0, padx=10, pady=10)

btn_close = CTkButton(frm_menu, text="Повернутись", command=close_menu)  # кнопка назад
btn_close.grid(row=0, column=0, padx=10, pady=10)

question = CTkLabel(
    frm_main,
    text="Яка структура даних зберігає пари ключ-значення?",  # текст питання
    font=("Arial", 20)
)
question.grid(row=1, column=0, columnspan=2, pady=30)

radio_var = StringVar(value="")  # змінна для збереження вибору

rb1 = CTkRadioButton(frm_main, text="кортеж", variable=radio_var, value="кортеж")
rb1.grid(row=2, column=0, padx=40, pady=10)

rb2 = CTkRadioButton(frm_main, text="множина", variable=radio_var, value="множина")
rb2.grid(row=2, column=1, padx=40, pady=10)

rb3 = CTkRadioButton(frm_main, text="список", variable=radio_var, value="список")
rb3.grid(row=3, column=0, padx=40, pady=10)

rb4 = CTkRadioButton(frm_main, text="словник", variable=radio_var, value="Словник")
rb4.grid(row=3, column=1, padx=40, pady=10)

def check_answer():
    if radio_var.get() == "Словник":  # перевірка правильної відповіді
        result.configure(text="Правильно!", text_color="green")
    else:
        result.configure(text="Неправильно!", text_color="red")

result = CTkLabel(frm_main, text="")  # поле для виводу результату
result.grid(row=0, column=1, padx=20, pady=10, sticky="e")

btn_answer = CTkButton(frm_main, text="Відповісти", command=check_answer)  # кнопка перевірки
btn_answer.grid(row=4, column=0, columnspan=2, pady=20)

app.mainloop()  # запуск програми