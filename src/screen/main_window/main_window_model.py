from PyQt5.QtCore import QObject

class MainWindowModel(QObject): 
    current_user_name = ""
    
    @property 
    def current_user_name(self):
        return self.current_user_name
    
    @current_user_name.setter
    def current_user_name(self, name):
        self.current_user_name = name