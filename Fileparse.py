import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

# Hello peter. I am here to give you information.
# In order for this to work, you need to go to your VS code and upgrade the Python version to the latest version, 3.13.5.
# You can do this by going to View, opening the command pallete, searching "Python: Select Interpreter"
# Additionally, you will need to do "pip3 install openpyxl" in the terminal
# In order to get this shit running, you run UI.py


def parser():
    filename=filedialog.askopenfilename()


    file = pd.ExcelFile(filename)
    thing = pd.read_excel(file, skiprows=1, usecols="B:V")
    for i in thing.columns:
        print(i)



    def output(dataset):
        #tada!
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
        dataset.to_excel()