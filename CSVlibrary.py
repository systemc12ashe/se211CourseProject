import csv
import CSVFile
import CSVlibraryValidator as validator
import CSVlibraryInterpreter as interpreter

def print_commands():
    print('Enter a command')
    print('RTAB - Return Table')
    print('RROW - Return Row')
    print('RCOL - Return Column')
    print('RCEL - Return Cell')
    print('CROW - Change Row')
    print('CCOL - Change Column')
    print('CCEL - Change Cell')
    print('DROW - Delete Row')
    print('DCOL - Delete Column')
    print('DCEL - Delete Cell')
    print('IROW - Insert Row')
    print('ICOL - Insert Column')
    print('SAVE - Writes working table to file')
    print('EXIT - Exit program')


if __name__ == "__main__":
    print('Input File Name')
    fileName = str(input())
    file = CSVFile.csvFile(fileName)
    validator = validator.validator()
    interpreter = interpreter.interpreter(file)
    loop = True
    
    while loop:
        print_commands()
        command = input()
        command.strip()
        command.lower()
        if validator.validate_command(command):
            if command == "exit":
                print('Exiting CSVlibrary')
                loop = False
            interpreter.interpret(command)
        print()

                