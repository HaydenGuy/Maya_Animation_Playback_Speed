import sys
from maya import cmds

sys.path.append("/home/hayden/Documents/Maya/Animation_Playback_Speed")

from PySide6.QtWidgets import QMainWindow, QApplication
import UI.animation_playback_speed as aps

class Animation_Playback_Speed(QMainWindow, aps.Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_1x.clicked.connect(self.button_changed)
        self.button_05x.clicked.connect(self.button_changed)
        self.button_025x.clicked.connect(self.button_changed)
        self.button_2x.clicked.connect(self.button_changed)


    def button_changed(self):
        if self.button_1x.isChecked():
            cmds.polySphere()

        elif self.button_05x.isChecked():
            cmds.polyCube()
        
        elif self.button_025x.isChecked():
            cmds.polyCylinder()
        
        elif self.button_2x.isChecked():
            cmds.polyCone()

if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    # Create and show the UI window
    window = Animation_Playback_Speed()    
    window.show()