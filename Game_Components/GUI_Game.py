# 17/01/2024

import random
import time
from tkinter import *
from tkinter import ttk

# To Do:
# Add Welcome Text
# Add start button
# Move Quit Button to side
# Make Game Components Interact

start_text = 'press start to begin game'
question_text = start_text

def start_game():
    print("Game Started")

    ql_text_var.set('Game Has Begun')
    # time.sleep(1.0) # Move This!!
    root.after(1000, set_next_question())


def set_next_question():
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    a = round(x, 1)
    b = round(y, 1)

    question_text = str(a) + ' + ' + str(b)
    ql_text_var.set(question_text)
    sb_text_var.set('Enter')


root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

ql_text_var = StringVar()
question_label = ttk.Label(frame, textvariable=ql_text_var)
question_label.grid(column=0, row=0)
ql_text_var.set(question_text)



sb_text_var = StringVar()
start_button = ttk.Button(frame, textvariable=sb_text_var, command=start_game)
start_button.grid(column=0, row=1)
sb_text_var.set('Start')


ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=2)
root.mainloop()

