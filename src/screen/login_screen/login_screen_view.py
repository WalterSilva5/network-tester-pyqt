from PyQt5.QtWidgets import (
    QPushButton, QFrame, QLabel,
    QLineEdit, QGridLayout
)

from PyQt5.QtCore import QRect, QSize

class UiLoginScreen(object):
    def __init__(self, parent):
        self.parent = parent
        self.generate_frame()
        self.login_message_label = QLabel(self.frame)
        self.login_message_label.setText("Olá Mundo!")
        self.login_button = QPushButton(parent=self.frame, text="Confirmar")
        self.username_input = QLineEdit(parent=self.frame)

        grid_layout = QGridLayout(self.frame)
        grid_layout.addWidget(self.login_message_label, 0, 0)  
        grid_layout.addWidget(self.username_input, 1, 0)
        grid_layout.addWidget(self.login_button, 2, 0)


    def generate_frame(self):
        self.frame = QFrame(self.parent)
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setMinimumSize(QSize(800, 600))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setStyleSheet("padding: 0 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")