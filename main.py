import sys
from maya import cmds

sys.path.append("/home/hayden/Documents/Maya/Animation_Playback_Speed")

from PySide6.QtWidgets import QMainWindow, QApplication
import UI.animation_playback_speed as aps

class Animation_Playback_Speed(QMainWindow, aps.Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    # Create and show the UI window
    window = Animation_Playback_Speed()    
    window.show()