class csvGetter:
    def __init__(self, csvFile):
        self.csvFile = csvFile

    def return_table(self):
        for row in self.csvFile.rows:
            print(row)

    def return_column(self, index):
        print(self.csvFile.columns[index])

    def return_row(self, index):
        print(self.csvFile.rows[index])

    def return_cell(self, x, y):
        row = self.csvFile.rows[x]
        cell = row[y]
        print(cell)