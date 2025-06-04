# PySide6의 GUI 구성 요소 중 QTreeView와 QApplication을 import
from PySide6.QtWidgets import QApplication, QTreeView

# QDir은 디렉토리 경로 관련 기능, QFileInfo는 파일 정보 추출을 위한 클래스
from PySide6.QtCore import QDir, QFileInfo

# 파일 시스템 모델 클래스를 import (모델-뷰 구조에서 모델 역할)
from PySide6.QtWidgets import QFileSystemModel

# 시스템 인자를 가져오기 위한 모듈 (e.g., QApplication에 전달할 인자용)
import sys

# QApplication 인스턴스 생성
# Qt 어플리케이션의 실행 환경을 구성하는 객체로, 이벤트 루프와 GUI 자원 관리 등의 역할
app = QApplication(sys.argv)

# QTreeView 인스턴스 생성
# 트리 형태로 디렉토리 및 파일 구조를 보여주는 뷰 컴포넌트
tree = QTreeView()

# QFileSystemModel 인스턴스 생성
# 파일 시스템의 디렉토리 및 파일 정보를 제공하는 모델
model = QFileSystemModel()

# 모델의 루트 경로를 시스템 사용자 홈 디렉토리로 설정
# 해당 경로를 기준으로 하위 디렉토리/파일을 로딩함
model.setRootPath(QDir.homePath())

# 모델에 표시할 항목을 필터링: 디렉토리, 파일 포함 / .(현재 디렉토리), ..(상위 디렉토리)는 제외
model.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)

# 생성한 파일 시스템 모델을 QTreeView에 연결
tree.setModel(model)

# QTreeView의 루트 인덱스를 사용자의 홈 디렉토리로 설정
# 이것은 사용자가 처음 볼 수 있는 디렉토리의 위치를 지정하는 것
tree.setRootIndex(model.index(QDir.homePath()))

# 항목이 클릭될 때 호출될 콜백 함수 정의
def on_click(index):
    # 클릭된 항목의 파일 또는 디렉토리 이름 출력
    print("파일 이름:", model.fileName(index))

    # 클릭된 항목의 전체 경로 출력
    print("전체 경로:", model.filePath(index))

    # 해당 항목이 디렉토리인지 여부 출력 (True / False)
    print("디렉토리 여부:", model.isDir(index))

    # QFileInfo 객체를 사용해 해당 항목의 상세 정보 추출
    info: QFileInfo = model.fileInfo(index)

    # 항목의 파일 크기 출력 (바이트 단위)
    print("크기:", info.size())

    # 마지막으로 수정된 날짜와 시간을 문자열로 변환하여 출력
    print("수정일:", info.lastModified().toString())

    # 클릭한 항목의 각 열(이름, 크기, 타입, 수정일 등)에 대해 데이터 출력
    for col in range(model.columnCount(index)):
        # index.row(): 클릭된 행 번호
        # col: 열 번호
        # index.parent(): 부모 인덱스를 기준으로 자식 인덱스를 얻기 위해 필요
        print(f"열 {col}: {model.data(model.index(index.row(), col, index.parent()))}")

# QTreeView에서 항목을 클릭했을 때 on_click 함수가 호출되도록 시그널 연결
tree.clicked.connect(on_click)

# QTreeView 윈도우의 제목 설정
tree.setWindowTitle("QFileSystemModel 전체 예제")

# 윈도우 크기 설정
tree.resize(800, 600)

# 트리 뷰 표시
tree.show()

# 이벤트 루프 실행 (프로그램이 종료될 때까지 GUI 응답을 유지)
sys.exit(app.exec())