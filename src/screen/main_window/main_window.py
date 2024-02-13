from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QStackedWidget

from src.screen.login_screen.login_screen_controller import LoginScreenController
from src.screen.login_screen.login_screen_model import LoginScreenModel
from src.screen.home_screen.home_screen_controller import HomeScreenController
from src.screen.home_screen.home_screen_model import HomeScreenModel
from src.screen.main_window.main_window_model import MainWindowModel

class UiMainWindow(QMainWindow):
    def __init__(self, window_model: MainWindowModel):
        super().__init__()
        self.model = window_model
        self.setGeometry(100, 100, 800, 600)
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)
        
        self.login_screen = LoginScreenController(self, LoginScreenModel())
        self.home_screen = HomeScreenController(self, HomeScreenModel())
        
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.home_screen)
        
        self.stack.setCurrentWidget(self.login_screen)
        
    def change_screen(self, screen):
        print("changing screen", screen)
        self.stack.setCurrentWidget(screen)