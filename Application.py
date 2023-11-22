from FileManager import FileManager
from TodoManager import TodoManager
from Interface.MainInterface import MainInterface
from Interface.ListInterface import ListInterface
from Interface.DetailInterface import DetailInterface
from Interface.AddInterface import AddInterface
from Interface.EditInterface import EditInterface
from Interface.SearchInterface import SearchInterface
class Application:
    def __init__(self):
        self.file_manager = FileManager()
        self.todo_manager = TodoManager(self.file_manager.get_df_list())

    def run(self):  ##메인함수
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
            elif menu == 3:  # 검색
                self.search_menu()
            else:
                self.file_manager.save_csv(self.todo_manager.get_save_todos())  ##파일 정렬
                break

    def add_menu(self):
        add_interface = AddInterface(self.todo_manager)
        while True:
            menu = add_interface.CLI()
            if menu == 0:  # 종료
                return
    def search_menu(self):
        search_interface = SearchInterface(self.todo_manager)
        search_interface.CLI()
        funcs=search_interface.get_funcs()
        self.select_menu(funcs)
    def select_menu(self,funcs=None):
        list_interface = ListInterface(self.todo_manager,funcs)
        while True:
            menu = list_interface.CLI()
            if menu == 0:
                return
            data = list_interface.get_detail_data(menu)  ##인덱스 가져오기(리스트 기준이 아니라 파일 기준 인덱스)
            self.detail_menu(data)  ##상세보기

    def detail_menu(self, data):
        detail_interface = DetailInterface(self.todo_manager, data)
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
            elif menu == 3:
                edit_interface.edit_repeat()
                edit_interface.edit_repeat_detail()
            elif menu == 4:
                edit_interface.edit_finish()
            elif menu == 5:
                edit_interface.edit_theme()
            elif menu == 0:
                break
            else:
                print(edit_interface.err_message)
                continue
