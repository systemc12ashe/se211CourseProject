import CSVGetter as getter
import CSVSetter as setter
import CSVlibraryValidator as validator

class interpreter:
    def __init__(self, file):
        self.file = file
        self.getter = getter.csvGetter(file)
        self.setter = setter.csvSetter(file)
        self.validator = validator.validator()

    def interpret(self, command):
        if command == 'rtab':
            self.getter.return_table()

        elif command == 'rrow':
            print('Enter row index')
            row = int(input())
            self.getter.return_row(row)

        elif command == 'rcol':
            print('Enter column index')
            column = int(input())
            self.getter.return_column(column)

        elif command == 'rcel':
            print('Enter row index')
            row = int(input())
            print('Enter column index')
            column = int(input())
            self.getter.return_cell(row, column)

        elif command == 'crow':
            print('Enter row index')
            index = int(input())
            print('Enter data seperated by commas')
            data = input().split(',')
            if self.validator.validate_row(data,  len(self.file.rows[0])):
                self.setter.change_row(index, data)
            else:
                print('Invalid Data')

        elif command == 'ccol':
            print('Enter column index')
            index = int(input())
            print('Enter data seperated by commas')
            data = input().split(',')
            if self.validator.validate_column(data, len(self.file.columns[0])):
                self.setter.change_column(index, data)
            else:
                print('Invalid Data')
            
        elif command == 'ccel':
            print('Enter row index')
            row = int(input())
            print('Enter column index')
            column = int(input())
            print('Enter data')
            data = input()
            self.setter.change_cell(row, column, data)

        elif command == 'drow':
            print('Enter row index')
            row = int(input())
            self.setter.change_row(row)

        elif command == 'dcol':
            print('Enter column index')
            column = int(input())
            self.setter.change_column(column)

        elif command == 'dcel':
            print('Enter row index')
            row = int(input())
            print('Enter column index')
            column = int(input())
            self.setter.change_cell(row, column)

        elif command == 'irow':
            print('Enter data seperated by commas')
            new_row = input().split(',')
            if self.validator.validate_row(new_row,  len(self.file.rows[0])):
                self.setter.insert_row(new_row)
            else:
                print('Invalid Data')

        elif command == 'icol':
            print('Enter data seperated by commas')
            new_column = input().split(',')
            if self.validator.validate_column(new_column, len(self.file.columns[0])):
                self.setter.insert_column(new_column)
            else:
                print('Invalid Data')

        else:
            #exit command
            exit
