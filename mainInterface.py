from interface import interface
class MainInterface(interface):
    def __init__(self):
        self.text = "<메인 메뉴>\n" \
                 "1. TODO 확인하기\n" \
                 "2. TODO 추가하기\n" \
                 "0. 종료하기\n" \
                 "\n" \
                 "TODO/메뉴 선택>"
        self.err_message="오류: 잘못 된 입력 입니다. 이동하려는 메뉴의 번호를 한자리 숫자로 입력해 주세요."
        self.range=2