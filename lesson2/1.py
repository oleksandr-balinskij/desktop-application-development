from customtkinter import*

win = CTk()
win.title(" створення кнопок")
win.geometry("350x240")

btn = CTkButton(win, text="Перша", corner_radius=15, text_color="darkblue", 
                font=("Courier New", 15, "bold" ))
btn.pack(padx=10, pady=20)

btn2 = CTkButton(win, text="Друга", width=100, height=100)

btn2.pack(padx=10, pady=10)

btn3 = CTkButton(win, text="Третья", border_width=1, border_color="purple",
                 fg_color="pink", hover_color="purple")

btn3.pack(padx=10, pady=10)

win.mainloop()