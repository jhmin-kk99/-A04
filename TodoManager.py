from utility import get_start_date, is_completed,input_today
from Todo import Todo
class TodoManager:
    def __init__(self, list_data):
        self.todos = {}
        self.TODAY = input_today()
        self.index=0
        self.X_DAYS=7
        self.load_todos(list_data)

    def load_todos(self,list_data):
        for row in list_data:
            new_todo=Todo(row,self.index)
            new_todo.calculate_dates(self.TODAY,self.X_DAYS)
            self.todos[self.index]=new_todo
            self.index+=1

    def get_save_todos(self):
        ##작업 이름,마감 날짜,시작 날짜,반복,반복 세부,반복 정지,완료,분류
        ##리스트 형식으로 리턴
        todolist=[]
        for todo in self.todos.values():
            todolist.append(todo.get_data())
        return todolist
    def add_todo(self, list):
        new_todo=Todo(list,self.index)
        new_todo.calculate_dates(self.TODAY,self.X_DAYS)
        self.todos[self.index]=new_todo
        self.index+=1

    def edit_todo(self, index, key, value, doCalc = True):
        self.todos[index].edit_data(key, value, self.TODAY, self.X_DAYS, doCalc)

    def delete_todo(self,index):
        del self.todos[index]
    def update_todos(self):
        ## X_DAYS 변경에 따라 다시 계산
        for key in self.todos.keys():
            self.todos[key].calculate_dates(self.TODAY,self.X_DAYS)

    def get_list(self):
        ##calculate_dates를 통해 계산된 날짜를 기준으로 정렬
        todolist=[]
        for key,todo in self.todos.items():
            data=todo.get_data()
            for date in data['calculated_dates']:
                fixed_start_date=get_start_date(date,data['start_date'])
                fixed_completed=is_completed(data['completed'],date)
                todolist.append({"title":data['title'],"finish_date":data['finish_date'],"start_date":fixed_start_date,
                                "repeat":data['repeat'],"repeat_detail":data['repeat_detail'],"stop_repeat":data['stop_repeat'],
                                 "calculated_date":date, "completed":data['completed'],
                                "calculated_completed":fixed_completed,"theme":data['theme'],'index':key,'is_include':False})
        todolist=sorted(todolist,key=lambda x:x['calculated_date'])
        return todolist

    def set_X_DAYS(self,X_DAYS):
        if(X_DAYS==self.X_DAYS):
            return
        self.X_DAYS=X_DAYS
        self.update_todos()

