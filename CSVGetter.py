class csvGetter:
    def __init__(self, csvFile):
        self.csvFile = csvFile

    def return_table(self):
        x = []
        for row in self.csvFile.rows:
            x.append(row)
        return x

    def return_column(self, index):
        return self.csvFile.columns[index]

    def return_row(self, index):
        return self.csvFile.rows[index]

    def return_cell(self, x, y):
        row = self.csvFile.rows[x]
        cell = row[y]
        return cell