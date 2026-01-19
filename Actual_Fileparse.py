import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from tkinter import filedialog
import math 

class Position:
    def __init__(self, name, count, hour_share, review_discipline):
        self.name = name
        self.count = count
        self.hour_share = hour_share
        self.discipline = review_discipline

class Review_Discipline:
    def __init__(self, name, hours):
        self.name = name
        self.total_hours = hours
        

class Permit():
    def __init__(self, per_year, name):
        self.per_year = per_year
        self.type = name
        self.sub_type_list = []
        self.review_disciplines = []

def file_read_parser():
    filename=filedialog.askopenfilename() 
    #wb = Workbook()
    thing = load_workbook(filename, rich_text=True)
    sheet_names = thing.sheetnames
    typex = thing[sheet_names[1]]
    hoursx = thing[sheet_names[2]]
    staffing = thing[sheet_names[3]]
    typex_generator = typex.iter_rows(min_row=2, max_row = 62, max_col = 3, values_only=True) #Need to make the min_row/max_row customizable
    hourx_generator = hoursx.iter_rows(min_row=2, max_row = 50, max_col=5, values_only=True)

    categories = {}

    counter = 0
    for row in typex_generator:
        counter += 1
        Catagory = row[0]
        Permit_type = row[1]
        Per_year = row[2]

        if Catagory== None and Per_year == None:
            categories[Permit_type]=[]
            most_recent = Permit_type
            print("first")

        elif Catagory == None:
            categories[most_recent].append(Permit(Per_year, Permit_type))
            print("second)")
        
        elif Catagory != None:
            checker = 0
            print("third")
            for i in categories[most_recent]:
                print(i.type)
                if i.type == Catagory:
                    i.per_year += Per_year
                    i.sub_type_list.append(Permit_type)
                    checker = 1
                    break
            if checker == 0:
                current = Permit(Per_year, Catagory)
                current.sub_type_list.append(Permit_type)
                categories[most_recent].append(current)

    print(counter)
    print(categories.keys())
    for i in categories.values():
        print(len(i))


    counter = 0
    for row in hourx_generator:
        counter += 1
        Permit_type = row[0]
        Administrative = row[1]
        Building = row[2]
        Planning = row[3]
        Stormwater = row[4]
        Engineering = row[5]

        if Administrative == None:




