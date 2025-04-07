import sys
import traceback

# PySide6 사용 시도
PYSIDE = True
try:
    from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QHBoxLayout)
    from PySide6.QtCore import Qt
except:
    # PySide6 import 실패 시 에러 메시지 출력
    e_msg = traceback.format_exc()
    print(e_msg)
    PYSIDE = False    

# PyQt6 사용 시도 (PySide6 실패 시 대체)
PYQT = True
if not PYSIDE:
    try:
        from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QHBoxLayout)
        from PyQt6.QtCore import Qt
    except:
        # PyQt6 import 실패 시 에러 메시지 출력
        e_msg = traceback.format_exc()
        print(e_msg)
        PYQT = False

# 색상과 텍스트를 가지는 QLabel을 정의하는 커스텀 클래스
class DsLabel(QLabel):
    def __init__(self, text, color):
        super().__init__(text)
        # 배경색 설정
        self.setStyleSheet(f"background-color: {color}")
        # 텍스트 중앙 정렬
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

# 메인 윈도우 클래스 정의
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # UI 초기 설정
    def init_ui(self):
        self.setWindowTitle("Ex: QHBoxLayout")  # 창 제목 설정
        self.setup_main_wnd()                   # 레이아웃 설정
        self.show()                             # 창 띄우기

    # 메인 위젯과 수평 레이아웃 구성
    def setup_main_wnd(self):
        lm = QHBoxLayout()  # 수평 박스 레이아웃 생성

        # 다섯 가지 색상으로 라벨 추가
        colors = ['red', 'green', 'blue', 'magenta', 'yellow']
        for i, c in enumerate(colors):
            lm.addWidget(DsLabel(str(i), c))  # 인덱스 번호와 색상을 가지는 라벨 추가

        # QWidget에 레이아웃 설정 후 중앙 위젯으로 지정
        dummy = QWidget()
        dummy.setLayout(lm)
        self.setCentralWidget(dummy)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 인스턴스 생성
    main_wnd = MW()               # 메인 윈도우 생성 및 표시
    sys.exit(app.exec())          # 이벤트 루프 진입
