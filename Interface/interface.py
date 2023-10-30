from utility import get_menu_input

class interface:
    def CLI(self):
        return get_menu_input(self.text, self.err_message, 0, self.range)
