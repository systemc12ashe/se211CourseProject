import csv

class csvFile:
    def __init__(self, fileName, delimiter):
        self.fileName = fileName
        self.delimiter = delimiter
        self.rows = []
        self.get_rows()
        print(self.rows)
        self.columns = []
        
        width = len(self.rows[0])
        i = 0
        while i < width:
            self.columns.append([])
            i+=1
        self.get_columns()

    def get_rows(self):
        with open(self.fileName, 'r') as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=self.delimiter)
            for row in csv_reader:
                self.rows.append(row)
        

    def get_columns(self):
        with open(self.fileName, 'r') as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=self.delimiter)
            width = len(self.rows[0])
            for row in csv_reader:
                i = 0
                while i < width:
                    self.columns[i].append(row[i])
                    i+=1
                    

    def save_changes(self):
        with open(self.fileName, mode='w') as csvFile:
            csvFile_writer = csv.writer(csvFile, delimiter=self.delimiter, quotechar="'", quoting=csv.QUOTE_MINIMAL)

            for i in self.rows:
                csvFile_writer.writerow(i)
    
if __name__ == '__main__':
    file = csvFile('example.csv', '/')