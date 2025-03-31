#juy20_button.py
# ----------------------------------------

import sys, os

PYSIDE6_MODE = True
PYQT_MODE = False

try:
    from PySide6.QtWidgets import (QApplication, QWidget, 
                                QLabel, QPushButton)
    from PySide6.QtGui import QFont,QIcon
    from PySide6.QtCore import Qt,QSize
except Exception as e:
    print(f"PySide6 import failed: {e}")
    PYSIDE6_MODE = False
    PYQT_MODE = True

if not PYSIDE6_MODE:
    try:
        from PyQt6.QtWidgets import (QApplication, QWidget, 
                                    QLabel, QPushButton)
        from PyQt6.QtGui import QFont,QIcon
        from PyQt6.QtCore import Qt,QSize
    except Exception as e:
        print(f"PyQt6 import failed: {e}")
        PYQT_MODE = False

if not PYSIDE6_MODE and not PYQT_MODE:
    print("No availabe Qt Binding found! Plz install PySide6 or PyQt6.")
    sys.exit(1)

# -------------------------------
class MW(QWidget):

    def __init__(self):  
        super().__init__()  
        self.init_ui()  # UI 초기화 함수 호출

    def init_ui(self):
        #self.setFixedSize(250,250)  # 창 크기를 고정합니다 (현재 비활성화됨)
        self.setWindowTitle('QPushButton Example')  
        self.setup_main_wnd()  
        self.show()  

    def setup_main_wnd(self):
        # self.hello_label = QLabel('Hello, World and Qt!',self) # 아래 두라인과 동일한 수행.
        self.hello_label = QLabel(self)  
        self.hello_label.setText('Hello, World and Qt!')  
        self.hello_label.setFont(QFont('Arial', 15))  
        self.hello_label.resize(230, 40)  

        # 아래 code line을 적절히 주석해제하여 동작을 확인해 볼것.
        # self.hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) # PyQt6용 중앙 정렬 
        # self.hello_label.setAlignment(Qt.AlignCenter)               # PySide6용 중앙 정렬
        # self.hello_label.setStyleSheet("background-color: yellow")  # 배경색 노란색 (둘 다 호환)
        # -----------------
        self.hello_label.move(10, 20)  # 라벨 위치 설정

        # 이미지 파일 경로 얻기
        path_py_file = os.path.realpath(__file__)  # 현재 실행 중인 스크립트의 절대 경로
        path_py_file = os.path.dirname(path_py_file)  # 스크립트가 있는 디렉토리 경로
        img_fstr = os.path.join(path_py_file, "earthblue_map-1324554.jpg!d")

        # 아이콘과 텍스트가 있는 버튼 생성
        it_button = QPushButton("icon and text button", self)  # 버튼 생성 및 텍스트 설정
        it_button.setIcon(QIcon(img_fstr))  # 버튼에 아이콘 설정
        it_button.clicked.connect(self.it_btn_clicked)  # 클릭 이벤트 핸들러 연결
        it_button.resize(150, 50)  # 버튼 크기 설정
        it_button.move(50, 70)  # 버튼 위치 설정

        # 아이콘만 있는 버튼 생성
        icon_button = QPushButton(self)  # 텍스트 없는 버튼 생성
        icon_button.setIcon(QIcon(img_fstr))  # 버튼에 아이콘 설정
        icon_button.clicked.connect(self.icon_btn_clicked)  # 클릭 이벤트 핸들러 연결
        icon_button.setIconSize(QSize(120, 30))  # 아이콘 크기 설정
        icon_button.resize(150, 50)  # 버튼 크기 설정
        icon_button.move(50, 130)  # 버튼 위치 설정

        # 텍스트만 있는 버튼 생성
        text_button = QPushButton("text button", self)  # 버튼 생성 및 텍스트 설정
        text_button.clicked.connect(self.text_btn_clicked)  # 클릭 이벤트 핸들러 연결
        text_button.resize(150, 50)  # 버튼 크기 설정
        text_button.move(50, 190)  # 버튼 위치 설정

    def it_btn_clicked(self):
        """아이콘과 텍스트 버튼 클릭 이벤트 핸들러"""
        self.hello_label.setText("Icon and txt Button")  # 라벨 텍스트 변경

    def icon_btn_clicked(self):
        """아이콘 버튼 클릭 이벤트 핸들러"""
        self.hello_label.setText("Icon Button")  # 라벨 텍스트 변경

    def text_btn_clicked(self):
        """텍스트 버튼 클릭 이벤트 핸들러"""
        self.hello_label.setText("text Button")  # 라벨 텍스트 변경

# 스크립트가 직접 실행될 때만 아래 코드 실행        
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 인스턴스 생성
    wnd = MW()  # 메인 창 인스턴스 생성
    sys.exit(app.exec())  # 이벤트 루프 시작 및 앱 종료 시 시스템에 종료 코드 반환

