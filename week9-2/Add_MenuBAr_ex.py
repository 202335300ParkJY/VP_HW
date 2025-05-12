import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

# ====================================================

class MW (QMainWindow):
  def __init__(self):
    super().__init__()
    self.init_ui()
  def init_ui(self):
    """ application의 gui를 초기화하는 메서드"""
    self.fstr = os.path.dirname(
      os.path.abspath(__file__)
    )
    self.setMinimumSize(600,600)
    self.setWindowTitle("Menu bar Ex")
    self.setup_main_wnd()    # main window를 설정하는 메서드 (풀소스코드 참고)
    self.create_actions()        # menu bar에서 수행될 command들에 해당하는 action생성.
    self.create_menu()          # menu bar 생성. 앞서 생성된 action들을 활용.
    self.show()

  def create_actions (self):
    self.quit_act = QAction("Quit")
    self.quit_act.setShortcut("Ctrl+X")
    self.quit_act.setIcon(QIcon(f"{self.fstr}/img/exit.png"))
    # self.quit_act.setIcon(QIcon("img/exit.png"),"Quit") #action의 icon과 이름을 한번에 지정.
    self.quit_act.triggered.connect(self.close)

  def create_menu(self):
    """어플리케이션의 menu bar를 만드는 method."""
    mb = self.menuBar()                         # main window의 menu bar를 추상화한 instance.
    menu_item = mb.addMenu("test")    # test 라는 이름의 menu item을 추가.
    menu_item.addAction(self.quit_act) # test 메뉴아이템에 아까 만든 QAction instance추가.
    mb.setNativeMenuBar(False) # for macOS

  def setup_main_wnd(self):
    label = QLabel('test')
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  wnd = MW()
  sys.exit(app.exec())
