import sys
import logging

# 로그 설정
logging.basicConfig(level=logging.INFO)

# Qt 모듈을 동적으로 불러오는 처리
qt_modules = None

try:
    from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
    from PySide6.QtCore import Qt
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox
        from PyQt6.QtCore import Qt
        qt_modules = 'PyQt6'
    except ImportError:
        logging.error("There is no Qt Binding for Python.")
        sys.exit(1)

logging.info(f"Using {qt_modules} binding.")

# ============================================================

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  # UI 초기화

    def init_ui(self):
        """
        UI 설정 함수
        - 윈도우 제목 설정
        - 레이아웃 설정
        - 콤보박스와 레이블을 배치
        """
        self.setWindowTitle("Ex: QCombobox")  # 창 제목 설정
        self.resize(400, 200)  # 창 크기 설정
        self.setup_main_wnd()  # 메인 윈도우 설정
        self.show()  # 창 표시

    def setup_main_wnd(self):
        """
        메인 윈도우의 레이아웃 설정
        - 레이블과 콤보박스를 배치
        """
        layout = QVBoxLayout()  # 수직 레이아웃 생성

        # 질문 레이블 추가
        layout.addWidget(QLabel('What is most important?'))

        # 콤보박스 아이템 리스트
        self.items = ['faith', 'hope', 'love']
        
        # 콤보박스 생성 및 아이템 추가
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.items)  # 아이템 추가

        # 콤보박스와 관련된 이벤트 연결
        self.combo_box.activated.connect(self.on_selected)  # 아이템 선택 시
        self.combo_box.currentIndexChanged.connect(self.on_current_idx_changed)  # 인덱스 변경 시

        # 콤보박스를 레이아웃에 추가
        layout.addWidget(self.combo_box)

        # 선택된 아이템을 표시할 레이블 추가
        self.dp_label = QLabel("")
        layout.addWidget(self.dp_label)

        self.setLayout(layout)  # 레이아웃을 메인 윈도우에 적용

    def on_selected(self, idx):
        """
        유저가 콤보박스에서 아이템을 선택할 때 호출되는 슬롯
        - 선택된 아이템을 레이블에 표시하고, 로그로 출력
        """
        selected_item = self.items[idx]
        message = f"You selected: {selected_item}"
        
        logging.info(message)  # 로그에 메시지 기록
        self.dp_label.setText(message)  # 레이블에 표시

    def on_current_idx_changed(self, idx):
        """
        콤보박스의 현재 인덱스가 변경될 때 호출되는 슬롯
        - 변경된 인덱스를 로그로 출력
        """
        logging.info(f'"currentIndexChanged" occurred: {idx}')

# ============================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()  # 메인 윈도우 객체 생성
    sys.exit(app.exec())  # 애플리케이션 실행
