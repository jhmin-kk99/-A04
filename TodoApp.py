from FileManager import FileManager
from MainInterface import MainInterface
from ListInterface import ListInterface
from DetailInterface import DetailInterface
from AddInterface import AddInterface
from EditInterface import EditInterface

class TodoApp:
    def __init__(self):
        self.file_manager = FileManager()

    def run(self):
        if not self.file_manager.is_valid_file():
            return
        self.file_manager.sort_todolist()
        self.main_menu()

    def main_menu(self):
        main_interface = MainInterface()
        while True:
            menu = main_interface.CLI()
            if menu == 1:
                self.select_menu()
            elif menu == 2:
                self.add_menu()
                self.select_menu()
            else:
                break

    def add_menu(self):
        add_interface = AddInterface(self.file_manager)
        while True:
            menu = add_interface.CLI()
            if menu == 0:
                return

    def select_menu(self):
        list_interface = ListInterface(self.file_manager)
        while True:
            menu = list_interface.CLI()
            if menu == 0:
                return
            index = list_interface.get_index_by_user(menu)
            self.detail_menu(index)

    def detail_menu(self, index):
        detail_interface = DetailInterface(index, self.file_manager)
        while True:
            menu = detail_interface.CLI()
            if menu == 0:
                return
            elif menu == 2:
                detail_interface.delete_todo()
                return
            else:
                self.edit_menu(detail_interface)

    def edit_menu(self, detail_interface):
        edit_interface = EditInterface(detail_interface)
        while True:
            menu = edit_interface.CLI()
            if menu == 1:
                edit_interface.edit_title()
            elif menu == 2:
                edit_interface.edit_date()
            elif menu == 3:
                edit_interface.edit_repeat()
            else:
                break
