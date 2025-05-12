import sys, os
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow,QStatusBar,QLabel,
    QProgressBar,QPushButton,
)
from PySide6.QtCore import QTimer

# =================================================================================

class MW(QMainWindow):  # QMainWindow 기반의 메인 윈도우 클래스 정의

    def __init__(self):
        super(MW, self).__init__()  # 부모 클래스 생성자 호출

        # 상태바 객체를 생성 (QMainWindow의 내장 메서드 이용)
        self.status_bar = self.statusBar()
        # self.setStatusBar(self.status_bar)  # 생략 가능. 이미 기본으로 설정됨.

        # -------------------- 시계 표시 설정 --------------------
        # 타이머 생성: 1초마다 현재 시간을 상태바에 표시
        self.timer0 = QTimer(self)
        self.timer0.timeout.connect(self.update_clk)
        self.timer0.start(1000)  # 1000ms = 1초 주기

        # 상태바의 우측 고정 영역에 시간 라벨 추가 (영구 위젯)
        self.clk_label = QLabel()
        self.status_bar.addPermanentWidget(self.clk_label)

        # -------------------- 진행률 표시 설정 --------------------
        # 상태바에 표시될 프로그레스 바 (임시 위젯)
        self.progress_bar = QProgressBar(self, minimum=0, maximum=100)

        # 상태바에 위젯을 추가할 때 두 번째 인자는 "stretch factor"를 의미
        # 이 값이 클수록 해당 위젯이 더 많은 가로 공간을 차지하게 됨
        # 여기서 1은 가변 크기를 허용함을 의미하며, 다른 위젯과 공간을 유동적으로 나눔
        self.status_bar.addWidget(self.progress_bar, 1)  # 가변 폭 설정

        # -------------------- 중앙 버튼 --------------------
        # 중앙에 위치할 버튼 생성 및 클릭 이벤트 연결
        self.btn = QPushButton('Start Progress!')
        self.btn.clicked.connect(self.start_progress)
        self.setCentralWidget(self.btn)  # QMainWindow의 중앙 위젯 설정

        # -------------------- 프로그레스 타이머 --------------------
        # 100ms 간격으로 프로그레스 바 업데이트
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_progress)
        self.progress_value = 0  # 현재 진행률 초기값

        self.show()  # 윈도우 표시

    def start_progress(self):
        # 버튼 클릭 시 프로그레스바 초기화 및 진행 시작
        self.progress_value = 0
        self.progress_bar.reset()
        self.progress_bar.setValue(self.progress_value)
        self.timer1.start(100)  # 0.1초 간격으로 update_progress 호출
        self.status_bar.showMessage('Progress started...', 2000)  # 2초간 메시지 표시

    def update_clk(self):
        # 현재 시간 문자열을 상태바의 영구 위젯에 표시
        now = datetime.now()
        now_str = now.strftime('%H:%M:%S')  # '시:분:초' 형식 문자열
        self.clk_label.setText(now_str)

    def update_progress(self):
        # 타이머에 의해 호출되며 프로그레스 값을 증가시킴
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer1.stop()  # 100에 도달 시 타이머 정지
            self.status_bar.showMessage('Progress completed...', 2000)  # 완료 메시지

# -------------------- 앱 실행 --------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 인스턴스 생성
    wnd = MW()  # 메인 윈도우 생성 및 표시
    sys.exit(app.exec())  # 이벤트 루프 실행 및 정상 종료 처리