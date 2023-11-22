import re
from datetime import datetime, date, timedelta


def is_valid_title(input_string):
    pattern = r'^(?![ ])[ a-zA-Z가-힣0-9]{1,10}$'
    if isinstance(input_string, int):
        input_string = str(input_string)
    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_valid_title_str(input_string):
    pattern = r'^(?![ ])[ a-zA-Z가-힣0-9]{1,10}$'
    if re.match(pattern, input_string):
        return "True"
    else:
        if len(input_string) < 1 or len(input_string) > 10:
            return "오류: 길이가 1 이상 10 이하가 아닙니다."
        if input_string[0] == ' ':
            return "오류: 작업 이름은 공백으로 시작할 수 없습니다."
        if not re.match(r'[ a-zA-Z가-힣0-9]*$', input_string):
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


def is_valid_repeat_end_date(input_date):
    if (input_date == "x"):
        return True
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
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


def is_valid_theme(input_text):
    ## 입력양식: 축구+농구+야구
    if(input_text=="x"):
        return True
    if (not re.match(r"([가-힣]|\+)+$", input_text)):
        return False
    input_list = input_text.split("+")
    if len(input_list) != len(set(input_list)):
        return False
    ##개별 분류의 길이는 5 이하
    return True


def is_valid_theme_a_word(input_text):
    return re.match('^[가-힣]{1,5}$', input_text)


def is_valid_date_str(input_date):
    if (not re.match(r"\d{4}-\d{2}-\d{2}$", input_date)):
        return "오류: 날짜는 YYYY-MM-DD 형태로 입력해야 합니다."
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return "True"
    except ValueError:
        return "오류: 정의되지 않은 날짜 입니다."


def is_valid_day_detail_str(input_text):
    if (not re.match(r"([월화수목금토일]\/)*[월화수목금토일]$", input_text)):
        return "오류: 요일을 다시 입력해 주세요."
    input_list = input_text.split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 요일이 있습니다."
    return "True"


def is_valid_month_detail_str(input_text):
    if (not re.match(r"(\d{1,2}\/)*\d{1,2}$", input_text)):
        return "오류: 날짜를 다시 입력해 주세요."
    input_list = input_text.split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 일이 있습니다."
    menu_list = [str(i) for i in range(1, 32)]
    for i in input_list:
        if not i in menu_list:
            return "오류: 날짜를 다시 입력해 주세요."
    return "True"


def is_valid_year_detail_str(input_text):
    if (not re.match(r"(\d{2}-\d{2}\/)*(\d{2}-\d{2})$", input_text)):
        return "오류: MM-DD 혹은 MM-DD/MM-DD/... 형식으로 입력해 주세요."
    input_list = input_text.split("/")
    if len(input_list) != len(set(input_list)):
        return "오류: 중복된 날짜가 있습니다."
    ##input_text 양식 12-31/10-13
    month_list = [i for i in range(1, 13)]  ##월
    for i in input_list:
        month = int(i.split("-")[0])
        day = int(i.split("-")[1])
        if (month not in month_list):
            return "오류: 월을 다시 입력해 주세요."
        if (day > 31 or day < 1):
            return "오류: 일을 다시 입력해 주세요."
        if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 29):
            return "오류: 일을 다시 입력해 주세요."
    return "True"


def is_valid_repeat(input_string):
    valid = ["없음", "매주", "매달", "매년"]
    if (input_string in valid):
        return True
    else:
        return False


def get_valid_date(year, month, day):  ##str 리턴
    if (is_valid_date(str(year) + "-" + str(month) + "-" + str(day))):
        ##
        return datetime.strptime(str(year) + "-" + str(month) + "-" + str(day), "%Y-%m-%d").date().strftime("%Y-%m-%d")
    else:
        if (month == 13):
            return get_valid_date(year + 1, 1, day)
        if (day == 0):
            return get_valid_date(year, month - 1, 31)
        return get_valid_date(year, month, day - 1)


