import CSVGetter as getter
import CSVSetter as setter
import CSVlibraryValidator as validator

class interpreter:
    def __init__(self, file, header_list):
        self.file = file
        self.getter = getter.csvGetter(file)
        self.setter = setter.csvSetter(file)
        self.validator = validator.validator()
        self.header_list = header_list

    def interpret(self, command):
        if command[0] == 'rtab':
            self.getter.return_table()

        elif command[0] == 'rrow':
            # print('Enter row index')
            row = int(command[1])
            r = self.getter.return_row(row)
            return r

        elif command[0] == 'rcol':
            # print('Enter column index')
            column = int(command[1])
            col = self.getter.return_column(column)
            return col

        elif command[0] == 'rcel':
            # print('Enter row index')
            row = int(command[1])
            # print('Enter column index')
            column = int(command[2])
            cell = self.getter.return_cell(row, column)
            return cell

        elif command[0] == 'crow':
            # print('Enter row index')
            index = int(command[1])
            # print('Enter data seperated by commas')
            data = command[2:]
            if self.validator.validate_row(data,  len(self.file.rows[0])):
                self.setter.change_row(index, data)
            else:
                print('Invalid Data')

        elif command[0] == 'ccol':
            # print('Enter column index')
            index = int(command[1])
            # print('Enter data seperated by commas')
            data = command[3:]
            self.header_list[index] = command[2]
            if self.validator.validate_column(data, len(self.file.columns[0])):
                self.setter.change_column(index, data)
            else:
                print('Invalid Data')
            
        elif command[0] == 'ccel':
            # print('Enter row index')
            row = int(command[1])
            # print('Enter column index')
            column = int(command[2])
            # print('Enter data')
            data = command[3]
            self.setter.change_cell(row, column, data)

        elif command[0] == 'drow':
            # print('Enter row index')
            row = int(command[1])
            self.setter.change_row(row)

        elif command[0] == 'dcol':
            # print('Enter column index')
            column = int(command[1])
            self.setter.change_column(column)

        elif command[0] == 'dcel':
            # print('Enter row index')
            row = int(command[1])
            # print('Enter column index')
            column = int(command[2])
            self.setter.change_cell(row, column)

        elif command[0] == 'irow':
            # print('Enter data seperated by commas')
            new_row = command[1:]
            if self.validator.validate_row(new_row,  len(self.file.rows[0])):
                self.setter.insert_row(new_row)
                print(self.file.rows)
            else:
                print('Invalid Data')

        elif command[0] == 'icol':
            # print('Enter data seperated by commas')
            new_column = command[2:]
            if self.validator.validate_column(new_column, len(self.file.columns[0])):
                self.setter.insert_column(new_column)
            else:
                print('Invalid Data')
        elif command[0] == 'update':
            self.setter.update_file(self.header_list)

        else:
            #exit command
            exit
