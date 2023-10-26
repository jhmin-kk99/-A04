from .interface import interface
from utility import get_start_date,is_completed,can_finish,add_finish_date,remove_finish_date
class DetailInterface(interface):
    def __init__(self, row_data, file_manager):
        self.file_manager=file_manager##row_data는 series 객체
        self.index=row_data['Index']
        self.row_data=row_data
        self.err_message="오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        self.range=3
        self.title=row_data['작업 이름']
        self.finish_date=row_data['수정 날짜']
        self.start_date=get_start_date(row_data['수정 날짜'],row_data['시작 날짜'])
        self.repeat=row_data['반복']
        self.repeat_detail=row_data['반복 세부']
        self.stop_repeat=row_data['반복 정지']
        self.completed=is_completed(row_data['완료'],self.finish_date)

    def CLI(self):
        self.todoText="\n작업 이름: "+self.title+"\n마감 날짜: "+self.finish_date+"\n시작 날짜: "+self.start_date+"\n반복: "+self.repeat+\
                        "\n반복 세부: "+self.repeat_detail+"\n반복 정지: "+self.stop_repeat+"\n완료: "+self.completed
        self.text = "\n<할일>"
        self.text+=self.todoText+"\n"
        self.text+="\n1. 수정하기" \
                   "\n2. 삭제하기" \
                   "\n3. 완료하기\n" \
                   "\n0. 돌아가기\n"
        self.text += "\nTODO/할일 세부>"
        return super().CLI()



    def delete_todo(self):
        self.file_manager.delete_todo(self.index)

    def complete_todo(self):
        if(self.completed=="o"):
            print("오류: 이미 완료된 할일입니다.")
        elif(can_finish(self.start_date,self.file_manager.TODAY)):##완료 가능함
            complete_days=add_finish_date(self.row_data['완료'],self.finish_date)
            self.file_manager.edit_todo(self.index, "완료", complete_days)
            self.completed="o"
        else:
            print("오류: 시작일이 지나지 않았습니다.")

    def reset_completed_todo(self):
        complete_days=remove_finish_date(self.row_data['완료'],self.finish_date)
        self.file_manager.edit_todo(self.index, "완료", complete_days)
        self.completed="x"