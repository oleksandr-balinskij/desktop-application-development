from customtkinter import*

app = CTk()
app.title("Buttons")
app.geometry("300x300")

btn = CTkButton(app, text=" ", width=100, height=100, fg_color="blue")
btn.grid(row=0, column=0)

btn2 = CTkButton(app, text=" ", width=100, height=100, fg_color="pink")
btn2.grid(row=0, column=2)

btn3 = CTkButton(app, text=" ", width=100, height=100, fg_color="yellow")
btn3.grid(row=1, column=1)

btn4 = CTkButton(app, text=" ", width=100, height=100, fg_color="purple")
btn4.grid(row=2, column=0)

btn5 = CTkButton(app, text=" ", width=100, height=100, fg_color="green")
btn5.grid(row=2, column=2)

app.mainloop()