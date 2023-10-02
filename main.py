from userInterFace import *
from FileManager import FileManager

def main():
    file_manager=FileManager()
    if(not file_manager.isValidFile()):
        return
    file_manager.sortTodoList()
    print(file_manager.filterTodoList())
    # while(True):
    #     menu=mainInterface()
    #     if(menu==1):
    #         todoListInterface()
    #     elif(menu==2):
    #         print(2)
    #     else:
    #         print("프로그램을 종료합니다.")
    #         exit()



main()