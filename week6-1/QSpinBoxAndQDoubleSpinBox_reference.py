import sys

# Qt 바인딩: PySide6 우선, 실패 시 PyQt6 백업
qt_modules = None
try:
    from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QVBoxLayout,
        QLabel, QSpinBox,
    )
    from PySide6.QtCore import Qt
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (
            QApplication, QMainWindow,
            QWidget, QVBoxLayout,
            QLabel, QSpinBox,
        )
        from PyQt6.QtCore import Qt
        qt_modules = 'PyQt6'
    except ImportError:
        # 둘 다 import 실패 시 에러 메시지 출력 후 종료
        print("There is no Qt Binding for Python.")
        sys.exit(1)

# 사용 중인 Qt 바인딩 출력
print(f"Using {qt_modules} binding.")

# 메인 윈도우 클래스 정의
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # UI 초기화

    def init_ui(self):
        # 윈도우 기본 설정
        self.setWindowTitle("QSpinBox with Validation and Formatting")
        self.setGeometry(100, 100, 300, 200)

        # 중앙 위젯과 레이아웃 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QSpinBox 생성 및 설정
        self.spinbox = QSpinBox()
        self.spinbox.setRange(100, 100000)         # 허용 범위: 1,000 ~ 100,000
        self.spinbox.setValue(777)                 # 초기값: 5,000
        self.spinbox.setSingleStep(1000)            # 증감 단위: 1,000
        self.spinbox.setPrefix("Level ")            # 접두사: "Level "
        self.spinbox.setSuffix(" pts")              # 접미사: " pts"
        self.spinbox.setMaximumWidth(180)           # 최대 너비 제한 (UI 깨짐 방지)

        # 값 변경 시 슬롯 함수(on_value_changed) 연결
        self.spinbox.valueChanged.connect(self.on_value_changed)

        # QSpinBox 추가
        layout.addWidget(self.spinbox)

        # 결과 표시용 QLabel 생성 및 추가
        self.label = QLabel()
        layout.addWidget(self.label)

        # 초기 상태에서 라벨에 현재 값 표시
        self.on_value_changed(self.spinbox.value())

    # QSpinBox 값이 바뀔 때 호출되는 슬롯 함수
    def on_value_changed(self, value):
        # 최소/최대값 확인
        min_val = self.spinbox.minimum()
        max_val = self.spinbox.maximum()

        if value < min_val or value > max_val:
            # 범위를 벗어난 경우 경고 메시지 출력
            self.label.setText("선택한 값이 허용 범위를 벗어났습니다.")
        else:
            # 천 단위 쉼표가 포함된 문자열로 변환 (예: 1,000)
            formatted = f"{value:,}"
            # 라벨에 포맷팅된 텍스트 표시
            self.label.setText(f"선택한 값: {self.spinbox.prefix()}{formatted}{self.spinbox.suffix()}")

# 프로그램 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)   # QApplication 생성
    main_window = MW()             # 메인 윈도우 인스턴스 생성
    main_window.show()             # 윈도우 화면에 표시
    sys.exit(app.exec())           # 이벤트 루프 실행
