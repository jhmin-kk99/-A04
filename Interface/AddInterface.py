from .interface import interface
from utility import is_valid_title_str, is_valid_date_str, \
    input_menu, is_valid_day_detail_str, is_valid_month_detail_str, is_valid_year_detail_str, diff_date, is_valid_theme


class AddInterface(interface):
    def __init__(self, todo_manager):
        self.todo_manager = todo_manager
        self.range = 1
        self.err_message = "오류: 잘못 된 입력 입니다. 다시 입력해 주세요"
        self.today = self.todo_manager.TODAY

    def CLI(self):
        self.add_todo()  ##할일 추가
        self.text = "<할일 추가하기>\n"
        self.text += "할일을 추가하였습니다. 계속 추가하시곘습니까?\n"
        self.text += "1. 계속 추가하기\n"
        self.text += "0. 돌아가기\n"
        self.text += "TODO/추가>"
        return super().CLI()

    def add_todo(self):
        self.ask_title()
        self.ask_repeat()
        self.ask_repeat_detail()
        self.ask_finish_date()
        self.ask_start_date()
        self.ask_stop_repeat()
        self.ask_theme()
        ##작업 이름,마감 날짜,시작 날짜,반복,반복 세부,반복 정지,완료,분류
        self.todo_manager.add_todo([self.title, self.finish_date,self.diff ,self.repeat
                                     , self.repeat_detail, self.stop_repeat,"x",self.theme])

    def ask_title(self):
        text = "<할일 추가하기>\n"
        text += "추가할 작업 이름을 입력해 주세요.\n"
        text += "TODO/할일추가 - 작업\n"
        title = input(text)
        while (True):
            if (is_valid_title_str(title) == "True"):
                self.title = title
                break
            else:
                print(is_valid_title_str(title))
                title = input(text)
        self.middle_text="작업: " + self.title + "\n"

    def ask_repeat(self):
        text = "<할일 추가하기>\n"
        text += self.middle_text
        text += "반복 여부를 선택하세요.\n" \
                " - 매주 옵션의 경우 요일 기준으로 반복이 설정됩니다.\n" \
                " - 매달 / 매년의 경우 날짜 기준으로 반복이 설정 됩니다.\n" \
                " 만약 해당되는 날짜가 그 달에 없다면 달의 말일로 설정됩니다.\n\n" \
                "  1. 없음\n" \
                "  2. 매주\n" \
                "  3. 매달\n" \
                "  4. 매년\n"
        text += "TODO/할일추가 - 작업\n"
        menu_list = ["-", "없음", "매주", "매달", "매년"]
        self.repeat = menu_list[input_menu(1, 4, text)]
        self.middle_text+= "반복: " + self.repeat + "\n"

    def ask_repeat_detail(self):
        self.repeat_detail = "x"
        text = "<할일 추가하기>\n"
        text += self.middle_text
        
        if (self.repeat == "매주"):
            while True:
                message = input("반복 요일을 선택하세요. ex) 월/화/수\n")
                ret = is_valid_day_detail_str(message)
                if (ret == "True"):
                    self.repeat_detail = message
                    break
                else:
                    print(ret)
        elif (self.repeat == "매달"):
            while True:
                message = input("반복 날짜를 선택하세요. ex) 1/2/3.../31\n")
                ret = is_valid_month_detail_str(message)
                if (ret == "True"):
                    self.repeat_detail = message
                    break
                else:
                    print(ret)
        elif (self.repeat == "매년"):
            while True:
                message = input("반복 날짜를 선택하세요. ex)12-31/10-13\n")
                ret = is_valid_year_detail_str(message)
                if (ret == "True"):
                    self.repeat_detail = message
                    break
                else:
                    print(ret)
        self.middle_text+= "반복 세부: " + self.repeat_detail + "\n"


    def ask_stop_repeat(self):
        text = "<할일 추가하기>\n"
        text+=self.middle_text
        text += "추가할 작업의 반복 정지일을 입력해 주세요.\n"
        text += "TODO/할일추가 - 반복 정지일 (무한 반복이면 'x' 입력)\n"
        while (True):
            date = input(text)
            if (date == "x"):
                    self.stop_repeat = date
                    break
            if (is_valid_date_str(date) == "True"):
                self.stop_repeat = date
                break
            else:
                print(is_valid_date_str(date))
        self.middle_text+= "반복 정지: " + self.stop_repeat + "\n"


    def ask_finish_date(self):
        text = "<할일 추가하기>\n"
        text +=self.middle_text
        text += "추가할 할일의 마감 날짜를 입력해 주세요.\n" \
                "마감 날짜(반복을 시작하는 경계 날짜)\n" \
                "만약 반복: 없음으로 설정했다면, 마감 날짜가 마감일이 됩니다.\n"
        text += "TODO/할일추가 - 마감 날짜\n"
        while (True):
            date = input(text)
            if (is_valid_date_str(date) == "True"):
                self.finish_date = date
                break
            else:
                print(is_valid_date_str(date))
        self.middle_text+= "마감 날짜: " + self.finish_date + "\n"

    def ask_start_date(self):
        text = "<할일 추가하기>\n"
        text +=self.middle_text
        text += "추가할 할일의 시작일을 입력해 주세요.\n" \
                "시작일: TODO를 완료로 설정할 수 있는 일수(마감일 x일 전부터 완료 가능의 x)\n"
        text += "TODO/할일추가 - 시작일(시작일이 없다면 'x'를 입력하세요.)\n"
        while (True):
            date = input(text)
            if (date == "x"):
                self.start_date = "x"
                self.diff = "x"
                break
            elif (is_valid_date_str(date) == "True"):
                self.diff = diff_date(self.finish_date, date)
                if (self.diff < 0):
                    print("오류: 시작일이 마감 날짜보다 늦습니다.")
                    continue
                else:
                    self.start_date = date
                break
            else:
                print(is_valid_date_str(date))

    def ask_theme(self):
        text = "<할일 추가하기>\n"
        text += self.middle_text
        text += "추가할 할일의 분류를 입력해 주세요.\n" \
                "예시: 일상+공부 or 일상\n"
        text += "TODO/할일추가 - 분류\n"
        while (True):
            theme = input(text)
            if (is_valid_theme(theme)):
                break
            else:
                print("오류: 분류를 다시 입력해 주세요.")
        self.theme = theme
