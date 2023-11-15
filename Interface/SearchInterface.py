from .interface import interface
from utility import is_valid_search, get_query_func
class SearchInterface(interface):
    def __init__(self, todo_manager):
        self.err_message = "오류: 잘못 된 입력 입니다. 이동하려는 할일의 번호를 정확히 숫자로 입력해 주세요"
        self.todo_manager = todo_manager
        self.query_list=[]
    def CLI(self):
        ## theme으로 검색하는 메뉴
        self.text = "<할일 검색하기>\n"
        self.text += "검색할 분류를 입력하세요.\n"
        self.text += "ex)운동 or 공부 and not 코딩\n"
        self.text += "TODO/검색 - 분류\n"
        self.input_theme()

    def get_funcs(self):
        funcs=[]
        for and_query in self.query_list:
            funcs.append(get_query_func(and_query))
        return funcs


    def input_theme(self):
        text = input(self.text)
        while (not is_valid_search(text)):
            text = input(self.text)
        self.query_list= [item.strip() for item in text.split('or')]
