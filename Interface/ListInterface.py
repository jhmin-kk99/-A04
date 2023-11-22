from .interface import interface
from utility import is_completed


class ListInterface(interface):
    def __init__(self, todo_manager, funcs=None):
        self.err_message = "오류: 잘못 된 입력 입니다. 이동하려는 할일의 번호를 정확히 숫자로 입력해 주세요"
        self.todo_manager = todo_manager
        self.funcs = funcs

    def CLI(self):
        self.todo_manager.set_X_DAYS(self.get_X_day())
        self.todolist = self.todo_manager.get_list()
        self.filter_todolist_by_theme()
        self.todolist = self.todolist[:10]
        self.range = min(10, len(self.todolist))
        self.text = "<TODO List>\n"
        if len(self.todolist) == 0:
            input("할일이 없습니다. 아무키나 입력하면 돌아갑니다.")
            return 0
        header = f"{'작업 이름':<10} {'마감일':<15} {'반복':<10} {'반복 세부':<20} {'반복 정지':<15} {'완료':<10} {'분류':<10}"
        self.text += header + "\n"
        for i, data in enumerate(self.todolist):
            line = f"{str(i + 1) + '. ' + data['title']:<10} {data['calculated_date']:<15}" \
                   f" {data['repeat']:<10} {data['repeat_detail']:<20} {data['stop_repeat']:<15} " \
                   f"{data['calculated_completed']:<10} {data['theme']:<10}"
            self.text += line + "\n"

        self.text += "\n0. 돌아가기"
        self.text += "\nTODO/할일>"
        return super().CLI()
    def filter_todolist_by_theme(self):
        if self.funcs is not None:
            for func in self.funcs:
                for data in self.todolist:
                    if data['is_include']: ## 이미 필터링 된 데이터는(or 조건) 다시 필터링 하지 않음
                        continue
                    data['is_include'] = func(data['theme'])
            self.todolist = list(filter(lambda x: x['is_include'], self.todolist))

    def get_detail_data(self, num):
        return self.todolist[num - 1]

    def get_X_day(self):
        input_message = "향후 몇 날? [7]>"
        err_message = "오류: 잘못 된 입력 입니다. 0 이상 30 이하의 자연수를 입력해 주세요"
        while True:
            try:
                input_str = input(input_message)
                if (input_str == ""):
                    return 7
                day_list = [str(i) for i in range(0, 31)]
                if not input_str in day_list:
                    print(err_message)
                    continue
                return int(input_str)
            except ValueError:
                print(err_message)
                continue
