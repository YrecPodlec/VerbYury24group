from tkinter import *
from tkinter import messagebox
def btn_ok_click():
    global qas
    global cur_qa
    global count_true_answers
    if (cur_qa >= 0 and qas[cur_qa].true_answer == selected_answer.get()):
        count_true_answers = count_true_answers + 1
    cur_qa = cur_qa + 1
    global radio_buttons
    for radio_button in radio_buttons: 
        radio_button.destroy()
    radio_buttons.clear()
    global btn_ok
    global btn_finish
    if (cur_qa == len(qas)):
        btn_finish_click()
    else:
        global cur_question
        cur_question.set(qas[cur_qa].question)
        for answer in qas[cur_qa].answers:
            python_checkbutton = Radiobutton(text=answer, value=len(radio_buttons), variable=selected_answer, padx=15, pady=10)
            python_checkbutton.grid(row=len(radio_buttons)+1, column=0, sticky=W)
            radio_buttons.append(python_checkbutton)
        btn_ok.grid(row=5, column=1, rowspan=2, columnspan=1, sticky=SW)
        btn_finish.grid(row=5, column=0, sticky=SW)
def btn_finish_click():
    global qas
    global header
    global btn_ok
    global btn_finish
    global count_true_answers
    global radio_buttons
    for radio_button in radio_buttons: 
        radio_button.destroy()
    radio_buttons.clear()
    btn_ok.grid_remove()
    btn_finish.grid_remove()
    header.grid_remove()
    result_test = Label(text=f'Ваш результат: {count_true_answers} правильных ответов из {len(qas)}', padx=15, pady=10)
    result_test.grid(row=0, column=0, sticky=W)
    messagebox.showinfo("Завершение теста","Вы завершили прохождение теста по матеше. Ваш результат высвечен на экране.")
root = Tk()
qas = list()
cur_qa = -1
count_true_answers = 0
cur_question = StringVar()
selected_answer = IntVar()
radio_buttons = list()
btn_ok = Button(text="Далее", background="#555", foreground="#d5cade",font="16", command=btn_ok_click)
btn_finish = Button(text="Завершить", background="#555", foreground="#d5cade",font="16", command=btn_finish_click)
header = Label(textvariable=cur_question, padx=15, pady=10)
class QA:
    def __init__(self, question, answers, true_answer):
        self.question = question
        self.answers = answers
        self.true_answer = true_answer
 
    def __str__(self):
        return f'{self.question}: {self.answers} : {self.true_answer}'
def main():
    lines = list()
    with open("data.txt", mode="r", encoding="utf-8") as file_in:
        for line in file_in:
            lines.append(line.strip())
    i = 0
    while i < len(lines)-1:
        question = lines[i]
        i = i + 1
        count_answers = int(lines[i])
        i = i + 1
        j = 0
        answers = list()
        while j < count_answers:
            answers.append(lines[i])
            i = i + 1
            j = j + 1
        true_answer = int(lines[i])
        i = i + 2
        qas.append(QA(question, answers, true_answer))
    root.title("Тест по матеше")
    root.geometry("700x300")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    header.grid(row=0, column=0, sticky=W)
    btn_ok_click()
    root.mainloop()
if __name__== "__main__":
  main()