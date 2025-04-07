import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton)
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    """
    MainWindow는 QVBoxLayout과 QSizePolicy를 사용한 예제입니다.
    이 예제에서는 다양한 위젯의 크기 정책을 설정하고
    리사이즈 이벤트가 발생할 때 그 크기 변화를 출력합니다.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        UI 초기화 함수
        - 창의 제목, 레이아웃, 위젯들을 설정하고,
        - 레이아웃에 위젯들을 추가하여 표시합니다.
        """
        self.setWindowTitle("Ex: QVBoxLayout and QSizePolicy")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        """
        메인 윈도우의 레이아웃과 위젯을 설정하는 함수
        - QVBoxLayout을 사용하여 위젯들을 배치하고,
        - 각 위젯에 대한 QSizePolicy를 적용하여 크기 정책을 설정합니다.
        """
        layout = QVBoxLayout()

        # 레이블 추가
        self.label0 = QLabel('Enter text!')
        layout.addWidget(self.label0)

        # 고정 간격 추가
        layout.addSpacing(10)

        self.label1 = QLabel('--------')
        layout.addWidget(self.label1)

        # 고정 간격 추가
        layout.addSpacing(20)

        # Line Edit (텍스트 입력 필드)
        self.line_edit = QLineEdit()
        self.set_size_policy_for_line_edit()  # QLineEdit의 사이즈 정책 설정
        layout.addWidget(self.line_edit)

        # Stretch 추가 (남은 공간을 채움)
        layout.addStretch(1)

        # 두 번째 레이블
        self.label2 = QLabel('--------')
        layout.addWidget(self.label2)

        # Stretch 추가 (남은 공간을 채움)
        layout.addStretch(2)

        # 버튼 추가
        self.push_button = QPushButton("Check")
        self.set_size_policy_for_push_button()  # QPushButton의 사이즈 정책 설정
        layout.addWidget(self.push_button)

        # 위젯들의 크기 정보 출력
        self.print_qsize()

        # 레이아웃 설정
        self.setLayout(layout)

    def set_size_policy_for_line_edit(self):
        """
        QLineEdit의 QSizePolicy를 설정하는 함수
        """
        # 여기서 QSizePolicy를 "Preferred"로 설정하면 크기가 기본 크기대로 설정됩니다.
        # self.line_edit.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        # QLineEdit를 Expanding으로 설정 (여기서는 사이즈 정책을 Expanding으로 설정)
        self.line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def set_size_policy_for_push_button(self):
        """
        QPushButton의 QSizePolicy를 설정하는 함수
        """
        # 버튼을 Expanding으로 설정
        # self.push_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.push_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

    def print_qsize(self):
        """
        각 위젯들의 사이즈 정보와 사이즈 정책을 출력하는 함수
        """
        print('==============================')
        print("label0's ideal size (=sizeHint)     :", self.label0.sizeHint())
        print("label1's ideal size (=sizeHint)     :", self.label1.sizeHint())
        print("label2's ideal size (=sizeHint)     :", self.label2.sizeHint())
        print("line_edit's ideal size (=sizeHint)  :", self.line_edit.sizeHint())
        print("push_button's ideal size (=sizeHint):", self.push_button.sizeHint())
        print('==============================')
        self.print_widget_size(self.label0)
        self.print_widget_size(self.label1)
        self.print_widget_size(self.label2)
        self.print_widget_size(self.line_edit)
        self.print_widget_size(self.push_button)

    def print_widget_size(self, widget):
        """
        위젯의 사이즈와 사이즈 정책을 출력하는 함수
        """
        print(f"{widget.objectName()}'s size      : {widget.size()} / {widget.sizePolicy().verticalPolicy()} / {widget.sizePolicy().horizontalPolicy()}")

    def resizeEvent(self, event):
        """
        리사이즈 이벤트 핸들러
        - 윈도우 크기 변경 시 위젯들의 크기 정보 출력
        """
        super().resizeEvent(event)
        self.print_qsize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MainWindow()
    sys.exit(app.exec())
