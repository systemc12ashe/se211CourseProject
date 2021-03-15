import PySimpleGUI as sg
import csv
import CSVFile
import CSVlibraryValidator
import CSVlibraryInterpreter
# Show CSV data in Table
sg.theme('Dark Red')
# # for table example, https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Table_CSV.py
# def table_example():
#     # filename = sg.popup_get_file('filename to open', file_types=(("CSV Files","*.csv"),))
#     # # --- populate table with file contents --- #
#     # if filename == '':
#     #     return
#     data = []
#     header_list = []
#     button = sg.popup_yes_no('Does this file have column names already?')
#     if filename is not None:
#         with open(filename, "r") as infile:
#             reader = csv.reader(infile)
#             if button == 'Yes':
#                 header_list = next(reader)
#             try:
#                 data = list(reader)  # read everything else into a list of rows
#                 if button == 'No':
#                     header_list = ['column' + str(x) for x in range(len(data[0]))]
#             except:
#                 sg.popup_error('Error reading file')
#                 return
#     sg.set_options(element_padding=(0, 0))

# def create_csv(fileName, delimiter = ','):
#     file = CSVlibrary.CSVFile.csvFile(fileName, delimiter)
#     rows = file.rows
#     columns = file.columns
#     header_list = []
#     button = sg.popup_yes_no('Does this file have column names already?')
#     if button == 'Yes':
#         header_list = rows[0]
#         rows.remove(rows[0])
#         for i in columns:
#             i.remove(i[0])
#     if button == 'No':
#         header_list = ['column' + str(x) for x in range(len(data[0]))]
#     
#     # layout = [  [sg.Text('Select a File', size=(35, 1)), sg.Button('Create Table')],
#     #         [sg.In() ,sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
#     #         [sg.Text('Modify Data'), sg.InputText(), sg.Button('GO')],
#     #         [sg.Text('Add Data'), sg.InputText(), sg.Button('GO')],
#     #         [sg.Text('Retrieve Data'), sg.InputText(), sg.Button('GO')],
#     #         [sg.Text('Remove Data'), sg.InputText(), sg.Button('GO')],
#     #         [sg.Table(values=rows,
#     #         headings=header_list,
#     #         max_col_width=25,
#     #         auto_size_columns=True,
#     #         justification='right',
#     #         # alternating_row_color='lightblue',
#     #         num_rows=min(len(rows), 20))]
#     #     ]
#     return [header_list, rows]

# def update_table(rows, header):
#     layout.append([sg.Table(values=rows, key='table', headings = header, max_col_width=25, auto_size_columns=True, justification='right', num_rows=min(len(rows), 20))])
    


# rows = [['a'], ['b']]
# header_list = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
# layout = [  [sg.Text('Select a File', size=(35, 1)), sg.Button('Create Table')],
#             [sg.In() ,sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
#             [sg.Text('Modify Data'), sg.InputText(), sg.Button('GO')],
#             [sg.Text('Add Data'), sg.InputText(), sg.Button('GO')],
#             [sg.Text('Retrieve Data'), sg.InputText(), sg.Button('GO')],
#             [sg.Text('Remove Data'), sg.InputText(), sg.Button('GO')],
#         ]

# window = sg.Window('CSVapp', layout, grab_anywhere=False)
# while True:             # Event Loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == 'Create Table':
#         print(values[0])
#         rows = create_csv(values[0])       # call the "Callback" function
#         print(rows)
#         update_table(rows[1], rows[0])
#         event, values = window.read()

# window.close()

# import PySimpleGUI as sg
# import time, random

# contents = [[0, 'Temperature', 0], [1, 'Pressure', 0]]
# layout = [[sg.Table(values=contents, headings=['ID', 'Sensor', 'Reading'], key='table', enable_events=True)],
#           [sg.T('Selected Row: None ', key='sr')],
#           [sg.Button('Delete Row')],
#           ]

# window = sg.Window('', layout=layout)

# timer = 0
# selected_row = None


# def update_table():
#     window.Element('table').Update(values=contents)
#     window.Element('sr').Update('Selected Row: %s' % selected_row)

#     # need something like this to keep same row selected (highlighted)
#     # if selected_row:
#     #     window.Element('table').Update(selected_row=selected_row)


# while True:
#     e, v = window.Read(timeout=100)

#     if e == 'None' or e is None:
#         break

#     elif e == 'table':
#         selected_row = v['table'][0]
#         window.Element('sr').Update('Selected Row: %s' % selected_row)

#     elif e == 'Delete Row':
#         if selected_row is not None:
#             contents.pop(selected_row)
#             selected_row = None
#             update_table()

