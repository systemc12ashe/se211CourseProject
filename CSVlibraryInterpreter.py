import CSVGetter as getter
import CSVSetter as setter

class interpreter:
    def __init__(self, file):
        self.file = file
        self.getter = getter.csvGetter(file)
        self.setter = setter.csvSetter(file)

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
            return True

        elif command == 'ccol':
            return True
            
        elif command == 'ccel':
            return True

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
            return True

        elif command == 'icol':
            return True

        else:
            #exit command
            exit
