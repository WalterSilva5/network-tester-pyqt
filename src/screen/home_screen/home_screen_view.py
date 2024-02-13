from PyQt5.QtWidgets import (QFrame, QLabel,QGridLayout
)

from PyQt5.QtCore import QRect, QSize

class UiHomeScreen(object):
    def __init__(self, parent):
        self.parent = parent
        self.generate_frame()
        self.home_message_label = QLabel(self.frame)
        self.home_message_label.setText("HOME PAGE")

        grid_layout = QGridLayout(self.frame)
        grid_layout.addWidget(self.home_message_label, 0, 0)  



    def generate_frame(self):
        self.frame = QFrame(self.parent)
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QSize(800, 600))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setStyleSheet("padding: 0 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")