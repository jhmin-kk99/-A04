from interface import interface
from FileManager import FileManager
class ListInterface(interface):
    def __init__(self, file_manager):
        self.file_manager=file_manager
        self.filteredData = self.file_manager.filter_todolist()
        self.err_message = "오류: 잘못 된 입력 입니다. 이동하려는 할일의 번호를 정확히 숫자로 입력해 주세요"
        self.range = len(self.filteredData)

    def CLI(self):
        self.filteredData = self.file_manager.filter_todolist()
        printData=self.filteredData.drop(columns=['Index'])
        printData.index=range(1,len(printData)+1)
        self.text = "<TODO List>\n"
        if(len(printData)==0):
            self.text+="할일이 없습니다."
        else:
            self.text += printData.to_string()
        self.text+="\n0. 돌아가기"
        self.text += "\nTODO/할일>"
        if(len(printData)==0):
            input("할일이 없습니다. 아무키나 입력하면 돌아갑니다.")##예외처리
            return 0
        return super().CLI()
    def get_index_by_user(self, num):
        return self.filteredData.iloc[num-1]['Index']