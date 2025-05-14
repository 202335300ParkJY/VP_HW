import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                              QWidget, QTextEdit, QLabel)
from PySide6.QtCore import Qt

# ===================================================================

class FocusPolicyDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 포커스 정책 데모")
        self.setGeometry(100, 100, 500, 600)

        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 레이아웃 생성
        layout = QVBoxLayout(central_widget)

        # NoFocus 위젯
        layout.addWidget(QLabel("Qt.NoFocus - 키보드 포커스를 받지 않음:"))
        no_focus = QTextEdit("이 텍스트 편집기는 포커스를 받지 않습니다. 클릭해도 수정할 수 없습니다.")
        no_focus.setFocusPolicy(Qt.NoFocus)
        layout.addWidget(no_focus)

        # TabFocus 위젯
        layout.addWidget(QLabel("Qt.TabFocus - 탭 키로만 포커스 받음:"))
        tab_focus = QTextEdit("이 텍스트 편집기는 탭 키로만 포커스를 받습니다. 클릭해도 포커스가 오지 않습니다.")
        tab_focus.setFocusPolicy(Qt.TabFocus)
        layout.addWidget(tab_focus)

        # ClickFocus 위젯
        layout.addWidget(QLabel("Qt.ClickFocus - 마우스 클릭으로만 포커스 받음:"))
        click_focus = QTextEdit("이 텍스트 편집기는 클릭으로만 포커스를 받습니다. 탭 키로는 이동할 수 없습니다.")
        click_focus.setFocusPolicy(Qt.ClickFocus)
        layout.addWidget(click_focus)

        # StrongFocus 위젯
        layout.addWidget(QLabel("Qt.StrongFocus - 탭 키와 마우스 클릭으로 포커스 받음:"))
        strong_focus = QTextEdit("이 텍스트 편집기는 탭 키와 클릭 모두로 포커스를 받습니다.")
        strong_focus.setFocusPolicy(Qt.StrongFocus)
        layout.addWidget(strong_focus)

        # WheelFocus 위젯
        layout.addWidget(QLabel("Qt.WheelFocus - 탭 키, 마우스 클릭, 마우스 휠로 포커스 받음:"))
        wheel_focus = QTextEdit("이 텍스트 편집기는 탭 키, 클릭, 휠 모두로 포커스를 받습니다.")
        wheel_focus.setFocusPolicy(Qt.WheelFocus)
        layout.addWidget(wheel_focus)

        # 초기 포커스 설정
        strong_focus.setFocus()

    def keyPressEvent(self, event):
        # ESC 키를 누르면 애플리케이션 종료
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FocusPolicyDemo()
    window.show()
    sys.exit(app.exec())