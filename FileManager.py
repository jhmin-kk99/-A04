import pandas as pd
from utility import *


class FileManager:

    def __init__(self):
        self.file_path = "./resource/TodoList_Datas.csv"
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.df = pd.DataFrame({
                "작업 이름": [], "마감 날짜": [], "반복": [], "시작 날짜": [], "완료": [], "반복 세부": [],"반복 마감": []
            })
            self.df.to_csv(self.file_path, index=False)
        self.TODAY = self.input_today()  ##datetime.date
        self.filtered_df = pd.DataFrame()

    def input_today(self):
        while True:
            todaystr = input("오늘 날짜를 입력하세요(YYYY-MM-DD): ")
            ret = is_valid_date_str(todaystr)
            if ret == "True":
                return todaystr
            else:
                print(ret)

    def sort_todolist(self):
        self.df = self.df.sort_values(by='마감 날짜')
        self.df.to_csv(self.file_path, index=False)

    def get_data_by_index(self, index):
        list = self.df.loc[index].to_list()
        ##  0         1       2      3      4      5      6
        ## 작업 이름,마감 날짜,시작 날짜,반복,반복 세부,반복 정지,완료
        ## 변환 요소: 1,2
        if list[3] == "매년":
            list[1] = change_date_to_this_week_year(list[4], self.TODAY)
        elif list[3] == "매달":
            list[1] = change_date_to_this_week_month(list[4], self.TODAY)
        elif list[3] == "매주":
            list[1] = change_date_to_this_week_weekday(list[4], self.TODAY)
        list[2]=get_start_date(list[1],list[2])
        return list
    def is_null_data(self):
        return self.filtered_df.empty
    def filter_todolist(self):
        ##마감일이 7일 이내인 것만 필터링
        if self.df['마감 날짜'].isnull().all():
            return pd.DataFrame()
        filter_deadline_df=self.df[self.df['마감 날짜'].apply(is_under_7days,args=(self.TODAY,))].copy()
        ##반복 속성에 따라서 수정된 날짜가 7일 이내인 것만 필터링
        years_df=filter_deadline_df[(filter_deadline_df['반복'] == "매년")].copy()
        if not years_df['반복 세부'].isnull().all():
            ##수정 날짜 구하기
            years_df['수정 날짜']=years_df['반복 세부'].apply(change_date_to_this_week_year,args=(self.TODAY,))
            ##수정 날짜가 7일 이내인 것만 필터링
            years_df['수정 날짜']=years_df['수정 날짜'].str.split("/")
            years_df=years_df.explode('수정 날짜')
            years_df=years_df[years_df['수정 날짜'].apply(is_in_7days,args=(self.TODAY,))].copy()
        month_df=filter_deadline_df[(filter_deadline_df['반복'] == "매달")].copy()
        if not month_df['반복 세부'].isnull().all():
            month_df['수정 날짜']=month_df['반복 세부'].apply(change_date_to_this_week_month,args=(self.TODAY,))
            month_df['수정 날짜']=month_df['수정 날짜'].str.split("/")
            month_df=month_df.explode('수정 날짜')
            month_df=month_df[month_df['수정 날짜'].apply(is_in_7days,args=(self.TODAY,))].copy()
        week_df=filter_deadline_df[(filter_deadline_df['반복'] == "매주")].copy()
        if not week_df['반복 세부'].isnull().all():
            week_df['수정 날짜']=week_df['반복 세부'].apply(change_date_to_this_week_weekday,args=(self.TODAY,))
            week_df['수정 날짜']=week_df['수정 날짜'].str.split("/")
            week_df=week_df.explode('수정 날짜')
            week_df=week_df[week_df['수정 날짜'].apply(is_in_7days,args=(self.TODAY,))].copy()
        none_df=filter_deadline_df[(filter_deadline_df['반복'] == "없음")].copy()
        if not none_df['마감 날짜'].isnull().all():
            none_df=none_df[none_df['마감 날짜'].apply(is_in_7days, args=(self.TODAY,))].copy()
            none_df['수정 날짜']=none_df['마감 날짜']
        ##필터링된 데이터프레임 합치기
        filter_df=pd.concat([years_df,month_df,week_df,none_df])
        if filter_df.empty:
            return filter_df
        ##반복 정지 날짜가 수정 날짜보다 느린 것만 필터링
        filter_df=filter_df[filter_df.apply(lambda row: compare_date_bool(row['반복 정지'], row['수정 날짜']), axis=1)].copy()
        ##필터링된 데이터프레임 정렬
        filter_df=filter_df.sort_values(by='수정 날짜')
        filter_df['Index']=filter_df.index
        self.filtered_df=filter_df.iloc[:9]
        return self.filtered_df

    def is_valid_file(self):
        for index, row in self.df.iterrows():
            row_data = {'index': index, 'data': row.to_dict()}
            if (is_valid_title(row_data['data']['작업 이름'])
                    and is_valid_date(row_data['data']['마감 날짜'])
                    and is_valid_start_date(row_data['data']['시작 날짜'])
                    and is_valid_repeat(row_data['data']['반복'])
                    and is_valid_finish(row_data['data']['완료'])
                    and is_valid_detail(row_data['data']['반복 세부'], row_data['data']['반복'])
            ):
                continue
            else:
                print(f'오류: 데이터 파일 TodoList_Datas.csv에 문법 규칙과 의미 규칙에 위배되는 행이 {index + 2}행에 존재합니다.')
                return False
        return True

    def delete_todo(self, index):
        self.df.drop(index, inplace=True)
        self.df.to_csv(self.file_path, index=False)

    def edit_todo(self, index, col_name, data):  ##col name:'작업 이름'
        self.df.loc[index, col_name] = data
        self.df.to_csv(self.file_path, index=False)

    def add_todo(self, data):  ## data: [배열임]
        new_row = pd.DataFrame(
            {'작업 이름': [data[0]], '마감 날짜': [data[1]], '시작 날짜': [data[2]], '반복': [data[3]], '반복 세부': [data[4]],
             '반복 정지': [data[5]], '완료': [data[6]]})
        self.df = pd.concat([self.df, new_row], ignore_index=True)  ##index 초기화
        self.df.to_csv(self.file_path, index=False)
