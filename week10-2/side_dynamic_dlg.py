import os, sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLabel,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# ========================================================

class MW (QMainWindow):
    def __init__(self, ui_fstr):
        super().__init__()
        self.cnt = 0
        
        self.wnd = self.jy_get_wnd_from_ui(ui_fstr) # wnd가 pyside 객체임
        self.jy_setup()
        self.setCentralWidget(self.wnd)
        self.show()
        
    def jy_get_wnd_from_ui(self, ui_fstr):
        ui_loader = QUiLoader()
        
        root_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = root_dir +"/"+ ui_fstr
        
        ui_file_handler = QFile(ui_path) # 파일 검사하는 라인
        if not ui_file_handler.exists():
            raise FileNotFoundError(
                f"{ui_path} 존재하지 않습니다."
            )
            
        if not ui_file_handler.open(QFile.ReadOnly):
            raise IOError(
                f"{ui_path} 가 열리지 않음."
            )
            
        try:
            wnd = ui_loader.load(
                ui_file_handler,
                self,
                )
            if wnd is None:
                raise RuntimeError(
                    f"{ui_path} 가 로딩되지 않음."
                )
            return wnd
        finally:
            ui_file_handler.close()
            
    def jy_setup(self):
        self.pushButton = self.wnd.findChild(
            QPushButton,
            "pushButton",
        )
        self.label = self.wnd.findChild(
            QLabel,
            "label",
        )
        
        # widget이 제대로 로딩되었는지 확인.
        missing_widgets = []
        if not self.pushButton:
            missing_widgets.append('pushButton!')
        if not self.label:
            missing_widgets.append("label")
            
        if missing_widgets:
            raise AttributeError(
                f"UI에 다음의 widgets을 읽어들일 수 없습니다."
            )
        
        # 버튼 클릭 시그널 연결
        self.pushButton.clicked.connect(self.clk_slot)
        
    def clk_slot(self):
        self.cnt += 1
        self.label.setText(f"{self.cnt} clicked!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)                
    window = MW ("simple_dlg.ui")
    sys.exit(app.exec())
    
    
    