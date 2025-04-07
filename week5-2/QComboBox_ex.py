import sys

qt_modules = None # 일반적임

try:
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, )
    from PySide6.QtWidgets import Qt
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, )
        from PyQt6.QtCore import Qt
        qt_modules = 'PyQt6'
    except ImportError:
        print("There is no Qt Binding for Python.")
        sys.exit(1)

print(f"Using {qt_modules} binding.")
# logging으로도 log를 남길 수 있음.
# print부분이 logging.error or logging.info 등으로 대체 가능

# =================================================

class MW (QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QCombobox")
        self.resize(400,200)
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()
        lm.addWidget(QLabel('What is most important?'))
        
        # combobox's item list
        self.items = ['faith', 'hope', 'love']
        
        # self.cb = QComboBox() # 이후 제어를 위해선 self.cb가 더 나음
        cb = QComboBox()

        for idx, c in enumerate(self.items): #(이 부분은 items로도 가능함)
            # enumerate를 넣었기에 "currentIndexChanged" occured 1 or 0 or 2로 출력됨.
            cb.addItem(c)

        cb.activated.connect(self.on_selected)
        cb.currentIndexChanged.connect(self.on_current_idx_changed)
        lm.addWidget(cb)
        
        self.dp_label = QLabel("") # dp_label은 display관련임. dp가 diaply의 약어.
        lm.addWidget(self.dp_label)
        
        self.setLayout(lm)

    def on_selected(self, idx):
        # 유저가 선택항목을 선택한 경우에 호출되는 slot임
        # tmp = "you selected :"
        # tmp += self.items[idx] # items로 관리하는 이유가 index 관리가 편하기 때문
        tmp = f"you selected {self.items[idx]}"
        
        print(tmp) # print로 log를 남김
        self.dp_label.setText(tmp)

    def on_current_idx_changed(self, idx): # str로 넘어옴
        # 유저가 선택항목을 변경한 경우에 호출되는 slot임
        print(f'"currentIndexChanged" occured {idx}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
