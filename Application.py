from FileManager import FileManager
from Interface.MainInterface import MainInterface
from Interface.ListInterface import ListInterface
from Interface.DetailInterface import DetailInterface
from Interface.AddInterface import AddInterface
from Interface.EditInterface import EditInterface


class Application:
    def __init__(self):
        self.file_manager = FileManager()

    def run(self):  ##메인함수
        if not self.file_manager.is_valid_file():  ##파일이 유효하지 않으면
            return  ##종료
        self.main_menu()  ##메인메뉴 실행

    def main_menu(self):
        main_interface = MainInterface()
        while True:
            menu = main_interface.CLI()
            if menu == 1:  # 리스트
                self.select_menu()
            elif menu == 2:  # 추가
                self.add_menu()
                self.select_menu()  ##추가하고 리스트
            else:
                self.file_manager.sort_todolist()  ##파일 정렬
                ##종료
                break

    def add_menu(self):
        add_interface = AddInterface(self.file_manager)
        while True:
            menu = add_interface.CLI()
            if menu == 0:  # 종료
                return
            ##계속 추가

    def select_menu(self):
        list_interface = ListInterface(self.file_manager)
        while True:
            menu = list_interface.CLI()
            if menu == 0:
                return
            row = list_interface.get_row_by_user(menu)  ##인덱스 가져오기(리스트 기준이 아니라 파일 기준 인덱스)
            self.detail_menu(row)  ##상세보기

    def detail_menu(self, row):
        detail_interface = DetailInterface(row, self.file_manager)
        menu = detail_interface.CLI()
        if menu == 2:  ##삭제
            detail_interface.delete_todo()  ##삭제하고 리스트
        elif menu == 3:  ##완료
            detail_interface.complete_todo()
        elif menu==1:  ##수정 ##menu==1
            self.edit_menu(detail_interface)

    def edit_menu(self, detail_interface):
        while True:
            edit_interface = EditInterface(detail_interface)
            menu = edit_interface.CLI()
            if menu == 1:
                edit_interface.edit_title()
            elif menu == 2:
                edit_interface.edit_date()
                edit_interface.edit_start_date()
                edit_interface.edit_stop_repeat()
                break
            elif menu == 3:
                edit_interface.edit_repeat()
                edit_interface.edit_repeat_detail()
                break
            elif menu == 4:
                edit_interface.edit_finish()
                break
            elif menu == 0:
                break
            else:
                print(edit_interface.err_message)
                continue
