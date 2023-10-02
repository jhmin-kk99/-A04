from interface import interface
from FileManager import FileManager
class ListInterface(interface):
    def __init__(self, file_manager):
        self.file_manager=file_manager
        self.filteredData = self.file_manager.filterTodoList()
        self.err_message = "오류: 잘못 된 입력 입니다. 이동하려는 할일의 번호를 정확히 숫자로 입력해 주세요"
        self.range = len(self.filteredData)

    def CLI(self):
        self.filteredData = self.file_manager.filterTodoList()
        printData=self.filteredData.drop(columns=['Index'])
        printData.index=range(1,len(printData)+1)
        self.text = "<TODO List>\n"
        self.text += printData.to_string()
        self.text += "\nTODO/할일>"
        return super().CLI()
    def getIndexByUser(self,num):
        return self.filteredData.iloc[num-1]['Index']