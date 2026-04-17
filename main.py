from customtkinter import *

def button_callback():
    print("button clicked")

app = CTk()
app.title('First Program')
app.geometry("400x150")

btn = CTkButton(app, text="Click here", command=button_callback)
btn.pack(padx=20, pady=20)

app.mainloop()