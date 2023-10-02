from EditInterface import EditInterface
from FileManager import FileManager
from mainInterface import MainInterface
from listInterface import ListInterface
from DetailInterface import DetailInterface
def main():
    main_interface = MainInterface()
    if(not file_manager.isValidFile()):
        return
    file_manager.sortTodoList()
    ##main stream 시작
    while True:
        menu=main_interface.CLI()
        if(menu==1):
            select_todo()
        elif (menu==2):
            add_todo()
        else:
            break

def select_todo():
    list_interface = ListInterface(file_manager)
    while True:
        menu=list_interface.CLI()
        if(menu==0):
            return
        detail_todo(list_interface.getIndexByUser(menu))

def detail_todo(index):
    detail_interface=DetailInterface(index,file_manager)
    while True:
        menu=detail_interface.CLI()
        if(menu==0):
            return
        elif(menu==2):
            detail_interface.delete_todo()
            return
        else:
            edit_todo(detail_interface)
            return

def edit_todo(detail_interface):
    edit_interface = EditInterface(detail_interface)
    while True:
        menu=edit_interface.CLI()
        if(menu==1):
            edit_interface.edit_title()
        elif(menu==2):
            edit_interface.edit_date()
        elif(menu==3):
            edit_interface.edit_repeat()
        else:
            break

def add_todo():
    print("addtodo")

file_manager = FileManager()
main()