class validator:
    def validate_fileName(self):
        pass

    def validate_command(self,command):
        if command == 'rtab':
            return True
        elif command == 'rrow':
            return True
        elif command == 'rcol':
            return True
        elif command == 'rcel':
            return True
        elif command == 'crow':
            return True
        elif command == 'ccol':
            return True
        elif command == 'ccel':
            return True
        elif command == 'drow':
            return True
        elif command == 'dcol':
            return True
        elif command == 'dcel':
            return True
        elif command == 'irow':
            return True
        elif command == 'icol':
            return True
        elif command == 'exit':
            return True
        else:
            self.invalid_command()

    def validate_column(self):
        pass

    def validate_row(self):
        pass

    def validate_cell(self):
        pass

    def invalid_command(self):
        print('Not a valid command.\n')