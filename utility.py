import re
from datetime import datetime, date, timedelta


def is_valid_title(input_string):
    pattern = r'^(?![␣])[␣a-zA-Z가-힣1-9]{1,10}$'
    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_valid_title_str(input_string):
    pattern = r'^(?![␣])[␣a-zA-Z가-힣1-9]{1,10}$'
    if re.match(pattern, input_string):
        return "True"
    else:
        if len(input_string) < 1 or len(input_string) > 10:
            return "오류: 길이가 1 이상 10 이하가 아닙니다."
        if not input_string[0].isalpha() and not input_string[0].isspace():
            return "오류: 첫 문자가 알파벳 또는 띄어쓰기(␣)가 아닙니다."
        if not re.match(r'[a-zA-Z가-힣\s]*$', input_string):
            return "오류: 알파벳, 한글, 띄어쓰기(␣) 이외의 문자가 포함되어 있습니다."
        return "False"


def is_valid_date(input_date):
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_date_str(input_date):
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
    except ValueError:
        return "오류: 날짜를 입력해 주세요."

    year, month, day = map(int, input_date.split('-'))

    if year < 1000 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return "오류: 날짜는 YYYY-MM-DD 형태로 입력해야 합니다."

    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 29):
        return "오류: 정의되지 않은 날짜 입니다."
    return "True"


def is_valid_repeat(input_string):
    valid = ["없음", "매주", "매달", "매년"]
    if (input_string in valid):
        return True
    else:
        return False


def get_valid_date(year, month, day):
    if (is_valid_date(str(year) + "-" + str(month) + "-" + str(day))):
        return datetime(year, month, day).date()
    else:
        if (month == 13):
            return get_valid_date(year + 1, 1, day)
        return get_valid_date(year, month, day - 1)


def change_date_to_this_week_year(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    return get_valid_date(today.year, input.month, input.day).strftime("%Y-%m-%d")


def change_date_to_this_week_month(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    this_month_date = get_valid_date(today.year, today.month, input.day)
    next_month_date = get_valid_date(today.year, today.month + 1, input.day)
    if (is_in_7days(this_month_date)):
        return this_month_date.strftime("%Y-%m-%d")
    elif (is_in_7days(next_month_date)):
        return next_month_date.strftime("%Y-%m-%d")
    else:
        return "1111-11-11"


def change_date_to_this_week_weekday(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    while (today.weekday() != input.weekday()):
        today = today + timedelta(days=1)
    return (today).strftime("%Y-%m-%d")



def change_date_to_this_week(input_date, repeat):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    if (repeat == "없음"):
        return input_date
    elif (repeat == "매주"):
        while (today.weekday() != input.weekday()):
            today = today + timedelta(days=1)
        else:
            return (today).strftime("%Y-%m-%d")
    elif (repeat == "매달"):
        this_month_date = get_valid_date(today.year, today.month, input.day)
        next_month_date = get_valid_date(today.year, today.month + 1, input.day)
        if (is_in_7days(this_month_date)):
            return this_month_date.strftime("%Y-%m-%d")
        elif (is_in_7days(next_month_date)):
            return next_month_date.strftime("%Y-%m-%d")
        else:
            return "1111-11-11"
    elif (repeat == "매년"):
        return get_valid_date(today.year, input.month, input.day).strftime("%Y-%m-%d")
    else:
        return "1111-11-12"  ##오류


def is_in_7days(input_date):
    today = date.today()
    return (input_date - today).days <= 7 and (input_date - today).days >= 0


def is_later_todo(input_date):
    today = date.today()
    return (input_date - today).days > 7


def filter_by_year(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    if (is_later_todo(input)):
        return False
    return is_in_7days(get_valid_date(today.year, input.month, input.day))  ##말일처리 다시


def filter_by_month(input_date):
    today = date.today()
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    if (is_later_todo(input)):  ##마감일이 오늘보다 늦으면
        return False
    this_month_date = get_valid_date(today.year, today.month, input.day)
    next_month_date = get_valid_date(today.year, today.month + 1, input.day)
    return is_in_7days(this_month_date) or is_in_7days(next_month_date)


def filter_by_week(input_date):
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    if (is_later_todo(input)):
        return False
    return True


def filter_by_none(input_date):
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    return is_in_7days(input)


def input_menu(start, end, input_message):
    err_message = "오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
    while True:
        try:
            menu = int(input(input_message))
            if (menu < start or menu >= end):
                print(err_message)
                continue
            else:
                return menu
        except ValueError:
            print(err_message)
