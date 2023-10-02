class interface:
    def CLI(self):
        while (True):
            try:
                menu = int(input(self.text))
                if (menu < 0 or menu > self.range):
                    print(self.err_message)
                    continue
                else:
                    return menu
            except ValueError:
                print(self.err_message)
