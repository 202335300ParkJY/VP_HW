# 필요한 모듈 불러오기
import sys, json
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QCheckBox, QLineEdit, QGridLayout) 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


# 메인 윈도우 클래스 정의
class MW(QWidget):

    def __init__(self):
        super().__init__() 
        self.init_ui()

    def init_ui(self):
        """GUI 초기 설정"""
        # self.setMinimumSize(500, 500)  # 필요한 경우 최소 크기 설정 가능
        self.setWindowTitle("QGridLayout Example")  # 창 제목 설정

        self.setup_mw()  # 레이아웃 및 위젯 배치
        self.show()      # 창 보여주기

    def setup_mw(self):                
        # 메인 그리드 레이아웃 생성
        self.main_grid = QGridLayout()

        # 체크박스와 QLineEdit 위젯을 각각 5개씩 생성하여 배치
        for i in range(5):
            cb = QCheckBox()  # 체크박스 생성
            cb.stateChanged.connect(self.print_text)  # 상태 변경 시 이벤트 연결
            self.main_grid.addWidget(cb, i, 0)  # (i행, 0열)에 추가

            ledit = QLineEdit()  # 텍스트 입력 필드 생성
            ledit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
            self.main_grid.addWidget(ledit, i, 1, 1, 2)  # (i행, 1열 시작, 열 2칸 차지)

        # 체크된 항목들을 표시할 라벨 추가 (5행, 0열부터 2열까지 차지)
        self.dp_label = QLabel("")
        self.dp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_grid.addWidget(self.dp_label, 5, 0, 1, 2)

        # 레이아웃을 현재 위젯에 설정
        self.setLayout(self.main_grid)

    def print_text(self):
        """체크된 항목들의 텍스트를 읽어와 하단 라벨에 출력"""
        dp_text = ""

        for i in range(5):
            # (i행, 0열)의 체크박스 가져오기
            item = self.main_grid.itemAtPosition(i, 0)
            widget = item.widget()            

            if widget.isChecked():  # 체크되어 있는 경우
                # (i행, 1열)의 QLineEdit 가져오기
                item = self.main_grid.itemAtPosition(i, 1) 
                widget = item.widget()
                text = widget.text()  # 입력된 텍스트 읽기
                dp_text += f"[{text}]"  # 형식 맞춰 문자열에 추가

        # (5행, 0열)에 있는 라벨에 최종 문자열 출력
        item = self.main_grid.itemAtPosition(5, 0)
        widget = item.widget()
        widget.setText(dp_text)

        # 아래와 같이 직접 접근해도 되지만, 연습 목적상 위처럼 처리
        # self.dp_label.setText(dp_text)  

# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MW()
    sys.exit(app.exec())
