from utility import change_date_to_this_week_year, change_date_to_this_week_month, change_date_to_this_week_weekday, \
    compare_date_bool, is_in_x_days, compare_date_bool_include_equal
class Todo:
    def __init__(self,list,index):
        self.index=index
        self.set_data(list)
        self.calculated_dates = []

    def set_data(self, list):
        ##작업 이름,마감 날짜,시작 날짜,반복,반복 세부,반복 정지,완료,분류
        self.title=list[0]
        self.finish_date=list[1]
        self.start_date=list[2]
        self.repeat=list[3]
        self.repeat_detail=list[4]
        self.stop_repeat=list[5]
        self.completed=list[6]
        self.theme=list[7]

    def edit_data(self,key,value,TODAY,X_DAYS):
        if(key=="title"):
            self.title=value
        elif(key=="finish_date"):
            self.finish_date=value
        elif(key=="start_date"):
            self.start_date=value
        elif(key=="repeat"):
            self.repeat=value
        elif(key=="repeat_detail"):
            self.repeat_detail=value
        elif(key=="stop_repeat"):
            self.stop_repeat=value
        elif(key=="completed"):
            self.completed=value
        elif(key=="theme"):
            self.theme=value
        self.calculated_dates=[]
        self.calculate_dates(TODAY,X_DAYS)

    def get_data(self):
        ##dict 형식으로 리턴
        return {"title":self.title,"finish_date":self.finish_date,"start_date":self.start_date,
                "repeat":self.repeat,"repeat_detail":self.repeat_detail,"stop_repeat":self.stop_repeat,
                "completed":self.completed,"theme":self.theme, "calculated_dates":self.calculated_dates}
    def calculate_dates(self,TODAY,X_DAYS):
        self.calculated_dates=[]
        if(self.repeat=="없음"):
            self.calculated_dates.append(self.finish_date)
        elif(self.repeat=="매주"):
            self.calculated_dates=change_date_to_this_week_weekday(self.repeat_detail,TODAY)
        elif(self.repeat=="매달"):
            self.calculated_dates=change_date_to_this_week_month(self.repeat_detail,TODAY)
        elif(self.repeat=="매년"):
            self.calculated_dates=change_date_to_this_week_year(self.repeat_detail,TODAY)
        ##반복 정지일이 있으면 그 날짜 이후 필터링
        if(self.stop_repeat!="x"):
            self.calculated_dates=[date for date in self.calculated_dates if compare_date_bool(self.stop_repeat,date)]
        ##마감 날짜보다 빠르면 필터링
        if(self.repeat!="없음"):
            self.calculated_dates=[date for date in self.calculated_dates if compare_date_bool(date,self.finish_date)]
        ##오늘 날짜보다 빠르면 필터링
        self.calculated_dates=[date for date in self.calculated_dates if compare_date_bool_include_equal(date,TODAY)]
        ##x일 이내로 필터링
        self.calculated_dates=[date for date in self.calculated_dates if is_in_x_days(date,TODAY,X_DAYS)]