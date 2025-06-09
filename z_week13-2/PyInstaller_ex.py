# PySide6의 GUI 구성 요소들 import
from PySide6.QtWidgets import (
    QMainWindow,       # 메인 윈도우(타이틀바 포함 창 프레임)
    QApplication,      # 애플리케이션 객체 (이벤트 루프 관리)
    QWidget,           # 중앙 위젯 (다른 위젯을 담을 수 있음)
    QLabel,            # 텍스트 또는 이미지를 표시하는 라벨
    QPushButton,       # 클릭 가능한 버튼
    QVBoxLayout,       # 수직 레이아웃 관리자
)

# 아이콘(이미지)을 위한 클래스
from PySide6.QtGui import QIcon

# 정렬 등 다양한 상수들
from PySide6.QtCore import Qt

# 표준 파이썬 모듈
import sys  # 시스템 인자 및 종료 코드 등 관리
import os   # 파일 및 디렉토리 경로 처리용

# ===================================================================

# 메인 윈도우 클래스 정의 (QMainWindow를 상속받음)
class MW(QMainWindow):
    
    def __init__(self, base_dir):
        super().__init__()
        self.base_dir = base_dir  # 리소스 이미지 등의 기준 경로
        self.init_ui()            # 사용자 인터페이스 초기화
        
    def init_ui(self):
        self.setWindowTitle("Test PyInstaller")  # 창의 제목 설정
        
        # 수직 레이아웃 생성
        lm = QVBoxLayout()
        
        # 라벨 생성 및 가운데 정렬
        l = QLabel("PyInstaller Test App.")
        l.setAlignment(Qt.AlignCenter)
        lm.addWidget(l)  # 레이아웃에 라벨 추가
        
        # 닫기 버튼 생성
        btn_close = QPushButton("close")
        # 버튼에 아이콘 설정 (리소스 경로는 base_dir를 기준으로)
        btn_close.setIcon(QIcon(os.path.join(self.base_dir, "resources/rocket.png")))
        # 클릭 시 현재 윈도우 닫기
        btn_close.clicked.connect(self.close)
        lm.addWidget(btn_close)  # 레이아웃에 버튼 추가
        
        # 최소화 버튼 생성
        btn_min = QPushButton("minimize")
        btn_min.setIcon(QIcon(os.path.join(self.base_dir, "resources/star.png")))
        # 클릭 시 현재 윈도우 최소화
        btn_min.clicked.connect(self.lower)
        lm.addWidget(btn_min)
        
        # QWidget을 레이아웃 컨테이너로 설정
        container = QWidget()
        container.setLayout(lm)
        
        # 메인 윈도우의 중앙 위젯으로 설정
        self.setCentralWidget(container)
        
        # 윈도우 보여주기
        self.show()

# =================================================

# 프로그램 진입점
if __name__ == "__main__":
    # QApplication 객체 생성 (PyQt나 PySide에서는 반드시 하나만 존재해야 함)
    app = QApplication(sys.argv)
    
    # base_dir: 리소스(이미지 등) 파일의 기준 경로 설정
    # PyInstaller로 실행될 경우 임시 디렉토리(sys._MEIPASS)를 사용해야 함
    base_dir = ""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller가 실행 시 압축 해제한 리소스의 임시 디렉토리
        base_dir = sys._MEIPASS
    else:
        # 일반적인 실행 환경 (IDE 또는 파이썬 인터프리터)
        base_dir = os.path.dirname(__file__)
    
    # 메인 윈도우 인스턴스 생성
    wnd = MW(base_dir)
    
    # 앱 실행 (이벤트 루프 진입)
    sys.exit(app.exec())