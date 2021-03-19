import PySimpleGUI as sg
import csv
import CSVFile
import CSVlibraryValidator
import CSVlibraryInterpreter
sg.theme('Default 1')
# for table example, https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Table_CSV.py
# On how to browse files: https://stackoverflow.com/questions/57443004/pysimplegui-file-browser-specific-file-type
# On how to make multiple windows: https://www.blog.pythonlibrary.org/2021/01/20/pysimplegui-working-with-multiple-windows/

# Main window
def make_win1():
    layout = [  [sg.Text('Welcome to CSVapp!')],
            [sg.Text('To begin, select a file and delimiter and press the Create Table button.')],
            [sg.Text('Press the Help button for more information on commands and use of the program.')],
            [sg.Text('Select a File', size=(10, 1)), sg.In() ,sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
            [sg.Text('Delimiter', size=(10, 1)), sg.In(',')],
            [sg.Text('_'*80)],
            [sg.InputText(), sg.Button(' Modify Data ')],
            [sg.InputText(), sg.Button('   Add Data   ')],
            [sg.InputText(),sg.Button('Retrieve Data')],
            [sg.InputText(), sg.Button('Remove Data')],
            [sg.Button('Create Table', pad=((250, 0), 20))],
            [sg.Button('HELP')]
        ]
    return sg.Window('CSVapp', layout, location=(0,0), finalize=True, size=(600, 400))

# Table window
def make_win2(layout):
    
    return sg.Window('CSVapp Table', layout, finalize=True, keep_on_top=True)

# Function to create a csv object
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

main, table = make_win1(), None
# Main loop
while True:
    window, event, values = sg.read_all_windows()
    try:
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == table:
                table = None
            elif window == main:
                break

        elif event == 'Create Table' and not table:
            global x
            delimiter = values[1]
            x = create_csv(values[0],delimiter)
            layout = [[sg.Text(file.fileName)],
                [sg.Table(values=x[0], key='table', headings = x[1], max_col_width=25, auto_size_columns=True, vertical_scroll_only=False, justification='right', num_rows=min(len(x[0]), 20))]]
            table = make_win2(layout)

        elif event == 'Modify Data':
            command = values[2]
            command = command.split(', ')
            if command[0] == 'row':
                command[0] = 'crow'
                interpreter.interpret(command)
                update = ['update']
                interpreter.interpret(update)
                delimiter = values[1]

            elif command[0] == 'column':
                command[0] = 'ccol'
                interpreter.interpret(command)
                update = ['update']
                interpreter.interpret(update)

            elif command[0] == 'cell':
                command[0] = 'ccel'
                interpreter.interpret(command)
                update = ['update']
                interpreter.interpret(update)

        elif event == 'Add Data':
            command = values[3]
            command = command.split(', ')
            if command[0] == 'row':
                command[0]='irow'
                interpreter.interpret(command)
                update = ['update']
                interpreter.interpret(update)

            elif command[0] == 'column':
                data = command[1:]
                command[0] = 'icol'
                interpreter.interpret(command)
                header_list.append(command[1])
                update = ['update']
                interpreter.interpret(update)


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
            command = command.split(', ')
            if command[0] == 'row':
                command[0] = 'drow'
                interpreter.interpret(command)

            elif command[0] == 'column':
                command[0] = 'dcol'
                interpreter.interpret(command)
                header_list[int(command[1])] = None
                update = ['update']
                interpreter.interpret(update)

            elif command[0] == 'cell':
                command[0] = 'dcel'
                interpreter.interpret(command)
                update = ['update']
                interpreter.interpret(update)

        elif event == 'HELP':
            layout = [
                [sg.Text('CSVapp Instructions\n')],
                [sg.Text('HOW TO START')],
                [sg.Text('To begin, you must create a table using the desired filename and delimiter.')],
                [sg.Text('Browse your files for the desired CSV file, insert a delimiter or use the default comma. Then press the create table button located at the bottom of the window.\n')],
                [sg.Text('MODIFY DATA')],
                [sg.Text('To modify data, enter text into the field next to the "Modify Data" button in the following format:')],
                [sg.Text('(column/row/cell), index, (data seperated by ", ")')],
                [sg.Text('example:')],
                [sg.Text('column, 1, Number, 2, 3, 4, 5, 6\n')],
                [sg.Text('ADD DATA')],
                [sg.Text('To add data, enter text into the field next to the "Add Data" button in the following format:')],
                [sg.Text('(column/row), (data seperated by ", ")')],
                [sg.Text('example:')],
                [sg.Text('column, Number, 2, 3, 4, 5, 6\n')],
                [sg.Text('RETRIEVE DATA')],
                [sg.Text('To retrieve data, enter text into the field next to the "Retrieve Data" button in the following format:')],
                [sg.Text('(column/row/cell), index')],
                [sg.Text('example:')],
                [sg.Text('column, 1\n')],
                [sg.Text('REMOVE DATA')],
                [sg.Text('To remove data, enter text into the field next to the "Remove Data" button in the following format:')],
                [sg.Text('(column/row/cell), index')],
                [sg.Text('example:')],
                [sg.Text('column, 1')]
            ]
            make_win2(layout)
    except Exception as e:
        sg.popup(f'AN EXCEPTION OCCURRED!', e, keep_on_top=True)
window.close()