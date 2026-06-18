from customtkinter import *

app = CTk()
app.geometry("350x220")
app.title("Парк атракціонів")

def check():
    result_window = CTkToplevel(app)
    result_window.geometry("300x150")
    result_window.title("Результати")
    result_window.attributes("-topmost", True)

    age = int(entry_age.get())
    height = int(entry_height.get())

    if age >= 10 and height >= 120:
        text = "Вітаємо!\nВперед, якщо не боїшся!"
    else:
        text = "Треба трохи підрости.\nПовертайся до нас, коли будеш старше 10 років та ростом вище 120 см."

    result_label = CTkLabel(
        result_window,
        text=text,
        font=("Arial", 14, "bold"),
        wraplength=260
    )
    result_label.pack(expand=True)

question = CTkLabel(
    app,
    text="Чи можеш ти кататись на американських гірках у нашому парку?",
    font=("Arial", 16, "bold"),
    wraplength=300
)
question.pack(pady=10)

entry_age = CTkEntry(app, placeholder_text="вік")
entry_age.pack(pady=5)

entry_height = CTkEntry(app, placeholder_text="зріст (у см)")
entry_height.pack(pady=5)

btn_check = CTkButton(
    app,
    text="Перевірити",
    command=check
)
btn_check.pack(pady=10)

app.mainloop()