from interface import interface
from utility import is_valid_date_str,is_valid_title_str
class EditInterface(interface):
    def __init__(self, detail):
        self.detail = detail
        self.index = detail.index
        self.file_manager = detail.file_manager
        self.err_message="오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        self.range=3


    def CLI(self):
        self.text = "<할일 수정하기>"
        todo=self.file_manager.getDataByIndex(self.index)
        self.todoText="\n작업: "+todo[0]+"\n마감: "+todo[1]+"\n반복: "+todo[2]+"\n"
        self.text+=self.todoText
        self.text+="\n1.작업 수정하기" \
                   "\n2.마감 삭제하기" \
                   "\n3.반복 삭제하기" \
                   "\n0. 돌아가기\n"
        self.text += "\nTODO/할일 수정>"
        return super().CLI()

    def edit_title(self):
        text="<할일 수정하기>"
        text+=self.todoText+"\n변경될 작업 이름을 입력하세요."
        text+="TODO/할일 수정 - 작업>"
        while True:
            title=input(text)
            is_valid=is_valid_title_str(title)
            if(is_valid == "True"):
                break
            else:
                print(is_valid)
        self.file_manager.editTodo(self.index,'작업 이름',title)

    def edit_date(self):
        text="<할일 수정하기>"
        text+=self.todoText+"\n변경될 마감일을 입력하세요."
        text+="TODO/할일 수정 - 마감>"
        while True:
            date=input(text)
            is_valid=is_valid_date_str(date)
            if(is_valid == "True"):
                break
            else:
                print(is_valid)
        self.file_manager.editTodo(self.index,'마감 날짜',date)

    def edit_repeat(self):
        text = "<할일 수정하기>"
        text += self.todoText + "\n반복 여부을 입력하세요."
        text+="반복 여부를 선택하세요.\n 1. 없음\n 2. 매주\n 3. 매달\n 4. 매년\n"
        text += "TODO/할일 수정 - 반복>"
        range=4
        err_message="오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        while (True):
            try:
                menu = int(input(text))
                if (menu <= 0 or menu > range):
                    print(err_message)
                    continue
                else:
                    break
            except ValueError:
                print(err_message)
        self.file_manager.editTodo(self.index,'반복', menu)