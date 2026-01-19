import tkinter as tk
import pandas as pd
from tkinter import filedialog
import Actual_Fileparse


#def file_button_clicked():
#    filename = filedialog.askopenfilename()
#    print(filename)

m = tk.Tk()
m.geometry("700x500")
'''
widgets are added here
'''
label = tk.Label(m, text='sup nerd')
label.pack()
m.title('Permit Parser 9000!')
file_button = tk.Button(m, 
                   text='Pick a file', 
                   width=15, 
                   command=Actual_Fileparse.file_read_parser,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   wraplength=100)
file_button.pack()
quit_button = tk.Button(m,
                        text='Quit program',
                        command=m.destroy,
                        anchor='w')
quit_button.pack()

#filename=filedialog.askopenfilename()
#print(filename)

tk.mainloop()