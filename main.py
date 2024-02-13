from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow
from PyQt5.QtGui import QPalette, QColor
import sys
from src.screen.main_window.main_window import UiMainWindow
from src.screen.main_window.main_window_model import MainWindowModel

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Set the application style to Fusion
        self.setStyle(QStyleFactory.create('Fusion'))

        # Customize the palette for light mode
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        
        self.setPalette(palette)

        self.view = UiMainWindow(MainWindowModel())
        self.view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
