import sys

# Qt 바인딩을 PySide6 우선 사용하고, 실패 시 PyQt6 사용
qt_modules = None

try:
    # PySide6 우선 시도
    from PySide6.QtWidgets import (
        QApplication, QWidget, 
        QLabel,
        QGridLayout, 
    )
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QFont
    qt_modules = 'PySide6'
except ImportError:
    # PySide6 import 실패 시, PyQt6을 시도
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget, 
            QLabel,
            QGridLayout, 
        )
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QFont
        qt_modules = 'PyQt6'
    except ImportError:
        # 둘 다 실패한 경우 메시지 출력 후 종료
        print("There is no Qt Binding for Python.")
        sys.exit(1)

# 메인 윈도우 클래스 정의 (QWidget 상속)
class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 윈도우 타이틀과 크기 설정
        self.setWindowTitle("Ex: Spacing of LayoutManager")
        self.resize(300, 200)
        # 레이아웃 및 위젯 설정 함수 호출
        self.setup_main_wnd()
        # 윈도우 표시
        self.show()

    def setup_main_wnd(self):
        # GridLayout 생성
        lm = QGridLayout()

        # 위젯 간의 수평/수직 간격 설정 (픽셀 단위)
        lm.setSpacing(1)

        # (0, 0) 위치에 빨간 배경의 label 생성 및 추가
        self.label0 = QLabel('0,0')
        self.label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label0.setStyleSheet("background-color: red")
        self.label0.setFont(QFont("Arial", 20))
        lm.addWidget(self.label0, 0, 0)

        # (0, 1) 위치에 파란 배경의 label
        self.label1 = QLabel('0,1')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setStyleSheet("background-color: blue")
        self.label1.setFont(QFont("Arial", 20))
        lm.addWidget(self.label1, 0, 1)

        # (0, 2) 위치에 분홍 배경의 label
        self.label2 = QLabel('0,2')
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet("background-color: pink")
        self.label2.setFont(QFont("Arial", 20))
        lm.addWidget(self.label2, 0, 2)

        # (1, 0) 위치부터 colSpan=3으로 흰 배경의 label 추가
        self.label3 = QLabel('1,0')
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setStyleSheet("background-color: white")
        self.label3.setFont(QFont("Arial", 20))
        lm.addWidget(self.label3, 1, 0, 1, 3)  # (row=1, col=0), rowSpan=1, colSpan=3

        # (2, 1) 위치부터 colSpan=2로 노란 배경의 label 추가
        self.label4 = QLabel('2,1')
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setStyleSheet("background-color: yellow")
        self.label4.setFont(QFont("Arial", 20))
        lm.addWidget(self.label4, 2, 1, 1, 2)  # (row=2, col=1), rowSpan=1, colSpan=2

        # 레이아웃 주변 여백 설정 (왼쪽, 위, 오른쪽, 아래 순)
        lm.setContentsMargins(30, 30, 30, 30)
        # 위젯 간 간격 다시 설정 (10픽셀)
        lm.setSpacing(10)

        # 레이아웃을 현재 위젯에 설정
        self.setLayout(lm)

    # 각 QLabel 위젯의 sizeHint() 및 실제 size(), sizePolicy 정보 출력
    def print_qsize(self):
        print('==============================')
        print("label0's ideal size (=sizeHint)     :", self.label0.sizeHint())
        print("label1's ideal size (=sizeHint)     :", self.label1.sizeHint())
        print("label2's ideal size (=sizeHint)     :", self.label2.sizeHint())
        print("label3's ideal size (=sizeHint)     :", self.label3.sizeHint())
        print("label4's ideal size (=sizeHint)     :", self.label4.sizeHint())
        print('==============================')
        print("label0's size      :", self.label0.size(), "/",
              self.label0.sizePolicy().verticalPolicy(), "/",
              self.label0.sizePolicy().horizontalPolicy())
        print("label1's size      :", self.label1.size(), "/",
              self.label1.sizePolicy().verticalPolicy(), "/",
              self.label1.sizePolicy().horizontalPolicy())
        print("label2's size      :", self.label2.size(), "/",
              self.label2.sizePolicy().verticalPolicy(), "/",
              self.label2.sizePolicy().horizontalPolicy())
        print("label3's size      :", self.label3.size(), "/",
              self.label3.sizePolicy().verticalPolicy(), "/",
              self.label3.sizePolicy().horizontalPolicy())
        print("label4's size      :", self.label4.size(), "/",
              self.label4.sizePolicy().verticalPolicy(), "/",
              self.label4.sizePolicy().horizontalPolicy())

    # 윈도우 크기 변경 시 자동 호출되는 이벤트 핸들러
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.print_qsize()  # 크기 정보 출력


# 프로그램 실행 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 인스턴스 생성
    main_wnd = MW()               # 메인 윈도우 생성 및 실행
    sys.exit(app.exec())          # 이벤트 루프 시작
