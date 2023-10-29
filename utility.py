import re
from datetime import datetime, date, timedelta
from constants import TODAY


def is_valid_title(input_string):
    pattern = r'^(?![ ])[ a-zA-Z가-힣1-9]{1,10}$'
    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_valid_title_str(input_string):
    pattern = r'^(?![ ])[ a-zA-Z가-힣1-9]{1,10}$'
    if re.match(pattern, input_string):
        return "True"
    else:
        if len(input_string) < 1 or len(input_string) > 10:
            return "오류: 길이가 1 이상 10 이하가 아닙니다."
        if input_string[0] == ' ':
            return "오류: 작업 이름은 공백으로 시작할 수 없습니다."
        if not re.match(r'[ a-zA-Z가-힣1-9]*$', input_string):
            return "오류: 알파벳, 한글, 숫자, 띄어쓰기(␣) 이외의 문자가 포함되어 있습니다."
        return "False"


def is_valid_date(input_date):
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_start_date(input_date):
    if (input_date == "x"):
        return True
    try:
        int(input_date)
        return True
    except ValueError:
        return False


def is_valid_finish(input_date):
    if (input_date == "x"):
        return True
    date_list = input_date.strip().split("/")
    try:
        for i in date_list:
            datetime.strptime(i, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_detail(input_date, repeat):
    if (repeat == "없음"):
        if (input_date == "x"):
            return True
        else:
            return False
    if (repeat == "매주"):
        if (is_valid_day_detail_str(input_date) == "True"):
            return True
        else:
            return False
    if (repeat == "매달"):
        if (is_valid_month_detail_str(input_date) == "True"):
            return True
        else:
            return False
    if (repeat == "매년"):
        if (is_valid_year_detail_str(input_date) == "True"):
            return True
        else:
            return False
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


def is_valid_day_detail_str(input_text):
    input_list = input_text.strip().split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 요일이 있습니다."
    menu_list = ["월", "화", "수", "목", "금", "토", "일"]
    for i in input_list:
        if not i in menu_list:
            return "오류: 요일을 다시 입력해 주세요."
    return "True"


def is_valid_month_detail_str(input_text):
    input_list = input_text.strip().split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 월이 있습니다."
    menu_list = [str(i) for i in range(1, 32)]
    for i in input_list:
        if not i in menu_list:
            return "오류: 날짜를 다시 입력해 주세요."
    return "True"


def is_valid_year_detail_str(input_text):
    input_list = input_text.strip().split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 날짜가 있습니다."
    ##input_text 양식 12-31/10-13
    menu_list = [str(i) for i in range(1, 13)]  ##월
    for i in input_list:
        month = i.split("-")[0]
        day = i.split("-")[1]
        if (month not in menu_list):
            return "오류: 월을 다시 입력해 주세요."
        if (int(day) > 31):
            return "오류: 일을 다시 입력해 주세요."
        if (month == "2" and int(day) > 29):
            return "오류: 2월은 29일까지 있습니다."
    return "True"


def is_valid_repeat(input_string):
    valid = ["없음", "매주", "매달", "매년"]
    if (input_string in valid):
        return True
    else:
        return False


def get_valid_date(year, month, day):  ##str 리턴
    if (is_valid_date(str(year) + "-" + str(month) + "-" + str(day))):
        return str(year) + "-" + str(month) + "-" + str(day)
    else:
        if (month == 13):
            return get_valid_date(year + 1, 1, day)
        return get_valid_date(year, month, day - 1)


def is_in_7days(input_date, today):
    input_date = datetime.strptime(input_date, "%Y-%m-%d").date()
    today = datetime.strptime(today, "%Y-%m-%d").date()
    return (input_date - today).days <= 7 and (input_date - today).days >= 0


def is_under_7days(input_date, today_date):
    ##마감일은 오늘보다 빠르기만 하면 됨
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    today = datetime.strptime(today_date, "%Y-%m-%d").date()
    return (input - today).days <= 7


def compare_date_bool(dateA, date_B):
    if (dateA == "x"):
        return True
    dateA = datetime.strptime(dateA, "%Y-%m-%d").date()
    date_B = datetime.strptime(date_B, "%Y-%m-%d").date()
    return dateA > date_B  ##dateA가 더 늦으면 True


def diff_date(input_date, today_date):
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    today = datetime.strptime(today_date, "%Y-%m-%d").date()
    return (input - today).days


def get_start_date(input_date, day):
    if (day == "x"):
        return "x"
    input = datetime.strptime(input_date, "%Y-%m-%d").date()
    return (input - timedelta(days=int(day))).strftime("%Y-%m-%d")


def change_date_to_this_week_year(MM_YY, today_date):
    if ("/" not in MM_YY):  ##
        today = datetime.strptime(today_date, "%Y-%m-%d").date()
        month = int(MM_YY.split("-")[0])
        day = int(MM_YY.split("-")[1])
        return datetime.strptime(get_valid_date(today.year, month, day), "%Y-%m-%d").date().strftime("%Y-%m-%d")
    else:
        list = MM_YY.strip().split("/")
        result_list = [change_date_to_this_week_year(i, today_date) for i in list]
        return "/".join(result_list)


def change_date_to_this_week_month(DD, today):
    ## 날짜를 today와 크거나 같고 일주일 이하인 날짜로 리턴
    if ("/" not in DD):  ##
        today = datetime.strptime(today, "%Y-%m-%d").date()
        this_month_date = get_valid_date(int(today.year), today.month, int(DD))
        next_month_date = get_valid_date(int(today.year), today.month + 1, int(DD))
        if (is_in_7days(this_month_date, today.strftime("%Y-%m-%d"))):
            return this_month_date
        elif (is_in_7days(next_month_date, today.strftime("%Y-%m-%d"))):
            return next_month_date
        else:
            return "1111-11-11"
    else:
        list = DD.strip().split("/")
        result_list = [change_date_to_this_week_month(i, today) for i in list]
        return "/".join(result_list)


def change_date_to_this_week_weekday(weekday, today):
    ##weekday: 월
    if ("/" not in weekday):  ##
        week_list = ["월", "화", "수", "목", "금", "토", "일"]
        week_num = week_list.index(weekday)
        today = datetime.strptime(today, "%Y-%m-%d").date()
        while (today.weekday() != week_num):
            today = today + timedelta(days=1)
        return (today).strftime("%Y-%m-%d")
    else:
        list = weekday.strip().split("/")
        result_list = [change_date_to_this_week_weekday(i, today) for i in list]
        return "/".join(result_list)


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


def is_completed(complete_date, finish_date):
    if (complete_date == "x"):
        return "x"
    list = complete_date.strip().split("/")
    today = datetime.strptime(finish_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    if today in list:
        return "o"
    else:
        return "x"


def can_finish(start_date, today_date):
    if (start_date == "x"):
        return True
    else:
        return compare_date_bool(today_date, start_date) or today_date == start_date


def add_finish_date(finish_date, edit_date):
    if (finish_date == "x"):
        return edit_date
    else:
        list = finish_date.strip().split("/")
        if (edit_date not in list):
            list.append(edit_date)
        if(len(list)==1):
            return list[0]
        else:
            return "/".join(list)


def remove_finish_date(finish_date, edit_date):
    list = finish_date.strip().split("/")
    if (edit_date in list):
        list.remove(edit_date)
    if(len(list)==0):
        return "x"
    else:
        return "/".join(list)
