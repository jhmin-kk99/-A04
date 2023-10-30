from .interface import interface
from utility import is_valid_date_str, is_valid_title_str, is_valid_day_detail_str, is_valid_year_detail_str, \
    is_valid_month_detail_str, get_start_date, is_completed, diff_date, input_menu


class EditInterface(interface):
    def __init__(self, detail):
        self.detail = detail
        self.index = detail.index
        self.file_manager = detail.file_manager
        self.err_message = "오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        self.range = 4

    def CLI(self):
        self.text = "<할일 수정하기>"
        self.row_data = self.detail.row_data
        self.todoText = "\n작업 이름: " + self.detail.title + "\n마감 날짜: " + self.detail.finish_date + "\n시작 날짜: " + \
                        self.detail.start_date + "\n반복: " + self.detail.repeat + \
                        "\n반복 세부: " + self.detail.repeat_detail + "\n반복 정지: " + self.detail.stop_repeat + "\n완료: " + \
                        self.detail.completed
        self.text += self.todoText
        self.text += "\n1.작업 수정하기" \
                     "\n2.날짜 수정하기" \
                     "\n3.반복 수정하기" \
                     "\n4.완료 수정하기" \
                     "\n0.돌아가기\n"
        self.text += "\nTODO/할일 수정>"
        return super().CLI()

    def update_todo_text(self):
        self.todoText = "\n작업 이름: " + self.detail.title + "\n마감 날짜: " + self.detail.finish_date + "\n시작 날짜: " + \
                        self.detail.start_date + "\n반복: " + self.detail.repeat + \
                        "\n반복 세부: " + self.detail.repeat_detail + "\n반복 정지: " + self.detail.stop_repeat + "\n완료: " + \
                        self.detail.completed
    def edit_title(self):
        text = "<할일 수정하기>"
        text += self.todoText + "\n변경될 작업 이름을 입력하세요."
        text += "\nTODO/할일 수정 - 작업>"
        while True:
            title = input(text)
            is_valid = is_valid_title_str(title)
            if (is_valid == "True"):
                break
            else:
                print(is_valid)
        self.file_manager.edit_todo(self.index, '작업 이름', title)
        self.detail.title=title
        self.update_todo_text()

    def edit_date(self):
        text = "<할일 수정하기>"
        text += self.todoText + "\n변경될 마감 날짜를 입력하세요."
        text += "\nTODO/할일 수정 - 마감 날짜>"
        while True:
            date = input(text)
            is_valid = is_valid_date_str(date)
            if (is_valid == "True"):
                break
            else:
                print(is_valid)
        self.file_manager.edit_todo(self.index, '마감 날짜', date)
        self.detail.finish_date=date
        self.update_todo_text()

    def edit_start_date(self):
        text = "<할일 수정하기>"
        text += self.todoText + "\n변경될 시작일을 입력하세요."
        text += "\nTODO/할일수정 - 시작일(시작일이 없다면 'x'를 입력하세요.)\n"
        while (True):
            date = input(text)
            if (date == "x"):##시작일이 없다면
                self.file_manager.edit_todo(self.index, '시작 날짜', date)
                self.detail.start_date=date
                break
            if (is_valid_date_str(date) == "True"):##시작일이 있다면
                diff = diff_date(self.detail.finish_date, date)
                if (diff < 0):
                    print("오류: 시작일이 마감일보다 늦습니다.")
                    continue
                else:
                    self.file_manager.edit_todo(self.index, '시작 날짜', diff)
                    self.detail.start_date=date
                    break
            else:
                print(is_valid_date_str(date))
        self.update_todo_text()

##만약 마감일이 10/25일이었는데, 월/화/수 반복하는 할일이 있다고 하자. 그런데 반복을 매달 1/2/3일 반복하는 할일로 바꾸면
##마감일은 현재 날짜 기준으로 보여야 하기 대문에 마감일을 11/1일로 바꿔야 한다. 게다가 11/1, 11/2, 11/3 중 무엇으로 바꿀지 결정하기도 애매하다.
##그래서 그냥 Listinterface로 돌아가는게 좋을 듯 하다.
    def edit_repeat(self):
        text = "<할일 수정하기>"
        text += self.todoText + "\n반복 여부을 입력하세요."
        text += "반복 여부를 선택하세요.\n 1. 없음\n 2. 매주\n 3. 매달\n 4. 매년\n"
        text += "TODO/할일 수정 - 반복>"
        menu = input_menu(1, 4, text)
        menu_list = ["-", "없음", "매주", "매달", "매년"]
        menu = menu_list[menu]
        self.file_manager.edit_todo(self.index, '반복', menu)
        self.detail.repeat = menu
        self.update_todo_text()

    def edit_repeat_detail(self):
        if (self.detail.repeat == "매주"):
            while True:
                message = input("반복 요일을 선택하세요. ex) 월/화/수\n")
                ret = is_valid_day_detail_str(message)
                if (ret == "True"):
                    break
                else:
                    print(ret)
        elif (self.detail.repeat == "매달"):
            while True:
                message = input("반복 날짜를 선택하세요. ex) 1/2/3.../31\n")
                ret = is_valid_month_detail_str(message)
                if (ret == "True"):
                    break
                else:
                    print(ret)
        elif (self.detail.repeat == "매년"):
            while True:
                message = input("반복 날짜를 선택하세요. ex)12-31/10-13\n")
                ret = is_valid_year_detail_str(message)
                if (ret == "True"):
                    break
                else:
                    print(ret)
        else:
            message = "x"
        self.file_manager.edit_todo(self.index, '반복 세부', message).strip()
        self.detail.repeat_detail = message
        self.update_todo_text()
        ##반복이 바뀌면 마감일이 바뀌어야 한다.


    def edit_stop_repeat(self):
        text = "<할일 수정하기>\n"
        text += "TODO/할일수정 - 반복 정지일 (무한 반복이면 'x' 입력)\n"
        while (True):
            date = input(text)
            if (date == "x" or is_valid_date_str(date) == "True"):
                break
            else:
                print(is_valid_date_str(date))
        self.file_manager.edit_todo(self.index, '반복 정지', date)
        self.detail.stop_repeat=date
        self.update_todo_text()

    def edit_finish(self):
        text = "<할일 수정하기>\n"
        text += "TODO/할일수정 - 완료일 (미완료이면 'x' 입력, 완료면 'o' 입력)\n"
        while (True):
            OX = input(text)
            if OX=="x":
                if self.detail.completed=="o":
                    self.detail.reset_completed_todo()
                    self.detail.completed="x"
                else:
                    print("오류: 이미 미완료된 할일입니다.")
                break
            elif OX=="o":
                self.detail.complete_todo()
                self.detail.completed="o"
                break
            else:
                print("오류: 잘못된 입력입니다.")
                continue
        self.update_todo_text()
