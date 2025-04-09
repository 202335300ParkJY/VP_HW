
import sys, os

# Qt 바인딩을 PySide6 우선, PyQt6는 백업용
qt_modules = None

try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QLabel,
        QVBoxLayout, QComboBox, QStackedWidget
    )
    from PySide6.QtGui import QPixmap
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget, QLabel,
            QVBoxLayout, QComboBox, QStackedWidget
        )
        from PyQt6.QtGui import QPixmap
        qt_modules = 'PyQt6'
    except ImportError:
        print("There is no Qt Binding for Python.")
        sys.exit(1)

print(f"Using {qt_modules} binding.")

# ------------------------------------

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QStackedWidget with ComboBox")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        # 현재 스크립트 경로를 기준으로 이미지 파일 위치 설정
        fpath = os.path.dirname(os.path.abspath(__file__))

        # 페이지 이름과 이미지 경로 정의
        pages = ['faith', 'hope', 'love']
        self.imgs = [
            os.path.join(fpath, 'img/faith.png'),
            os.path.join(fpath, 'img/hope.png'),
            os.path.join(fpath, 'img/love.png')
        ]

        # 콤보박스 생성 및 페이지 이름 추가
        combo_box = QComboBox()
        combo_box.addItems(pages)
        combo_box.activated.connect(self.change_page)

        # QStackedWidget 생성
        self.stack_widget = QStackedWidget()

        # 각 페이지에 해당하는 QLabel + 이미지 추가
        for idx in range(len(pages)):
            label = QLabel()
            pixmap = QPixmap(self.imgs[idx])
            label.setPixmap(pixmap)
            label.setScaledContents(True)  # 이미지가 QLabel에 맞게 리사이즈됨
            self.stack_widget.addWidget(label)

        # 수직 레이아웃 구성: 콤보박스 위, 이미지 아래
        layout = QVBoxLayout()
        layout.addWidget(combo_box)
        layout.addWidget(self.stack_widget)

        self.setLayout(layout)

    # 콤보박스 인덱스 선택 시 보여줄 페이지 변경
    def change_page(self, idx):
        self.stack_widget.setCurrentIndex(idx)

# ------------------------------------

if __name__ == "__main__":
    print(os.path.realpath(__file__))
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())

