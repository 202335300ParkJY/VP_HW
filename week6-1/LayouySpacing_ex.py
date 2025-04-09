import sys

qt_modules = None

try:
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel,QGridLayout, )
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QFont
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,QGridLayout, )
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QFont
        qt_modules = 'PyQt6'
    except ImportError:
        print("There is no Qt Binding for Python.")
        sys.exit(1)
# ===========================================================
# 메인 윈도우 클래스 정의 (QWidget 상속)
class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # 타이틀& 크기 설정
        self.setWindowTitle("spacing of layout manager")
        self.resize(300, 200)
        # layout, widget func. 호출
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        # gridalyout 생성
        lm = QGridLayout()
        
        # 위젯 간 수직, 수평 간격 설정(픽셀 단위로)
        lm.setSpacing(1) # 1px 단위\
        
        # (0,0) 빨간 label 생성/ 추가
        self.label0 = QLabel('0,0')
        self.label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label0.setStyleSheet("background-color: red")
        self.label0.setFont(QFont("Arial", 20))
        lm.addWidget(self.label0, 0, 0)
        
        # (0,1) 파란 label 생성/ 추가
        self.label1 = QLabel('0,1')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setStyleSheet("background-color: blue")
        self.label1.setFont(QFont("Arial", 20))
        lm.addWidget(self.label0, 0, 1)
        
        # (0, 2) 위치에 분홍 배경의 label
        self.label2 = QLabel('0,2')
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setStyleSheet("background-color: pink")
        self.label2.setFont(QFont("Arial", 20))
        lm.addWidget(self.label2, 0, 2)
        
        # (1, 0) 위치부터 colSpan=3으로 흰 label 추가
        self.label3 = QLabel('1,0')
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setStyleSheet("background-color: white")
        self.label3.setFont(QFont("Arial", 20))
        lm.addWidget(self.label3, 1, 0, 1, 3)  # (row=1, col=0), rowSpan=1, colSpan=3

        # (2, 1) 위치부터 colSpan=2로 노란 label 추가
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
# ==================================================================================
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
        '''
        overloading는 같은 class에서 같은 이름의 메서드를 여러 번 정의(py.에선 연산자에서만)
        매개변수의 개수나 타입이 다르기에 각기 다른 메서드가 정의됨.
        '''
        super().resizeEvent(event) # collect 
        self.print_qsize()  # 크기 정보 크기

# entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)  
    main_wnd = MW()               
    sys.exit(app.exec())         
