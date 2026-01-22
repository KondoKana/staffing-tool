import dearpygui.dearpygui as dpg

form_width = 300

#holds tags that corrospond to the fields holding information that we want
permit_cata_tags = []
discipline_tags = []
departement_tags = []

departement_dropdowns = []



dpg.create_context()


def delete_cata(sender, app_data, user_data):
    dpg.delete_item(user_data[0])
    user_data[1].remove(user_data[2])

def delete_disc(sender, app_data, user_data):
    dpg.delete_item(user_data[0])
    user_data[1].remove(user_data[2])

def delete_dept(sender, app_data, user_data):
    dpg.delete_item(user_data[0])
    user_data[1][0].remove(user_data[2][0])
    user_data[1][1].remove(user_data[2][1])

def call_update(sender, app_data):
    print(f"Updating {sender}")

def update_combos_adding(sender, app_data):
    c = get_cata_names()
    for tag in departement_dropdowns:
        dpg.configure_item(tag, items=c)
        val = dpg.get_value(tag)
        if not val in c:
            dpg.set_value(tag,"")
    return 0

def update_combos_selecting(sender, app_data):
    val = dpg.get_value(sender)
    for tag in departement_dropdowns:
        if tag == sender:
            continue
        elif dpg.get_value(tag) == val:
            dpg.set_value(tag,"")


def make_fill_text_permit_catas(sender, app_data):
    textbox_group = dpg.add_group(parent=catagories_group)

    text_tag = dpg.add_input_text(label="Permit Catagory", width = form_width, parent = textbox_group, callback = update_combos_adding)
    with dpg.group(parent=textbox_group, horizontal=True):
        number_tag = dpg.add_input_int(width=form_width-58)
        dpg.add_button(width=50,label="Delete", before = number_tag, user_data = [textbox_group,permit_cata_tags,(text_tag,number_tag)], callback = delete_cata)
        permit_cata_tags.append((text_tag,number_tag))
        dpg.add_text("Estimated number of Permit Types in that catagory")
    


def make_fill_text_review(sender, app_data):
    textbox_group = dpg.add_group(parent=disciplines_group, horizontal = True)
    text_tag = dpg.add_input_text(hint="Review Discipline",width=form_width,parent=textbox_group, callback = call_update)
    discipline_tags.append(text_tag)
    dpg.add_button(width=50, label="Delete", parent=textbox_group, user_data = [textbox_group,discipline_tags,[text_tag]], callback = delete_disc)

def make_fill_text_departments(sender, app_data):
    textbox_group = dpg.add_group(parent=department_group, horizontal = True)
    text_tag = dpg.add_input_text(hint="Department Name",width=form_width,parent=textbox_group, callback = call_update)
    dropdown_tag = dpg.add_combo(items=get_cata_names(), parent = textbox_group, callback = update_combos_selecting)
    dpg.add_button(width=50, label="Delete", parent=textbox_group, before = text_tag, user_data = [textbox_group,[departement_tags, departement_dropdowns],[text_tag, dropdown_tag]], callback = delete_dept)
    
    departement_tags.append(text_tag)
    departement_dropdowns.append(dropdown_tag)



def print_tag_values(sender, app_data, user_data):
    s = []
    for tag in user_data:
        if type(tag) != int:
            s.append((dpg.get_value(tag[0]), dpg.get_value(tag[1])))
        else:
            s.append(dpg.get_value(tag))
    print(s)
    return s

def get_cata_names():
    c = []
    for tag in permit_cata_tags:
        c.append(dpg.get_value(tag[0]))
    return c

        

with dpg.window(tag="Primary Window", width=800, height=300, no_collapse=True, no_move=True):
    dpg.add_text("Please input your full time employee equivalent")
    fte_eq = dpg.add_input_int()
    dpg.add_separator()
    

    dpg.add_text("Please list the Catagories of Permits")
    catagories_group = dpg.add_group()
    dpg.add_separator()

    dpg.add_text("Please list the Review Disciplines")
    disciplines_group = dpg.add_group()
    dpg.add_separator()

    dpg.add_text("Please list the your Departments")
    department_group = dpg.add_group()
    dpg.add_separator()


    dpg.add_button(label = "Add", callback = make_fill_text_permit_catas, before = catagories_group)
    dpg.add_button(label = "Add", callback = make_fill_text_review, before = disciplines_group)
    dpg.add_button(label = "Add", callback = make_fill_text_departments, before = department_group)
    


    with dpg.group(horizontal=True):
        dpg.add_button(label = "Get Catagories" , user_data = permit_cata_tags , callback = print_tag_values)
        dpg.add_button(label = "Get Disciplines" , user_data = discipline_tags , callback = print_tag_values)
        dpg.add_button(label = "Get Departments" , user_data = departement_tags , callback = print_tag_values)
    
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()