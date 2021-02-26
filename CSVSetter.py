class csvSetter:

    def change_column(self, index, values = None):
        height = len(self.columns[index])
        column = []
        if values == None:
            i = 0
            while i < height:
                column.append('')
                i+=1
        else:
            column = values
        self.columns[index] = column
        print(self.columns[index])

    def change_row(self, index, values = None):
        width = len(self.rows[index])
        row = []
        if values == None:
            i = 0
            while i < width:
                row.append('')
                i+=1
        else:
            row = values
        self.rows[index] = row
        print(self.rows[index])

    def change_cell(self, x, y, value = None):
        row = self.rows[x]
        if value == None:
            row[y] = None
        else:
            row[y] = value
        self.rows[x] = row
        print(self.rows[x])