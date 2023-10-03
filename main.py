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
                self.select_todo()
            elif menu == 2:
                self.add_todo()
                self.select_todo()
            else:
                break

    def add_todo(self):
        add_interface = AddInterface(self.file_manager)
        while True:
            menu = add_interface.CLI()
            if menu == 0:
                return

    def select_todo(self):
        list_interface = ListInterface(self.file_manager)
        while True:
            menu = list_interface.CLI()
            if menu == 0:
                return
            index = list_interface.get_index_by_user(menu)
            self.detail_todo(index)

    def detail_todo(self, index):
        detail_interface = DetailInterface(index, self.file_manager)
        while True:
            menu = detail_interface.CLI()
            if menu == 0:
                return
            elif menu == 2:
                detail_interface.delete_todo()
                return
            else:
                self.edit_todo(detail_interface)

    def edit_todo(self, detail_interface):
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

app = TodoApp()
app.run()
