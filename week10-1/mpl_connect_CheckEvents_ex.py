import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# MainWindow 클래스는 PySide6의 QMainWindow를 상속받아 사용자 정의 윈도우를 생성.
class MainWindow(QMainWindow):
    def __init__(self):
        # 부모 클래스의 생성자 호출
        super().__init__()  
        # 윈도우 제목 설정
        self.setWindowTitle("Event Handling with Matplotlib and PySide6")  

        # Matplotlib Figure 객체 생성. 이 객체는 플롯의 컨테이너 역할을 수행.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)  # Figure 객체를 화면에 표시할 Canvas 생성
        self.ax = self.figure.add_subplot(111)  # 1x1 그리드에 첫 번째 서브플롯 추가
        self.ax.plot([1, 2, 3, 4], [1, 4, 9, 16])  # 예제 데이터로 간단한 선 그래프plotting 

        # NavigationToolbar2QT는 Matplotlib의 도구 모음을 PySide6 애플리케이션에 통합
        self.toolbar = NavigationToolbar(self.canvas, self)  # Canvas와 MainWindow를 툴바에 연결

        # QVBoxLayout을 사용하여 위젯을 수직으로 정렬.
        layout = QVBoxLayout()
        widget = QWidget()  # 중앙 위젯으로 사용할 QWidget 인스턴스 생성
        self.setCentralWidget(widget)  # 생성한 위젯을 메인 윈도우의 중앙 위젯으로 설정
        widget.setLayout(layout)  # QVBoxLayout을 QWidget에 설정
        layout.addWidget(self.toolbar)  # 툴바를 레이아웃에 추가
        layout.addWidget(self.canvas)   # 캔버스를 레이아웃에 추가

        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()

        # 각종 이벤트에 대한 리스너(콜백 함수) 연결
        self.canvas.mpl_connect("button_press_event", self.on_press)
        self.canvas.mpl_connect("button_release_event", self.on_release)
        self.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        self.canvas.mpl_connect("key_release_event", self.on_key_release)

    # 마우스 버튼이 눌렸을 때 호출되는 메소드
    def on_press(self, event):
        print(f"Mouse button pressed at ({event.xdata:.2f}, {event.ydata:.2f})")
        print(f"Mouse button is ({event.button}, it is clicked with the pressed key {event.key})")
        print(f"Mouse button is double clicked: {event.dblclick}")
        print('--------------\n')

    # 마우스 버튼이 떼어졌을 때 호출되는 메소드
    def on_release(self, event):
        print("Mouse button released")
        print('--------------\n')

    # 마우스가 움직였을 때 호출되는 메소드
    def on_motion(self, event):
        if event.xdata is not None and event.ydata is not None:  # 마우스 위치가 유효한 경우
            print(f"Mouse moved to ({event.xdata:.2f}, {event.ydata:.2f})")
            print('--------------')

    # 키보드 키가 눌렸을 때 호출되는 메소드
    def on_key_press(self, event):
        print(f"Key pressed: {event.key}")
        print('--------------\n')

    # 키보드 키가 떼어졌을 때 호출되는 메소드
    def on_key_release(self, event):
        print("Key released")
        print('--------------\n')

# 애플리케이션 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 애플리케이션 인스턴스 생성
    main_window = MainWindow()    # MainWindow 인스턴스 생성
    main_window.show()            # 메인 윈도우 표시
    sys.exit(app.exec())          # 애플리케이션 이벤트 루프 시작
    
    
