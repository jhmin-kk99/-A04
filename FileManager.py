import sys
import pandas as pd
from utility import *


class FileManager:

    def __init__(self):
        self.file_path = "./resource/TodoList_Datas.csv"
        try:
            self.df = pd.read_csv(self.file_path)
            self.df = self.df.fillna("")
            if not self.is_valid_file() :
                sys.exit(0)
        except PermissionError:
            print("오류: 데이터 파일 TodoList_Datas.csv에 대한 입출력 권한이 없습니다. 프로그램을 종료합니다.")
            sys.exit(0)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            self.df = pd.DataFrame({
                "작업 이름": [], "마감 날짜": [], "시작 날짜": [], "반복": [], "반복 세부": [],"반복 정지": [], "완료": [], "분류": []
            })
            self.df.to_csv(self.file_path, index=False)


    def get_df_list(self):
        return self.df.values.tolist()


    def is_valid_file(self):
        valid = True
        notValidIndices = []

        order_colnames = ["작업 이름","마감 날짜","시작 날짜","반복","반복 세부","반복 정지","완료","분류"]
        file_colnames = list(self.df.columns)
        if (len(file_colnames) != len(order_colnames)):
            print("오류 : 데이터 파일의 헤더행이 잘못되어 파일을 정상적으로 읽을 수 없었습니다.")
            return False
        for i in range(len(file_colnames)):
            if not file_colnames[i] == order_colnames[i] :
                print("오류 : 데이터 파일의 헤더행이 잘못되어 파일을 정상적으로 읽을 수 없었습니다.")
                return False
            
        for index, row in self.df.iterrows():
            row_data = {'index': index, 'data': row.to_dict()}
            if (is_valid_title(row_data['data']['작업 이름'])
                    and is_valid_date(row_data['data']['마감 날짜'])
                    and is_valid_start_date(row_data['data']['시작 날짜'])
                    and is_valid_repeat(row_data['data']['반복'])
                    and is_valid_finish(row_data['data']['완료'])
                    and is_valid_detail(row_data['data']['반복 세부'], row_data['data']['반복'])
                    and is_valid_repeat_end_date(row_data['data']['반복 정지'])
                    and is_valid_theme(row_data['data']['분류'])
            ):
                continue
            else:
                valid = False
                notValidIndices.append(index+2)
        
        if valid == False :
            f = open(self.file_path, 'r', encoding='utf8')
            csvLines = f.readlines()
            f.close()
            
            errStr = ",".join([(str(i)+"행") for i in notValidIndices])

            print(f'오류: 데이터 파일 TodoList_Datas.csv에 문법 규칙과 의미 규칙에 위배되는 행이 {errStr}에 존재합니다.')
            print()
            for i in notValidIndices :
                print("\t"+csvLines[i-1], end="")
            print()

        return valid


    def save_csv(self,savelist):
        self.save_df = pd.DataFrame({
            "작업 이름": [], "마감 날짜": [], "시작 날짜": [], "반복": [], "반복 세부": [], "반복 정지": [], "완료": [], "분류": []
        })
        for data in savelist:
            save_data = {
                "작업 이름": data['title'], "마감 날짜": data['finish_date'], "시작 날짜": str(data['start_date']), "반복": data['repeat'],
                "반복 세부": data['repeat_detail'], "반복 정지": data['stop_repeat'], "완료": data['completed'], "분류": data['theme']
            }
            save_df = pd.DataFrame([save_data])
            self.save_df = pd.concat([self.save_df, save_df], ignore_index=True)
        self.save_df = self.save_df.sort_values(by='마감 날짜')
        self.save_df.to_csv(self.file_path, index=False)
        print("저장되었습니다.")