#     # run every 2 seconds
#     if time.time() - timer >= 2:
#         timer = time.time()
#         for item in contents:
#             item[2] = random.randint(1, 101)
#         update_table()

import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window
    Window 1 launches window 2
    BOTH remain active in parallel
    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active
    Copyright 2020 PySimpleGUI.org
"""
def make_win1():
    # layout = [[sg.Text('This is the FIRST WINDOW'), sg.Text('      ', k='-OUTPUT-')],
    #           [sg.Button('Launch 2nd Window'), sg.Button('Exit')]]
    layout = [  [sg.Text('Welcome to CSVapp!')],
            [sg.Text('Press the Help button for more information on commands.')],
            [sg.Text('Select a File', size=(35, 1))],
            [sg.In() ,sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
            [sg.Text('Delimiter'), sg.In(',')],
            [sg.InputText(), sg.Button('Modify Data')],
            [sg.InputText(), sg.Button('Add Data')],
            [sg.InputText(),sg.Button('Retrieve Data')],
            [sg.InputText(), sg.Button('Remove Data')],
            [sg.Button('Create Table', pad=(215, 0))]
        ]
    return sg.Window('CSVapp', layout, location=(800,600), finalize=True, size=(1000, 1000))

def make_win2(layout):
    
    return sg.Window('CSVapp Table', layout, finalize=True)

def make_win3(layout):
    return sg.Window('CSVapp Table', layout, finalize=True)

def list_to_string(list):
    string = ''
    for i in list:
        string = string + str(i)

def create_csv(fileName, delimiter = ','):
    global file
    file = CSVFile.csvFile(fileName, delimiter)
    rows = file.rows
    columns = file.columns
    global header_list
    header_list = []
    button = sg.popup_yes_no('Does this file have column names already?')
    if button == 'Yes':
        header_list = rows[0]
        rows.remove(rows[0])
        for i in columns:
            i.remove(i[0])
    if button == 'No':
        header_list = ['column ' + str(x) for x in range(len(rows[0]))]
    global interpreter
    interpreter = CSVlibraryInterpreter.interpreter(file, header_list)
    return [rows, header_list]

main, table = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == table:       # if closing win 2, mark as closed
            table = None
        elif window == main:     # if closing win 1, exit program
            break
    elif event == 'Create Table' and not table:
        global x
        delimiter = values[1]
        x = create_csv(values[0],delimiter)
        layout = [[sg.Text(file.fileName)],
              [sg.Table(values=x[0], key='table', headings = x[1], max_col_width=25, auto_size_columns=True, vertical_scroll_only=False, justification='right', num_rows=min(len(x[0]), 20))],
              [sg.Button('Exit to Continue')]]
        table = make_win2(layout)
    elif event == 'Modify Data':
        command = values[2]
        if command[0] == 'row':
            interpreter.interpret('crow, ' + command)
        elif command[0] == 'column':
            interpreter.interpret('ccol, ' + command)
        elif command[0] == 'cell':
            interpreter.interpret('ccel, ' + command)
    elif event == 'Add Data':
        command = values[3]
        command = command.split(', ')
        if command[0] == 'row':
            data = command[1:]
            command[0]='irow'
            interpreter.interpret(command)
        elif command[0] == 'column':
            data = command[1:]
            command[0] = 'icol'
            header_list.append(command[1])
            interpreter.interpret(command)
    elif event == 'Retrieve Data':
        command = values[4]
        command = command.split(', ')
        if command[0] == 'row':
            command[0] = 'rrow'
            get = interpreter.interpret(command)
            get = [get]
            layout_3 = [[sg.Table(values=get, headings=header_list, key='table', max_col_width=25, auto_size_columns=True, vertical_scroll_only=False, justification='right', num_rows=min(len(get), 20))]]
            make_win2(layout_3)
        elif command[0] == 'column':
            command[0] = 'rcol'
            get = interpreter.interpret(command)
            layout_3 = [[sg.Text(get)]]
            header = header_list[int(command[1])]
            header = [header]
            layout_3 = [[sg.Table(values=get, headings=header, key='table', max_col_width=25, auto_size_columns=True, vertical_scroll_only=False, justification='right', num_rows=min(len(get), 20))]]
            make_win2(layout_3)
        elif command[0] == 'cell':
            command[0] = 'rcel'
            get = interpreter.interpret(command) 
            layout_3 = [[sg.Text(get)]]
            make_win2(layout_3)
    elif event == 'Remove Data':
        command = values[5]
        pass
window.close()