from FileManager import FileManager
from Interface.MainInterface import MainInterface
from Interface.ListInterface import ListInterface
from Interface.DetailInterface import DetailInterface
from Interface.AddInterface import AddInterface
from Interface.EditInterface import EditInterface

class Application:
    def __init__(self):
        self.file_manager = FileManager()

    def run(self):##메인함수
        if not self.file_manager.is_valid_file():##파일이 유효하지 않으면
            return##종료
        self.file_manager.sort_todolist()##파일 정렬
        self.main_menu()##메인메뉴 실행

    def main_menu(self):
        main_interface = MainInterface()
        while True:
            menu = main_interface.CLI()
            if menu == 1:#리스트
                self.select_menu()
            elif menu == 2:#추가
                self.add_menu()
                self.select_menu()##추가하고 리스트
            else:
                break

    def add_menu(self):
        add_interface = AddInterface(self.file_manager)
        while True:
            menu = add_interface.CLI()
            if menu == 0:#종료
                return
            ##계속 추가

    def select_menu(self):
        list_interface = ListInterface(self.file_manager)
        while True:
            menu = list_interface.CLI()
            if menu == 0:
                return
            index = list_interface.get_index_by_user(menu)##인덱스 가져오기(리스트 기준이 아니라 파일 기준 인덱스)
            self.detail_menu(index)##상세보기

    def detail_menu(self, index):
        detail_interface = DetailInterface(index, self.file_manager)
        while True:
            menu = detail_interface.CLI()
            if menu == 0:
                return##종료
            elif menu == 2:##삭제
                detail_interface.delete_todo()##삭제하고 리스트
                return
            else:##수정
                self.edit_menu(detail_interface)

    def edit_menu(self, detail_interface):
        edit_interface = EditInterface(detail_interface)
        while True:
            menu = edit_interface.CLI()
            if menu == 1:
                edit_interface.edit_title()
            elif menu == 2:
                edit_interface.edit_date()
            elif menu == 3:
                edit_interface.edit_repeat()
            else:
                break
