class csvGetter:
    def return_table(self):
        for row in self.rows:
            print(row)

    def return_column(self, index):
        print(self.columns[index])

    def return_row(self, index):
        print(self.rows[index])

    def return_cell(self, x, y):
        row = self.rows[x]
        cell = row[y]
        print(cell)