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

    categories = parse_types_x(typex)
    parse_hours_x(hoursx,categories)
    for i in categories["Building "][0].review_disciplines:
        print (i.name, i.total_hours)
    

def parse_types_x(typex, bottom= 62, row = 2, column = 3):
    parse_type_generator = typex.iter_rows(min_row=row, max_row = bottom, max_col = column, values_only=True)
    categories = {}
    counter = 0
    for row in parse_type_generator:
        counter += 1
        Catagory = row[0]
        
        Permit_type = row[1]
        Per_year = row[2]

        if Catagory== None and Per_year == None:
            categories[Permit_type]=[]
            most_recent = Permit_type

        elif Catagory == None:
            categories[most_recent].append(Permit(Per_year, Permit_type))
        
        elif Catagory != None:
            checker = 0
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
    #for i in categories.values():
        #print(len(i))
    return categories

def parse_hours_x(hoursx,categories, bottom = 50, row = 2, column = 6, min_col=1):
    parse_hours_generator = hoursx.iter_rows(min_row=row, max_row = bottom, max_col=column, min_col=min_col, values_only=True)
    print("\n")
    for i in hoursx.iter_rows(max_row = 1, values_only=True, max_col =  6, min_col = 2):
        names = i
    print(names)
    #print(variable_names)
    counter = 0
    for row in parse_hours_generator:
        counter += 1
        if row[0] in categories:
            current = categories[row[0]]
        else:
            for i in range(len(current)):
                if current[i].type == row[0]:
                    for g in range(1,len(row)):
                        print(g)
                        current[i].review_disciplines.append(Review_Discipline(names[g-1],row[g]))
                    break
    #print(categories.keys())
    #print(categories["Building "][0].review_disciplines)
    #for i in categories["Building "][0].review_disciplines:
    
    #    print (i.name, i.total_hours)

    
            





