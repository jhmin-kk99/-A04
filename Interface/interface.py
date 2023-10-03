class interface:
    def CLI(self):
        ## 0~ self.range까지 입력받음
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
