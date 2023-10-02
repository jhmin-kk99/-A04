from FileManager import FileManager
from mainInterface import MainInterface
def main():
    file_manager=FileManager()
    main_interface = MainInterface()
    if(not file_manager.isValidFile()):
        return
    file_manager.sortTodoList()
    while True:
        menu=main_interface.CLI()
        if(menu==1):
            print(1)
        elif (menu==2):
            print(2)
        else:
            break

main()