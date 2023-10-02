import re
from datetime import datetime, date,timedelta

def is_valid_title(input_string):
    pattern = r'^(?![␣])[␣a-zA-Z가-힣]{1,10}$'
    if re.match(pattern, input_string):
        return True
    else:
        # if len(input_string) < 1 or len(input_string) > 10:
        #     print("길이가 1 이상 10 이하가 아닙니다.")
        # if not input_string[0].isalpha() and not input_string[0].isspace():
        #     print("첫 문자가 알파벳 또는 띄어쓰기(␣)가 아닙니다.")
        # if not re.match(r'[a-zA-Z가-힣\s]*$', input_string):
        #     print("알파벳, 한글, 띄어쓰기(␣) 이외의 문자가 포함되어 있습니다.")
        return False

def is_valid_date(input_date):
    try:
        # 문자열을 날짜로 파싱합니다.
        datetime.strptime(input_date, '%Y-%m-%d')
        return True
    except ValueError:
        # 유효하지 않은 날짜 형식인 경우 예외가 발생합니다.
        return False

def is_valid_deadline(input_string):
    valid=["없음", "매주", "매달", "매년"]
    if(input_string in valid):
        return True
    else:
        return False

def is_last_day_of_month(date):
    next_month = date.replace(day=28) + timedelta(days=4)
    last_day = next_month - timedelta(days=next_month.day)
    return date.day == last_day.day

def filter_by_year(input_date):
    today=date.today()
    input=datetime.strptime(input_date, "%Y-%m-%d").date()
    if (today.year < input.year):
        return False
    return today.month==input.month and today.day==input.day


def filter_by_month(input_date):
    today=date.today()
    input=datetime.strptime(input_date, "%Y-%m-%d").date()
    if(today.year < input.year):
        return  False
    if(today.month < input.month):
        return False
    if(today.day==input.day):
        return True
    if(today.day<input.day and is_last_day_of_month(today)):
        return True
    return False

def filter_by_week(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    return today.weekday()==input.weekday()

def filter_by_day(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    return today==input