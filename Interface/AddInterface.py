from .interface import interface
from utility import is_valid_title_str, is_valid_date_str, input_menu
class AddInterface(interface):
    def __init__(self, file_manager):
        self.file_manager=file_manager
        self.range = 1
        self.err_message = "오류: 잘못 된 입력 입니다. 다시 입력해 주세요"

    def CLI(self):
        self.add_todo()##할일 추가
        self.text = "<할일 추가하기>\n"
        self.text += "할일을 추가하였습니다. 계속 추가하시곘습니까?\n"
        self.text += "1. 계속 추가하기\n"
        self.text += "0. 돌아가기\n"
        self.text += "TODO/추가>"
        return super().CLI()

    def add_todo(self):
        self.ask_title()
        self.ask_date()
        self.ask_repeat()
        self.file_manager.add_todo([self.title, self.date, self.repeat])


    def ask_title(self):
        text="<할일 추가하기>\n"
        text+="추가할 작업 이름을 입력해 주세요.\n"
        text+="TODO/할일추가 - 작업\n"
        title=input(text)
        while(True):
            if(is_valid_title_str(title)=="True"):
                self.title = title
                break
            else:
                print(is_valid_title_str(title))
                title=input(text)


    def ask_date(self):
        text="<할일 추가하기>\n"
        text+=" 작업: "+self.title+"\n\n"
        text+="추가할 할일의 마감일을 입력해 주세요.\n"
        text+="TODO/할일추가 - 작업\n"
        date=input(text)
        while(True):
            if(is_valid_date_str(date)=="True"):
                self.date = date
                break
            else:
                print(is_valid_date_str(date))
                date=input(text)

    def ask_repeat(self):
        text="<할일 추가하기>\n"
        text+=" 작업: "+self.title+"\n"
        text+=" 마감일: "+self.date+"\n\n"
        text+="반복 여부를 선택하세요.\n" \
              " - 매주 옵션의 경우 요일 기준으로 반복이 설정됩니다.\n" \
              " - 매달 / 매년의 경우 날짜 기준으로 반복이 설정 됩니다.\n" \
              " 만약 해당되는 날짜가 그 달에 없다면 달의 말일로 설정됩니다.\n\n" \
              "  1. 없음\n" \
              "  2. 매주\n" \
              "  3. 매달\n" \
              "  4. 매년\n"
        text+="TODO/할일추가 - 작업\n"
        menu_list=["-","없음","매주","매달","매년"]
        self.repeat=menu_list[input_menu(1,5,text)]