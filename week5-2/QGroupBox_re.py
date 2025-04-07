import sys
from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QGroupBox
from PySide6.QtCore import Qt

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 200)  # 창의 최소 크기 설정
        self.setWindowTitle("QGroupBox Ex")  # 창의 제목 설정
        self.setup_ui()  # UI 설정
        self.show()  # 창을 표시

    def setup_ui(self):
        """
        UI의 레이아웃을 설정하는 함수
        QGroupBox와 버튼들을 설정하고, 레이아웃을 화면에 배치한다.
        """
        main_layout = QHBoxLayout()  # 수평 레이아웃 생성
        
        # QCheckBox와 QRadioButton 그룹을 각각 생성하여 설정
        self.checks_group = self.create_group_box("QCheckBox Grp", self.setup_checkboxes)
        self.radios_group = self.create_group_box("QRadioButton Grp", self.setup_radios)

        # 그룹 박스를 수평 레이아웃에 추가
        main_layout.addWidget(self.checks_group)
        main_layout.addWidget(self.radios_group)

        self.setLayout(main_layout)  # 레이아웃을 메인 창에 적용

    def create_group_box(self, title, setup_method):
        """
        QGroupBox를 생성하고, 해당 그룹 박스를 설정하는 메서드를 호출
        title: 그룹 박스의 제목
        setup_method: 그룹 박스를 설정하는 함수 (체크박스나 라디오버튼 설정)
        """
        group_box = QGroupBox(title)  # 그룹 박스를 생성
        group_box.setCheckable(True)  # 그룹 박스를 체크 가능하게 설정
        group_box.setChecked(False)  # 초기 상태는 체크 해제
        setup_method(group_box)  # 그룹 박스를 설정하는 메서드를 호출
        return group_box  # 설정된 그룹 박스를 반환

    def setup_checkboxes(self, group_box):
        """
        QCheckBox들을 설정하고 그룹 박스에 배치하는 함수
        group_box: QGroupBox 객체
        """
        layout = QVBoxLayout()  # 수직 레이아웃 생성
        self.checkbox_group = QButtonGroup()  # 체크박스를 그룹화할 버튼 그룹 생성
        
        # 3개의 체크박스를 생성하고 레이아웃에 추가
        for idx in range(3):
            checkbox = QCheckBox(f"check {idx}")
            self.checkbox_group.addButton(checkbox)  # 버튼 그룹에 추가
            layout.addWidget(checkbox)  # 레이아웃에 체크박스 추가

        group_box.setLayout(layout)  # 그룹 박스에 레이아웃 설정
        self.checkbox_group.setExclusive(False)  # 여러 개의 체크박스를 동시에 선택할 수 있게 설정
        self.checkbox_group.buttonClicked.connect(self.toggle_checkboxes)  # 버튼 클릭 시 처리할 함수 연결
        group_box.clicked.connect(self.clk_checks)  # 그룹 박스 클릭 시 처리할 함수 연결

    def setup_radios(self, group_box):
        """
        QRadioButton들을 설정하고 그룹 박스에 배치하는 함수
        group_box: QGroupBox 객체
        """
        layout = QVBoxLayout()  # 수직 레이아웃 생성
        self.radio_group = QButtonGroup()  # 라디오 버튼을 그룹화할 버튼 그룹 생성

        # 3개의 라디오 버튼을 생성하고 레이아웃에 추가
        for idx in range(3):
            radio_button = QRadioButton(f"radio {idx}")
            self.radio_group.addButton(radio_button)  # 버튼 그룹에 추가
            layout.addWidget(radio_button)  # 레이아웃에 라디오 버튼 추가

        group_box.setLayout(layout)  # 그룹 박스에 레이아웃 설정
        self.radio_group.setExclusive(False)  # 여러 개의 라디오 버튼을 동시에 선택할 수 있게 설정
        self.radio_group.buttonClicked.connect(self.toggle_radios)  # 버튼 클릭 시 처리할 함수 연결
        group_box.clicked.connect(self.clk_radios)  # 그룹 박스 클릭 시 처리할 함수 연결

    def toggle_checkboxes(self, state):
        """
        체크박스 상태가 변경될 때 호출되는 함수
        선택된 체크박스의 텍스트를 출력
        state: 체크박스의 상태 (사용하지 않지만, 시그널로 전달됨)
        """
        print("\n======================")
        for checkbox in self.checkbox_group.buttons():
            if checkbox.isChecked():  # 체크박스가 선택된 경우
                print(checkbox.text())  # 선택된 체크박스의 텍스트 출력
        print("======================\n")

    def toggle_radios(self, state):
        """
        라디오 버튼 상태가 변경될 때 호출되는 함수
        선택된 라디오 버튼의 인덱스와 텍스트를 출력
        state: 라디오 버튼의 상태 (사용하지 않지만, 시그널로 전달됨)
        """
        print("\n======================")
        for idx, radio_button in enumerate(self.radio_group.buttons()):
            if radio_button.isChecked():  # 라디오 버튼이 선택된 경우
                print(f"{idx} {radio_button.text()}")  # 선택된 라디오 버튼의 인덱스와 텍스트 출력
        print("======================\n")

    def clk_checks(self, checked):
        """
        체크박스가 클릭될 때 호출되는 함수
        checked: 체크박스가 체크되었는지 여부
        """
        print("checks!")
        print(checked)

    def clk_radios(self, button):
        """
        라디오 버튼이 클릭될 때 호출되는 함수
        button: 클릭된 라디오 버튼
        """
        print("radios!")
        print(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()  # 윈도우 객체 생성
    sys.exit(app.exec())  # 애플리케이션 실행
