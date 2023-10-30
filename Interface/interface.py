class interface:
    def CLI(self):
        ## 0~ self.range까지 입력받음
        while (True):
            try:
                input_str = input(self.text)
                menu = int(input_str)
                if (menu < 0 or menu > self.range or len(input_str) != int(menu / 10) + 1):
                    print(self.err_message)
                    continue
                else:
                    return menu
            except ValueError:
                print(self.err_message)