def is_in_x_days(input_date, today, x):
    input_date = datetime.strptime(input_date, "%Y-%m-%d").date()
    today = datetime.strptime(today, "%Y-%m-%d").date()
    return (input_date - today).days <= x and (input_date - today).days >= 0


def compare_date_bool(dateA, date_B):
    if (dateA == "x"):
        return True
    dateA = datetime.strptime(dateA, "%Y-%m-%d").date()
    date_B = datetime.strptime(date_B, "%Y-%m-%d").date()
    return dateA > date_B  ##dateA가 더 늦으면 True


def compare_date_bool_include_equal(dateA, date_B):
    if (dateA == "x"):
        return True
    dateA = datetime.strptime(dateA, "%Y-%m-%d").date()
    date_B = datetime.strptime(date_B, "%Y-%m-%d").date()
    return dateA >= date_B  ##dateA가 더 늦으면 True


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
    if ("/" not in MM_YY):  ## MM-YY
        today = datetime.strptime(today_date, "%Y-%m-%d").date()
        month = int(MM_YY.split("-")[0])
        day = int(MM_YY.split("-")[1])
        this_year=datetime.strptime(get_valid_date(today.year, month, day), "%Y-%m-%d").date().strftime("%Y-%m-%d")
        next_year=datetime.strptime(get_valid_date(today.year+1, month, day), "%Y-%m-%d").date().strftime("%Y-%m-%d")
        return [this_year,next_year]
    else: ## MM-YY/MM-YY
        list = MM_YY.strip().split("/")
        result_list=[]
        for i in list:
            if change_date_to_this_week_year(i, today_date) not in result_list:
                result_list.extend(change_date_to_this_week_year(i, today_date))
        return result_list


def change_date_to_this_week_month(DD, today):
    ## 날짜를 today와 크거나 같고 30일 이내로 바꿔줌
    if ("/" not in DD):  ##
        today=datetime.strptime(today, "%Y-%m-%d").date()
        this_month_date = get_valid_date(int(today.year), today.month, int(DD))
        next_month_date = get_valid_date(int(today.year), today.month + 1, int(DD))
        return [this_month_date, next_month_date]
    else:
        list = DD.strip().split("/")
        result_list = []
        for i in list:
            for date in change_date_to_this_week_month(i, today):
                if date not in result_list and is_in_x_days(date, today, 31):
                    result_list.append(date)
        return result_list


def change_date_to_this_week_weekday(weekday, today):
    ## weekday를 today와 크거나 같고 30일 이내로 바꿔줌
    today = datetime.strptime(today, "%Y-%m-%d").date()
    if ("/" not in weekday):
        week_list = ["월", "화", "수", "목", "금", "토", "일"]
        week_num = week_list.index(weekday)
        while (today.weekday() != week_num):
            today = today + timedelta(days=1)
        return (today).strftime("%Y-%m-%d")
    else:
        list = weekday.strip().split("/")
        result_list = []
        for i in range(0,31,7):## 35일 이내의 모든 값이 나오게 됨
            calculated_today=today+timedelta(days=i)
            calculated_today=calculated_today.strftime("%Y-%m-%d")
            for j in list:
                result_list.append(change_date_to_this_week_weekday(j, calculated_today))
        return result_list

def input_menu(start, end, input_message):
    err_message = "오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
    return get_menu_input(input_message, err_message, start, end)


def get_menu_input(input_message, err_message, start, end):
    while (True):
        try:
            input_str = input(input_message)
            menu = int(input_str)
            if (menu < start or menu > end or len(input_str) != int(menu / 10) + 1):
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
        if (len(list) == 1):
            return list[0]
        else:
            return "/".join(list)


def remove_finish_date(finish_date, edit_date):
    list = finish_date.strip().split("/")
    if (edit_date in list):
        list.remove(edit_date)
    if (len(list) == 0):
        return "x"
    else:
        return "/".join(list)


