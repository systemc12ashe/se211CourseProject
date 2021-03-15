import csv
class csvSetter:
    def __init__(self, csvFile):
        self.csvFile = csvFile

    def change_column(self, index, values = None):
        height = len(self.csvFile.columns[index])
        column = []
        if values == None:
            i = 0
            while i < height:
                column.append(None)
                i+=1
        else:
            column = values
        self.csvFile.columns[index] = column
        i = 0
        while i < len(self.csvFile.rows):
            row = self.csvFile.rows[i]
            row[index] = column[i]
            self.csvFile.rows[i] = row
            i+=1
        print('Column {} is now {}'.format(index, self.csvFile.columns[index]))

    def change_row(self, index, values = None):
        width = len(self.csvFile.rows[index])
        row = []
        if values == None:
            i = 0
            while i < width:
                row.append(None)
                i+=1
        else:
            row = values
        self.csvFile.rows[index] = row
        print('Row {} is now {}'.format(index, self.csvFile.rows[index]))

    def change_cell(self, x, y, value = None):
        row = self.csvFile.rows[x]
        if value == None:
            row[y] = None
        else:
            row[y] = value
        self.csvFile.rows[x] = row
        print('Cell ({},{}) is now {}'.format(x, y, row[y]))

    def insert_row(self, data, header_row):
        self.csvFile.rows.append(data)
        with open(self.csvFile.fileName, 'w') as csvfile:  
            csvwriter = csv.writer(csvfile, lineterminator = '\n')  
            list = self.csvFile.rows
            list.insert(0, header_row)
            csvwriter.writerows(list) 

    def insert_column(self, data, header_row):
        self.csvFile.columns.append(data)
        i = 0
        while i < len(data):
            self.csvFile.rows[i].append(data[i])
            i+=1
        with open(self.csvFile.fileName, 'w') as csvfile:  
            # creating a csv writer object  
            csvwriter = csv.writer(csvfile, lineterminator = '\n')  
            
            list = self.csvFile.rows
            list.insert(0, header_row)
            # writing the data rows  
            csvwriter.writerows(list) 