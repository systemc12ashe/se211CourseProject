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
        print('Cell ({},{}) is now {}'.format(x, y, self.csvFile.rows[x]))

    def insert_row(self):
        pass