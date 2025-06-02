import sys
from PySide6.QtWidgets import (
    QApplication, 
    QTreeView, 
    QVBoxLayout, QWidget, QMainWindow,
    )

from PySide6.QtGui import (
    QStandardItemModel, 
    QStandardItem,
)

# =========================================================

# 메인 위젯 클래스 정의
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 창 제목 및 크기 설정
        self.setWindowTitle("Deep Learning Algorithms")
        self.setGeometry(100, 100, 600, 500)
        self.set_main_wnd()
        self.show()

    def set_main_wnd(self):
        # 수직 레이아웃 생성
        layout = QVBoxLayout()

        # QTreeView 위젯 생성: 트리 형태로 데이터를 보여주는 뷰
        self.tree_view = QTreeView()
        self.tree_view.setAlternatingRowColors(True)  # 줄마다 배경색 교차
        self.tree_view.setAnimated(True)              # 트리 확장/축소 시 애니메이션 적용
        self.tree_view.setSortingEnabled(False)       # 정렬 기능 비활성화

        # 데이터 모델 생성: 계층적 데이터를 담는 모델
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["분류", "설명"])  # 헤더 라벨 지정

        # 트리 데이터 구성 및 model에 추가.
        root,root_info = self.populate_tree()

        # 최상위 루트 아이템을 모델에 등록
        self.model.appendRow([root,root_info])

        # 모델과 뷰 연결
        self.tree_view.setModel(self.model)

        # 모든 항목 기본적으로 확장
        self.tree_view.expandAll()
        self.tree_view.setColumnWidth(0, 250)
        self.tree_view.setColumnWidth(1, 500)

        # 레이아웃에 트리 뷰 추가하고 위젯에 설정
        layout.addWidget(self.tree_view)

        # dummy container
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # QStandardItem 생성 도우미 메서드
    def create_item(self, text, editable=False):
        item = QStandardItem(text)
        item.setEditable(editable)  # 편집 가능 여부 설정
        return item

    # root, root_info에 트리 구조를 구성하는 메서드
    # 핵심 내용임 !!!!!!!!!!!!!!!! 아래 population_tree가 
    def populate_tree(self):
        """딥러닝 알고리즘 분류 트리 생성"""

        # 1. 최상위 루트 노드 (사용자에겐 보이는 루트)
        root = self.create_item("딥러닝")
        root_info = self.create_item("Deep Learning Algorithms")

        self.model.appendRow([root, root_info])

        # 1-1. 지도 학습 ─────────
        supervised = self.create_item("Supervised Learning")
        supervised_info = self.create_item("Labeled data 기반 학습")

        # 1-1. 루트 노드에 지도학습 추가
        root.appendRow([supervised, supervised_info])

        # 지도 학습 하위 알고리즘 추가.

        # 1-1-1. FCN 
        supervised.appendRow([
            self.create_item("FCN"),
            self.create_item("Fully Connected Network, MLP"),
            ])
        # 1-1-2. CNN
        supervised.appendRow([
            self.create_item("CNN"),
            self.create_item("이미지 처리에 특화된 구조"),
            ])
        # 1-1-3. RNN 및 하위 구조
        rnn = self.create_item("순환 신경망 (RNN)")
        rnn_info = self.create_item("시계열 데이터 처리")
        # 1-1-3-1. LSTM
        rnn.appendRow([
            self.create_item("LSTM"),
            self.create_item("Long Short-Term Memory"),
            ])
        # 1-1-3-2. GRU
        rnn.appendRow([
            self.create_item("GRU"),
            self.create_item("Gated Recurrent Unit"),
            ])
        supervised.appendRow([rnn, rnn_info])

        # 1-1-4. Transformer 및 하위 구조
        transformer = self.create_item("트랜스포머 (Transformer)")
        transformer_info = self.create_item("Self-Attention 기반 시퀀스 처리")

        # 1-1-4-1. BERT
        transformer.appendRow([
            self.create_item("BERT"),
            self.create_item("Bidirectional Encoder Representations")
        ])
        # 1-1-4-2. GPT
        transformer.appendRow([
            self.create_item("GPT"),
            self.create_item("Generative Pretrained Transformer")
        ])
        # 1-1-4-3. ViT
        transformer.appendRow([
            self.create_item("ViT"),
            self.create_item("Vision Transformer for Images")
        ])
        supervised.appendRow([transformer, transformer_info])

        # 2. 비지도 학습 
        unsupervised = self.create_item("Unsupervised Learning")
        unsupervised_info = self.create_item("레이블 없는 데이터")
        root.appendRow([unsupervised, unsupervised_info])

        # 2-1. AutoEncoder
        unsupervised.appendRow([
            self.create_item("AutoEncoder"),
            self.create_item("특징 추출 및 차원 축소"),
            ])
        # 2-2. GAN
        unsupervised.appendRow([
            self.create_item("생성적 적대 신경망 (GAN)"),
            self.create_item("Generative Adversarial Network"),
            ])

        # 3. 강화학습 (최상위 분류로) 
        reinforcement = self.create_item("강화학습")
        reinforcement_info = self.create_item("보상 기반 학습")
        root.appendRow([reinforcement, reinforcement_info])

        # 3-1. 값 기반 방법
        value_based = self.create_item("값 기반 방법 (Value-based)")
        value_based_info = self.create_item("Q 값을 추정하여 정책 도출")
        reinforcement.appendRow([value_based, value_based_info])

        # 3-1-1. DQN
        value_based.appendRow([
            self.create_item("DQN"),
            self.create_item("Deep Q-Network"),
            ])

        # 3-2.정책 기반 방법
        policy_based = self.create_item("정책 기반 방법 (Policy-based)")
        policy_based_info = self.create_item("정책 함수 직접 학습")
        reinforcement.appendRow([policy_based, policy_based_info])
        # 3-2-1. REINFORCE
        policy_based.appendRow([
            self.create_item("REINFORCE"),
            self.create_item("기초 정책 경사법"),
            ])

        # 3-3. 액터-크리틱 방법
        actor_critic = self.create_item("액터-크리틱 방법 (Actor-Critic)")
        actor_critic_info = self.create_item("정책과 가치 동시 학습")
        reinforcement.appendRow([actor_critic, actor_critic_info])

        # 3-3-1. A2C
        actor_critic.appendRow([
            self.create_item("A2C"),
            self.create_item("Advantage Actor-Critic"),
            ])
        # 3-3-2. PPO
        actor_critic.appendRow([
            self.create_item("PPO"),
            self.create_item("Proximal Policy Optimization"),
            ])

        return root,root_info

# ==================================================

# 프로그램 실행 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    wnd = MW()                    # 메인 위젯 생성
    sys.exit(app.exec())          # 이벤트 루프 실행 및 정상 종료 처리