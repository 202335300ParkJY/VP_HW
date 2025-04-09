import sys, os

# Qt 바인딩을 PySide6 우선 사용하고, 실패 시 PyQt6 사용
qt_modules = None

# PySide6을 먼저 시도
try:
    from PySide6.QtWidgets import (
        QApplication, QWidget,
        QStackedLayout, QVBoxLayout,
        QLabel,
        QComboBox, 
    )
    from PySide6.QtGui import QPixmap
    qt_modules = 'PySide6'
except ImportError:
    # 실패 시 PyQt6 시도
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget,
            QStackedLayout, QVBoxLayout,
            QLabel,
            QComboBox, 
        )
        from PyQt6.QtGui import QPixmap
        qt_modules = 'PyQt6'
    except ImportError:
        # 둘 다 실패하면 메시지 출력 후 종료
        print("There is no Qt Binding for Python.")
        sys.exit(1)

# 사용된 Qt 바인딩 이름 출력
print(f"Using {qt_modules} binding.")

# ------------------------------------

# 메인 윈도우 클래스 정의
class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 윈도우 타이틀 설정
        self.setWindowTitle("Ex Input Widgets")
        # 메인 위젯 및 레이아웃 구성
        self.setup_main_wnd()
        # 윈도우 표시
        self.show()

    def setup_main_wnd(self):
        # 현재 파일의 절대 경로 기준 디렉토리 경로 얻기
        fpath = os.path.dirname(
            os.path.abspath(__file__)
        )

        # 콤보박스에 표시될 페이지 이름들
        pages = ['faith', 'hope', 'love']

        # 각 페이지에 해당하는 이미지 파일 경로 리스트
        self.imgs = [
            os.path.join(fpath, 'img/faith.png'),
            os.path.join(fpath, 'img/hope.png'),
            os.path.join(fpath, 'img/love.png')
        ]

        # 콤보박스 생성 및 항목 추가
        combo_box = QComboBox()
        combo_box.addItems(pages)
        # 콤보박스 항목이 선택되면 change_page 함수 실행
        combo_box.activated.connect(self.change_page)

        # QStackedLayout 생성 (여러 페이지를 겹쳐서 보관, 하나만 보여줌)
        self.stacked_lm = QStackedLayout()

        # 페이지 수만큼 QLabel 생성 후 QStackedLayout에 추가
        for idx, c in enumerate(pages):
            label = self.setup_page(idx)  # QLabel을 생성하고 이미지 설정
            self.stacked_lm.addWidget(label)  # 스택에 추가

        # 수직 박스 레이아웃 생성
        v_box_lm = QVBoxLayout()
        v_box_lm.addWidget(combo_box)         # 콤보박스를 위에 추가
        v_box_lm.addLayout(self.stacked_lm)   # 스택 레이아웃을 아래에 추가

        # 최종 레이아웃을 윈도우에 설정
        self.setLayout(v_box_lm)

    # 페이지용 QLabel 설정 함수
    def setup_page(self, page_num):
        label = QLabel()
        pixmap = QPixmap(self.imgs[page_num])     # 해당 이미지 불러오기
        label.setPixmap(pixmap)                   # QLabel에 이미지 설정
        label.setScaledContents(True)             # QLabel 크기에 맞게 이미지 자동 조절
        return label

    # 콤보박스에서 선택된 인덱스에 해당하는 페이지를 보여줌
    def change_page(self, idx):
        self.stacked_lm.setCurrentIndex(idx)

# ------------------------------------

# 프로그램 진입점
if __name__ == "__main__":
    print(os.path.realpath(__file__))  # 현재 실행 중인 파일 경로 출력
    app = QApplication(sys.argv)       # QApplication 인스턴스 생성
    main_wnd = MW()                         # 메인 윈도우 생성
    sys.exit(app.exec())               # 이벤트 루프 실행
