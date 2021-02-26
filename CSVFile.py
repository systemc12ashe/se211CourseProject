import csv

class csvFile:
    def __init__(self, fileName):
        self.fileName = fileName
        self.rows = []
        self.get_rows()
        self.columns = []
        width = len(self.rows)
        i = 0
        while i < width:
            self.columns.append([])
            i+=1
        self.get_columns()

    def get_columns(self):
        with open(self.fileName, 'r') as csvFile:
            csv_reader = csv.reader(csvFile)
            width = len(self.rows[0])
            for row in csv_reader:
                i = 0
                while i < width:
                    self.columns[i].append(row[i])
                    i+=1

    def get_rows(self):
        with open(self.fileName, 'r') as csvFile:
            csv_reader = csv.reader(csvFile)
            for row in csv_reader:
                self.rows.append(row)