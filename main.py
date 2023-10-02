from FileManager import FileManager
from mainInterface import MainInterface
from listInterface import ListInterface

def main():
    main_interface = MainInterface()
    if(not file_manager.isValidFile()):
        return
    file_manager.sortTodoList()
    while True:
        menu=main_interface.CLI()
        if(menu==1):
            select_todo()
        elif (menu==2):
            add_todo()
        else:
            break

def select_todo():
    print("select_todo")
    # list_interface = ListInterface(file_manager)
    # list_menu=list_interface.CLI()

def add_todo():
    print("addtodo")

file_manager = FileManager()
main()