from PySide6.QtWidgets import QApplication, QTreeView
from PySide6.QtGui import QIcon
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileSystemModel
import sys

app = QApplication(sys.argv)

view = QTreeView()
model = QFileSystemModel()
model.setRootPath(QDir.homePath())  # 홈 디렉토리 기준으로 설정
view.setModel(model)
view.setRootIndex(model.index(QDir.homePath()))

view.setWindowTitle("QFileSystemModel 예제")
view.resize(800, 600)
view.show()

sys.exit(app.exec())
