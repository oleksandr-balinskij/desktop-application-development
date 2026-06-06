from customtkinter import *
from random import shuffle

app = CTk()
app.geometry("400x320")
app.title("quiz")

def open_menu():
    txt = ""
    for i in questions:
        txt += f"{i['question']}\n"
        if i["full_answers"] == 0:
            txt += 'Успішність: немає данних\n\n'
        else:
            x = i["true_answers"] / i["full_answers"] * 100
            txt += f"Успішність: {round(x, 2)}%\n\n"
    tx_box.configure(state="normal")   
    tx_box.delete("0.0", END)
    tx_box.insert("0.0", txt)
    tx_box.configure(state="disabled") 
    frm_menu.lift()

def close_menu():
    frm_main.lift()

def change_mode():
    if light_mode.get() == 1:
        set_appearance_mode("light")
        light_mode.configure(text="☀")
    else:
        set_appearance_mode("dark")
        light_mode.configure(text="☾")

questions = [
    {
       "question": "в якому році випустився мультсеріал берсерк",
       "answers": ["1998", "1991", "1987", "1981"],
       "correct": "1991",
       "true_answers": 0,
       "full_answers": 0
    },

    {
       "question": "в якій серії була остання схватка грифіта та гатса",
       "answers": ["21", "18", "25", "11"],
       "correct": "18",
       "true_answers": 0,
       "full_answers": 0
       
    },

    {
       "question": "в якій серії грифіт зрадив загін",
       "answers": ["7", "18", "23", "15"],
       "correct": "23",
       "true_answers": 0,
       "full_answers": 0
    },

    { 
       "question": "що зробив грифіт з гатсом в затемненні",
       "answers": ["помирився", "вбив", "знущався над ним", "залишив"],
       "correct": "знущався над ним",
       "true_answers": 0,
       "full_answers": 0
    }        
]

index_right = -1
count = 0

def load_question():
    global count
    global index_right
    q = questions[count]
    question.configure(text=q ['question'])
    voprosi = q['answers']
    shuffle(voprosi)
    index_right=voprosi.index(q["correct"])
    rb1.configure(text=voprosi[0])
    rb2.configure(text=voprosi[1])
    rb3.configure(text=voprosi[2])
    rb4.configure(text=voprosi[3])

    radio_var.set(-1)
    
def check_answer():
    global count
    if btn_answer.cget("text") == "Відповісти":
        questions[count]["full_answers"] += 1
        if radio_var.get() == index_right:
            questions[count]["true_answers"] += 1
            result.configure(text="Правильно!", text_color="green")
            if count < len(questions) - 1:
                count += 1
                btn_answer.configure(text="Далі")
            else:
                count = 0
                btn_answer.configure(text="почати знову")
        else:
            result.configure(text="Неправильно!", text_color="red")
    else:
        result.configure(text="")
        btn_answer.configure(text="Відповісти")
        load_question()

frm_menu = CTkFrame(app)
frm_menu.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

frm_main = CTkFrame(app)
frm_main.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

frm_main.grid_columnconfigure(0, weight=1)
frm_main.grid_columnconfigure(1, weight=1)
frm_main.grid_rowconfigure((1, 4 ), weight=1)
frm_menu.grid_columnconfigure((0, 1), weight=1)
frm_menu.grid_rowconfigure((1), weight=1)

btn_menu = CTkButton(frm_main, text="Меню", command=open_menu)
btn_menu.grid(row=0, column=0, columnspan=1, pady=10)

btn_close = CTkButton(frm_menu, text="Повернутись", command=close_menu)
btn_close.grid(row=0, column=0, padx=10, pady=10)

question = CTkLabel(frm_main, text="Яка структура даних зберігає пари ключ-значення?", font=("Arial", 20), wraplength=350)
question.grid(row=1, column=0, columnspan=2, pady=30)

light_mode = CTkSwitch(frm_menu, text="☀", command=change_mode)
light_mode.grid(row=0, column=1 , sticky="e")

light_mode.select()

tx_box = CTkTextbox(frm_menu, )
tx_box.grid(row=1, column=0, columnspan=2, sticky="wens", padx=2, pady=2)

radio_var = IntVar(value=-1)

rb1 = CTkRadioButton(frm_main, text="кортеж", variable=radio_var, value=0)
rb1.grid(row=2, column=0, padx=20, pady=10)

rb2 = CTkRadioButton(frm_main, text="множина", variable=radio_var, value=1)
rb2.grid(row=2, column=1, padx=20, pady=10)

rb3 = CTkRadioButton(frm_main, text="список", variable=radio_var, value=2)
rb3.grid(row=3, column=0, padx=20, pady=10)

rb4 = CTkRadioButton(frm_main, text="словник", variable=radio_var, value=3)
rb4.grid(row=3, column=1, padx=20, pady=10)

result = CTkLabel(frm_main, text="")
result.grid(row=0, column=1, padx=20, pady=10, sticky="e")

btn_answer = CTkButton(frm_main, text="Відповісти", command=check_answer)
btn_answer.grid(row=4, column=0, columnspan=2, pady=20)

load_question()

app.mainloop()