from .interface import interface
from utility import can_finish,add_finish_date,remove_finish_date, get_most_fast_calculate_date
class DetailInterface(interface):
    def __init__(self, todo_manager,data):
        self.todo_manager=todo_manager
        self.data=data
        self.err_message = "오류: 잘못 된 입력 입니다. 다시 입력해 주세요"
        self.range = 3
        self.index=data['index']
    def CLI(self):
        self.todoText="\n작업 이름: "+self.data["title"]+ "\n마감 날짜: "+self.data['finish_date']+\
                      "\n마감일: "+self.data["calculated_date"] +"\n시작 날짜: "+self.data["start_date"]+\
                      "\n반복: "+self.data["repeat"]+ "\n반복 세부: "+self.data["repeat_detail"]+\
                        "\n반복 정지: "+self.data['stop_repeat']+"\n완료: "+self.data['calculated_completed']+\
                      "\n분류: "+self.data['theme']
        self.text = "\n<할일>"
        self.text+=self.todoText+"\n"
        self.text+="\n1. 수정하기" \
                   "\n2. 삭제하기" \
                   "\n3. 완료하기\n" \
                   "\n0. 돌아가기\n"
        self.text += "\nTODO/할일 세부>"
        return super().CLI()

    def update_todo_text(self):
        self.todoText="\n작업 이름: "+self.data["title"]+ "\n마감 날짜: "+self.data['finish_date']+\
                      "\n마감일: "+self.data["calculated_date"] +"\n시작 날짜: "+self.data["start_date"]+\
                      "\n반복: "+self.data["repeat"]+ "\n반복 세부: "+self.data["repeat_detail"]+\
                        "\n반복 정지: "+self.data['stop_repeat']+"\n완료: "+self.data['calculated_completed']+\
                      "\n분류: "+self.data['theme']

    def delete_todo(self):
        if(self.data["repeat"]=="없음"):
            self.todo_manager.delete_todo(self.index)
        else:
            ## 반복 정지를 '마감일-1'로 변경
            self.todo_manager.edit_todo(self.index, "stop_repeat", self.data['calculated_date'])
            ## 마감일이 마감 날짜 이후 첫 마감일이면 바로 삭제
            if(self.data['calculated_date']==get_most_fast_calculate_date(self.data['repeat'],self.data['repeat_detail'],self.data['finish_date'])):
                self.todo_manager.delete_todo(self.index)



    def complete_todo(self):
        if(self.data["calculated_completed"]=="o"):
            print("오류: 이미 완료된 할일입니다.")
        elif(can_finish(self.data['start_date'],self.todo_manager.TODAY)):##완료 가능함
            complete_days=add_finish_date(self.data['completed'],self.data['calculated_date'])
            self.todo_manager.edit_todo(self.data['index'], "completed", complete_days)
            self.data['calculated_completed']="o"
        else:
            print("오류: 시작일이 지나지 않았습니다.")

    def reset_completed_todo(self):
        complete_days=remove_finish_date(self.data['completed'],self.data['calculated_date'])
        self.todo_manager.edit_todo(self.data['index'], "completed", complete_days)
        self.data['calculated_completed']="x"