def is_valid_search(text):
    ##text가 유효한지 검사
    ##단어 토큰이 'and or not' 혹은 5글자 이하 한글 이어야 함
    word_list = text.split(' ')
    for word in word_list:
        if word == '':
            print("오류: 입력을 해주세요")
        if word not in ['and', 'or', 'not'] and not is_valid_theme_a_word(word):
            print("오류: 올바르지 않은 입력이 포함되어 있습니다.")
            return False
    if (len(word_list) == 1 and word_list[0] in ['and', 'or', 'not']):
        print("오류: 입력이 논리 연산자 만을 포함하고 있습니다.")
        return False
    if (word_list[0] in ['and', 'or'] or word_list[-1] in ['and', 'or', 'not']):
        print("오류: 처음이나 끝에 논리 연산자는 사용할 수 없습니다.\n")
        return False
    ## not, or, and가 연속으로 나오면 안됨
    ## 단어가 연속으로 나오면 안됨
    ## or not은 가능
    for i in range(len(word_list) - 1):
        if word_list[i] not in ['and', 'or', 'not'] and word_list[i + 1] not in ['and', 'or', 'not']:
            print("오류: 연속된 단어는 사용할 수 없습니다.\n")
            return False
        if word_list[i] in ['and', 'or', 'not'] and word_list[i + 1] in ['and', 'or', 'not']:
            if ((word_list[i] == 'and' or word_list[i] == 'or') and word_list[i + 1] == 'not'):
                continue
            print("오류: 연속된 논리 연산자는 사용할 수 없습니다.\n")
            return False
        if word_list[i] == 'not' and word_list[i + 1] in ['and', 'or', 'not']:
            print("오류: not 연산자 뒤에는 단어가 와야 합니다.\n")
            return False
    return True


def get_query_func(query_text):
    ## query_text와 word_list를 받아서 True, False를 리턴하는 함수를 리턴
    ## and, not으로 이루어진 텍스트를 함수로 바꿔줌
    ## and는 두 함수를 and로 연결
    ## word_list가 query_text를 모두 만족해야 함.
    query_list = query_text.split(' ')
    postive_set = set()
    negative_set = set()
    if len(query_list) == 1:
        postive_set.add(query_list[0])
    else:
        if query_list[0] not in ['not']:
            postive_set.add(query_list[0])
        for i in range(1, len(query_list)):
            if query_list[i] not in ['and', 'not']:
                if query_list[i - 1] == 'and':
                    postive_set.add(query_list[i])
                elif query_list[i - 1] == 'not':
                    negative_set.add(query_list[i])

    ##func는 word_list를 받아서 True, False를 리턴하는 함수
    def func(theme_text):
        if(theme_text=="x"):
            word_list=[]
        else:
            word_list = theme_text.split('+')
        # print('word list: ',word_list)
        # print('theme text: ',theme_text)
        # print('positive list: ', postive_set)
        # print('negative list: ',negative_set)
        for word in word_list:
            if word in negative_set:
                # print('False')
                return False
        if (postive_set.issubset(set(word_list))):
            # print('True')
            return True
        else:
            # print('False')
            return False

    return func


def get_most_fast_calculate_date(repeat, repeat_detail, finish_date):
    calculated_dates = []
    if (repeat == "매주"):
        calculated_dates = change_date_to_this_week_weekday(repeat_detail, finish_date)
    elif (repeat == "매달"):
        calculated_dates = change_date_to_this_week_month(repeat_detail, finish_date)
    elif (repeat == "매년"):
        calculated_dates = change_date_to_this_week_year(repeat_detail, finish_date)
    ##calculated_dates 중 finish_date보다 빠른 날짜 필터링
    calculated_dates = [date for date in calculated_dates if compare_date_bool_include_equal(date, finish_date)]
    ##calculated_dates중 가장 빠른 날짜 리턴
    return min(calculated_dates)


def input_today():
    while True:
        # todaystr = input("오늘 날짜를 입력하세요(YYYY-MM-DD): ")
        todaystr = datetime.today().strftime("%Y-%m-%d")
        print("디버깅 귀찮으니 오늘 날짜는 현재 날짜"+todaystr+"로 자동 입력됩니다.")
        ret = is_valid_date_str(todaystr)
        if ret == "True":
            return todaystr
        else:
            print(ret)
