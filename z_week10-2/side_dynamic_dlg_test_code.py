import os, sys
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MW(QDialog):  # QMainWindow 대신 QDialog 사용
    def __init__(self, ui_fstr):
        super().__init__()
        self.cnt = 0
        
        self.wnd = self.jy_get_wnd_from_ui(ui_fstr)
        self.jy_setup()
        
        # QDialog의 레이아웃에 wnd의 위젯을 추가
        self.setLayout(self.wnd.layout())
        self.setWindowTitle("Dialog")
        self.resize(320, 240)  # 창 크기 설정
        self.show()
        
    def jy_get_wnd_from_ui(self, ui_fstr):
        ui_loader = QUiLoader()
        
        root_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(root_dir, ui_fstr)
        print(f"UI 파일 경로: {ui_path}")
        
        ui_file_handler = QFile(ui_path)
        if not ui_file_handler.exists():
            print(f"에러: {ui_path} 존재하지 않습니다.")
            raise FileNotFoundError(f"{ui_path} 존재하지 않습니다.")
            
        if not ui_file_handler.open(QFile.ReadOnly):
            print(f"에러: {ui_path} 가 열리지 않음.")
            raise IOError(f"{ui_path} 가 열리지 않음.")
            
        try:
            wnd = ui_loader.load(ui_file_handler, self)
            if wnd is None:
                print(f"에러: {ui_path} 가 로딩되지 않음.")
                raise RuntimeError(f"{ui_path} 가 로딩되지 않음.")
            print("UI 파일 로드 성공")
            return wnd
        finally:
            ui_file_handler.close()
            
    def jy_setup(self):
        self.pushButton = self.wnd.findChild(QPushButton, "pushButton")
        self.label = self.wnd.findChild(QLabel, "label")
        
        print(f"pushButton: {self.pushButton}")
        print(f"label: {self.label}")
        
        missing_widgets = []
        if not self.pushButton:
            missing_widgets.append('pushButton')
        if not self.label:
            missing_widgets.append("label")
            
        if missing_widgets:
            print(f"에러: UI에서 다음 위젯을 찾을 수 없습니다: {missing_widgets}")
            raise AttributeError(f"UI에 다음의 widgets을 읽어들일 수 없습니다: {missing_widgets}")
        
        self.pushButton.clicked.connect(self.clk_slot)
        
    def clk_slot(self):
        self.cnt += 1
        self.label.setText(f"{self.cnt} clicked!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW("simple_dlg.ui")
    sys.exit(app.exec())
