from PySide6.QtWidgets import QLabel, QApplication
import sys

app = QApplication(sys.argv)
widget = QLabel("tets!")
widget.resize(300,200) # 창의 크기 설정 (너비, 높이)
widget.show()
sys.exit(app.exec())
