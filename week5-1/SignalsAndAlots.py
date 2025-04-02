import sys

# PyQt6의 주요 위젯과 레이아웃을 import합니다.
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QCheckBox, QButtonGroup)
from PyQt6.QtCore import Qt

# 메인 윈도우 클래스
class MW (QWidget):

    def __init__(self):
        super().__init__()  # 부모 클래스(QWidget)의 초기화 메서드를 호출
        self.init_ui()  # UI 초기화 함수 호출

    def init_ui(self):
        self.setWindowTitle("Ex: QCheckbox")  # 윈도우 타이틀 설정
        self.setup_main_wnd()  # 메인 윈도우 설정 함수 호출
        self.show()  # 윈도우를 화면에 표시

    def setup_main_wnd(self):
        lm = QVBoxLayout()  # 세로 방향 레이아웃을 생성

        # 중요한 항목에 대한 질문을 QLabel로 추가
        lm.addWidget(QLabel('What is most important?'))

        # QButtonGroup 생성. 체크박스를 그룹으로 묶기 위해 사용.
        self.bg = QButtonGroup(self)

        # 첫 번째 체크박스를 생성하고 레이아웃에 추가
        self.cb01 = QCheckBox('1. faith')
        lm.addWidget(self.cb01)
        self.bg.addButton(self.cb01)  # 버튼 그룹에 체크박스 추가

        # 두 번째 체크박스를 생성하고 레이아웃에 추가
        self.cb02 = QCheckBox('2. hope')
        lm.addWidget(self.cb02)
        self.bg.addButton(self.cb02)  # 버튼 그룹에 체크박스 추가

        # 세 번째 체크박스를 생성하고 레이아웃에 추가
        self.cb03 = QCheckBox('3. love')
        lm.addWidget(self.cb03)
        self.bg.addButton(self.cb03)  # 버튼 그룹에 체크박스 추가

        # QButtonGroup을 독점적(exclusive)으로 설정
        self.bg.setExclusive(True)

        # 체크박스가 클릭될 때 호출될 슬롯 연결
        self.bg.buttonClicked.connect(self.ck_click)

        # 선택된 체크박스를 표시할 레이블 추가
        self.dp_label = QLabel("")
        lm.addWidget(self.dp_label)

        # 다중 선택을 위한 체크박스 추가
        self.cb = QCheckBox('Check it for the multiple selection.')
        # self.cb.toggle()  # 기본값을 토글(켜고 끄는) 상태로 설정하려면 사용
        self.cb.stateChanged.connect(self.ck_multiple)  # 상태가 변경될 때 호출될 슬롯 연결
        lm.addWidget(self.cb)

        # 레이아웃을 윈도우에 설정
        self.setLayout(lm)

    # 체크박스 클릭 시 호출되는 함수
    def ck_click(self, button):
        tmp = ""  # 선택된 버튼의 텍스트를 저장할 변수
        tmp = button.text()  # 클릭된 버튼의 텍스트 가져오기

        print(tmp)  # 선택된 항목을 콘솔에 출력
        self.dp_label.setText(tmp)  # 선택된 항목을 레이블에 표시

    # 다중 선택이 가능한지 여부를 설정하는 함수
    def ck_multiple(self, state):
        if state == Qt.CheckState.Checked:  # 체크박스가 체크되었을 때
            self.bg.setExclusive(True)  # 독점 모드 활성화 (단일 선택)
        else:  # 체크박스가 체크되지 않았을 때
            self.bg.setExclusive(False)  # 독점 모드 비활성화 (다중 선택 가능)


# 프로그램 시작 지점
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    main_wnd = MW()  # 메인 윈도우 객체 생성
    sys.exit(app.exec())  # 이벤트 루프 시작
