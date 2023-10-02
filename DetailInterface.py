from interface import interface
class DetailInterface(interface):
    def __init__(self,index,file_manager):
        self.file_manager=file_manager
        self.index=index
        self.err_message="오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        self.range=2

    def CLI(self):
        todo=self.file_manager.getDataByIndex(self.index)
        self.todoText="\n작업: "+todo[0]+"\n마감: "+todo[1]+"\n반복: "+todo[2]
        self.text = "\n<할일>"
        self.text+=self.todoText+"\n"
        self.text+="\n1. 수정하기" \
                   "\n2. 삭제하기" \
                   "\n0. 돌아가기\n"
        self.text += "\nTODO/할일 세부>"
        return super().CLI()

    def delete_todo(self):
        self.file_manager.deleteTodo(self.index)

