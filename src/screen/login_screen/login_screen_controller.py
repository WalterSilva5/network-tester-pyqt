from PyQt5.QtWidgets import QWidget
from src.screen.login_screen.login_screen_view import UiLoginScreen

class LoginScreenController(QWidget):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model
        self.parent = parent
        self.view = UiLoginScreen(self)
        self.setup_ui()

    def exec_login(self):
        self.parent.change_screen(self.parent.home_screen)
        print("current_window")
    
    def setup_ui(self):
        self.view.login_button.clicked.connect(self.exec_login)
