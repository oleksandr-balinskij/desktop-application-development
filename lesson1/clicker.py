from customtkinter import*

def button_callback():
    global count 
    count = count + 1
    lbl.configure(text=count)

app = CTk()
app.title("клікер")
app.geometry("500x500")

set_appearance_mode("dark")

count = 0 

lbl = CTkLabel(app, text="0", font=("Arial", 30, "bold"))
lbl.pack(pady=20)

btn = CTkButton(app, text="Click", command=button_callback)
btn.pack(pady=20)

app.mainloop()