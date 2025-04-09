import sys

# Qt 바인딩을 PySide6 우선 사용, PyQt6는 예비용으로 사용
qt_modules = None

# PySide6을 먼저 시도
try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QMainWindow,
        QWidget, QVBoxLayout, 
        QSlider,
    )
    from PySide6.QtCore import Qt
    qt_modules = 'PySide6'
except ImportError:
    # PySide6 import 실패 시, PyQt6을 시도
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget, QLabel,
            QWidget, QVBoxLayout, 
            QSlider,
        )
        from PyQt6.QtCore import Qt
        qt_modules = 'PyQt6'
    except ImportError:
        # 두 바인딩 모두 import에 실패한 경우 에러 메시지 출력 후 종료
        print("There is no Qt Binding for Python.")
        sys.exit(1)

# 사용 중인 Qt 바인딩 출력
print(f"Using {qt_modules} binding.")


# 메인 윈도우 클래스 정의
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # UI 초기화
        self.show()     # 윈도우 표시

    def init_ui(self):
        # 메인 윈도우의 제목과 초기 위치/크기 설정
        self.setWindowTitle("QSlider Ex.")
        self.setGeometry(100, 100, 300, 200)

        # 중앙 위젯 생성 및 초기 배경색 설정
        central_widget = QWidget()
        init_value = 125  # 초기 RGB 값
        central_widget.setStyleSheet(
            f"background-color: rgb({init_value}, {init_value}, {init_value});"
        )
        self.setCentralWidget(central_widget)

        # 수직 레이아웃 생성 후 중앙 위젯에 설정
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 수평 슬라이더 생성 및 설정
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)        # 최소값 설정
        slider.setMaximum(255)      # 최대값 설정
        slider.setValue(init_value) # 초기값 설정
        slider.setTickInterval(10)  # 눈금 간격 설정
        slider.setTickPosition(QSlider.TicksBelow)  # 눈금 위치 설정
        slider.setSingleStep(1)     # 키보드 화살표 조작 시 증가 단위
        slider.setPageStep(10)      # PageUp/PageDown 조작 시 증가 단위

        # 슬라이더 값 변경 시 배경색 업데이트 함수 연결
        slider.valueChanged.connect(self.on_change_bg_color)

        # 레이아웃에 슬라이더 추가
        layout.addWidget(slider)

    def on_change_bg_color(self, value):
        # 슬라이더 값에 따라 중앙 위젯 배경색 변경
        self.centralWidget().setStyleSheet(
            f"background-color: rgb({value}, {value}, {value});"
        )


# 메인 실행부
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 인스턴스 생성
    main_window = MW()            # 메인 윈도우 생성
    sys.exit(app.exec())          # 이벤트 루프 실행 및 종료 시 코드 반환
