import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import openpyxl

# Hello peter. I am here to give you information.
# In order for this to work, you need to go to your VS code and upgrade the Python version to the latest version, 3.13.5.
# You can do this by going to View, opening the command pallete, searching "Python: Select Interpreter"
# Additionally, you will need to do "pip3 install openpyxl" in the terminal
# In order to get this shit running, you run UI.py

#types-x-per-interval
#hours-per-item-x-positions
#staffing-availibility

#xlsxwrite 

fte_per_person = 1872

class Position:
    def __init__(self, name, count, hour_share):
        self.name = name
        self.count = count
        self.hour_share = hour_share

class Review_Discipline:
    def __init__(self, name):
        self.name = name
        self.positions = []
        self.total_hours = 0

class Permit_or_Difficulity_or_Inspections():
    def __init__(self, per_year, name):
        self.per_year = per_year
        self.type = name
        self.sub_type_list = []
    
    

def main():
    parser(False)



def parser(ui = True, filename ="Template Input.xlsx"):
    categories = {}
    
    if ui:
        filename=filedialog.askopenfilename()   

    file = pd.ExcelFile(filename)
    thing = pd.read_excel(file, sheet_name=None)
    print(thing['staffing-availibility'])
    print(type(thing))
    output(thing)


    # df = openpyxl.load_workbook(filename)
    # df.active
    # print(df.sheetnames)
    # sa = df["staffing-availibility"]
    # for row in sa.iter_rows():
    #     for cell in row:
    #         if isinstance(cell, openpyxl.cell.cell.MergedCell):
    #             print(cell)
    file = pd.ExcelFile(filename)
    thing = pd.read_excel(file, sheet_name=None, header=0)
    typesx = thing['types-x-per-interval']
    hoursx = thing['hours-per-item-x-positions']
    staffing = thing['staffing-availibility']
    
    for index, row in typesx.iterrows():
        if index ==0:
            print("First row")
        else:
            if type(row['Catagory']==float and type(row['Permits per year']==float)):
                categories[row['Permit Type']]=[]
                most_recent = row['Permit Type']
            if type(row['Catagory'])==float:
                categories[most_recent].append(Permit_or_Difficulity_or_Inspections(row['Permit Type'], row['Permits per Year']))
            if type(row['Catagory'])!=float:
                
                
                


    
    
    
    
    #for i in thing.columns:
    #    print(i)
    #output(thing)
    #df = openpyxl.load_workbook(filename)
    #df.active
    #print(df.sheetnames)
    #sa = df["staffing-availibility"]
    #for row in sa.iter_rows():
    #    for cell in row:
    #        if isinstance(cell, openpyxl.cell.cell.MergedCell):
    #            print(cell)

def output(dataset):
    #tada!
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
        
     with pd.ExcelWriter('output.xlsx') as writer:
        dataset['types-x-per-interval'].to_excel(writer, sheet_name='types-x-per-interval')
        dataset['hours-per-item-x-positions'].to_excel(writer, sheet_name='hours-per-item-x-positions')
        dataset['staffing-availibility'].to_excel(writer, sheet_name='staffing-availibility')

if __name__ == "__main__":
    main()