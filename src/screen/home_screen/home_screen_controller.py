from PyQt5.QtWidgets import QWidget
from src.screen.home_screen.home_screen_view import UiHomeScreen

class HomeScreenController(QWidget):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model
        self.parent = parent
        self.view = UiHomeScreen(self)
        self.setup_ui()
    
    def setup_ui(self):
        pass