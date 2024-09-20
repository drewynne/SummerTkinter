
from tkinter import ttk

class Utility:

    @staticmethod
    def set_my_style():
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.map('StartFrame.TFrame', background=[('active', 'cyan')])
        style.configure('TButton', font="Helvetica 16 bold", background='white', foreground='black')
        style.map("Regular.TButton", background=[('active', 'cyan')], foreground=[('active', 'black')])
        style.map("Accent.TButton", background=[('active', 'orange')], foreground=[('active', 'black')])
        style.configure('TLabel', font="Helvetica 12 bold", background='white', foreground='black')

if __name__ == '__main__':
    print("THIS IS A TEST")
