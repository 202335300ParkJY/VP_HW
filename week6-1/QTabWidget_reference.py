import sys, os

# Qt 바인딩을 PySide6 우선 사용
qt_modules = None
try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QLabel,
        QVBoxLayout, QTabWidget
    )
    from PySide6.QtGui import QPixmap
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget, QLabel,
            QVBoxLayout, QTabWidget
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
        self.setWindowTitle("Ex: QTabWidget with Images")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        # 현재 파일의 경로 기준 이미지 디렉토리 지정
        fpath = os.path.dirname(os.path.abspath(__file__))

        # 탭 이름들
        pages = ['faith', 'hope', 'love']

        # 이미지 파일 경로 리스트
        self.imgs = [
            os.path.join(fpath, 'img/faith.png'),
            os.path.join(fpath, 'img/hope.png'),
            os.path.join(fpath, 'img/love.png')
        ]

        # QTabWidget 생성
        tab_widget = QTabWidget()

        # 각 탭에 QLabel + 이미지 설정
        for idx, title in enumerate(pages):
            label = QLabel()
            pixmap = QPixmap(self.imgs[idx])
            label.setPixmap(pixmap)
            label.setScaledContents(True)  # 이미지 크기를 자동으로 조정
            tab_widget.addTab(label, title)  # 탭에 QLabel 추가

        # 수직 레이아웃으로 QTabWidget 배치
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

# ------------------------------------

if __name__ == "__main__":
    print(os.path.realpath(__file__))
    app = QApplication(sys.argv)
    wdw = MW()
    sys.exit(app.exec())
