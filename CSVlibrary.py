import csv
import CSVFile
import CSVlibraryValidator as csvvalidator
import CSVlibraryInterpreter as csvinterpreter

# def print_commands():
#     print('Enter a command')
#     print('RTAB - Return Table')
#     print('RROW - Return Row')
#     print('RCOL - Return Column')
#     print('RCEL - Return Cell')
#     print('CROW - Change Row')
#     print('CCOL - Change Column')
#     print('CCEL - Change Cell')
#     print('DROW - Delete Row')
#     print('DCOL - Delete Column')
#     print('DCEL - Delete Cell')
#     print('IROW - Insert Row')
#     print('ICOL - Insert Column')
#     print('EXIT - Exit program')


# print('Input File Name')
# fileName = str(input())
# print('Input File Delimiter')
# delimiter = str(input())
# file = CSVFile.csvFile(fileName, delimiter)
# validator = csvvalidator.validator()
# interpreter = csvinterpreter.interpreter(file)
# loop = True

# while loop:
#     print_commands()
#     command = input()
#     command.strip()
#     command.lower()
#     if validator.validate_command(command):
#         if command == "exit":
#             print('Exiting CSVlibrary')
#             loop = False
#         interpreter.interpret(command)
#         file.save_changes()
#     print()