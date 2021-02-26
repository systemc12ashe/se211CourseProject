import csv
import CSVFile
import CSVGetter
import CSVSetter
import CSVlibraryValidator


if __name__ == "__main__":
    print('Input File Name\n')
    fileName = str(input())
    file = CSVFile.csvFile(fileName)
    # csvFile = csvFile('example.csv')
    # csvFile.return_table()
    # csvFile.return_column(0)
    # csvFile.return_row(0)
    # csvFile.return_cell(0, 0)
    # csvFile.change_column(0,['a', 'b', 'c', 'd', 'e'])
    # csvFile.return_column(0)
    # csvFile.change_row(0,['a', 'b', 'c', 'd', 'e'])
    # csvFile.return_row(0)
    # csvFile.change_cell(0, 0,'X')
    # csvFile.return_cell(0, 0)

                