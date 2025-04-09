import sys, os
qt_modules = None
try:
    from PySide6.QtWidgets import (QApplication, QWidget, QStackedLayout, QVBoxLayout, QLabel, QComboBox)
    from PySide6.QtGui import QPixmap
    qt_modules = 'PySide6'
except ImportError:
    try: 
        from PyQt6.QtWidgets import (QApplication, QWidget, QStackedLayout, QVBoxLayout, QLabel, QComboBox)
        from PyQt6.QtGui import QPixmap
        qt_modules = 'PyQt6'
    except ImportError:
        print("PYSide6 , PyQt6 X")
        sys.exit(1)
        
print(f"using {qt_modules} binding")

# ====================================================
class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 윈도우 타이틀 설정
        self.setWindowTitle("Ex Input Widgets")
        # 메인 위젯 및 레이아웃 구성
        self.setup_main_wnd()
        # 윈도우 표시
        self.show()

    def setup_main_wnd(self):
    # 현재 파일의 절대 경로 기준으로 dir path 얻기
        fpath = os.path.dirname(
            os.path.abspath(__file__)
        )
        
        # ComboBox 표시될 page names
        pages = ['faith', 'hope', 'love']
    
    # 각 페이지에 해당하는 이미지 파일 경로 리스트
        self.imgs = [
            os.path.join(fpath, 'img/faith.png'),
            os.path.join(fpath, 'img/hope.png'),
            os.path.join(fpath, 'img/love.png')
        ]
        
    # ComboBox 생성/ 항목 추가
    combo_box = QComboBox()
    combo_box.addItems(pages)
    # ComboBox 항목이 선택되면 change_page func. 실행
    combo_box.activated.connect(self.change_page)
    
    # StackedLayout 생성 (여러 page 겹쳐서 보관. 그중 하나만 표시)
    self.stacked_lm = QStackedLayout()
    
    # 페이지 수만큼 QLabel 생성 후, QStackedLayout 추가
    for idx, c in enumerate(pages):
        label = self.setup_page(idx) # QLabel 생성 후 이미지 설정
        self.stacked_lm.addWidget(label) # stack 추가
        
    