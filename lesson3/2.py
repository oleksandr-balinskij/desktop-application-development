from customtkinter import*

app = CTk()
app.title("messenger")
app.geometry("300x220")

lbl = CTkLabel(app, text="welcome", font=(None, 20, "bold"))
lbl.pack(pady=10, padx=10)

frm = CTkFrame(app)
frm.pack(pady=10, padx=10)

lbl1 = CTkLabel(frm, text="login")
lbl1.pack(side="left")

ent1 = CTkEntry(frm, width=180)
ent1.pack(side="left", padx=5)

frm2 = CTkFrame(app)
frm2.pack(fill="x", padx=10, pady=5)

lbl2 = CTkLabel(frm2, text="Password:")
lbl2.pack(side="left", padx=5)

ent2 = CTkEntry(frm2, width=180, show="*")
ent2.pack(side="left", padx=5)

check = CTkCheckBox(app, text="remember me")
check.pack(padx=10, pady=10)

btn = CTkButton(app, text="Sign in")
btn.pack(pady=10)

app.mainloop()