import sys
from maya import cmds

from PySide6.QtWidgets import QMainWindow, QApplication, QSlider, QLabel
from PySide6.QtCore import Qt

import Animation_Playback_Speed.UI.ui as ui

# Slider that uses float values rather than int
class FloatSlider(QSlider):
    def __init__(self, orientation=Qt.Vertical, parent=None):
        super().__init__(orientation, parent)
        self._scale = 100  # Default scaling factor for floats

    # Set the range using float
    def setFloatRange(self, min_value, max_value):
        self.setMinimum(int(min_value * self._scale))
        self.setMaximum(int(max_value * self._scale))

    # Set value using float
    def setFloatValue(self, value):
        self.setValue(int(value * self._scale))

    # Get current value as float
    def floatValue(self):
        return self.value() / self._scale

    # Set the step and tick size for the slider
    def setFloatStep(self, step):
        self.setSingleStep(int(step * self._scale))
        self.setTickInterval(int(step * self._scale))

class Animation_Playback_Speed(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ui.Ui_main_window()
        self.ui.setupUi(self)

        # Hide name from the title bar
        self.setWindowTitle("")

        self.add_slider()

        # When radio button clicked call button_changed method
        self.ui.button_1x.clicked.connect(self.button_changed)
        self.ui.button_05x.clicked.connect(self.button_changed)
        self.ui.button_025x.clicked.connect(self.button_changed)
        self.ui.button_2x.clicked.connect(self.button_changed)

        # When slider value changes call slider_changed method
        self.slider.valueChanged.connect(self.slider_changed)

    # Add the slider and its label to v_slider_layout
    def add_slider(self):
        # Initialize and add FloatSlider with values and steps
        self.slider = FloatSlider(Qt.Vertical)
        self.slider.setFloatRange(0.1, 5.0)
        self.slider.setFloatValue(1.0)
        self.slider.setFloatStep(0.1)
        self.ui.v_slider_layout.addWidget(self.slider, alignment=Qt.AlignHCenter)

        # Initalize and add slider label 
        self.slider_label = QLabel("1.0x")
        self.ui.v_slider_layout.addWidget(self.slider_label, alignment=Qt.AlignHCenter)

    # Updates the playback speed when a radio button is checked
    def button_changed(self):
        if self.ui.button_1x.isChecked():
            cmds.playbackOptions(playbackSpeed=1) # Sets playback speed to specific float value

        elif self.ui.button_05x.isChecked():
            cmds.playbackOptions(playbackSpeed=0.5)

        elif self.ui.button_025x.isChecked():
            cmds.playbackOptions(playbackSpeed=0.25)

        elif self.ui.button_2x.isChecked():
            cmds.playbackOptions(playbackSpeed=2)

    # Updates the playback speed and label when the slider value changes
    def slider_changed(self):
        value = self.slider.floatValue()
        self.slider_label.setText(f"{value:.1f}x") # :.1f = 1 decimal place (0.1)
        cmds.playbackOptions(playbackSpeed=value)

    # When QMainWindow closes set playback speed to 1
    def closeEvent(self, event):
        cmds.playbackOptions(playbackSpeed=1)
        event.accept()
        
if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    # Hides the application name from the title bar
    app.setApplicationDisplayName("")
    
    # Create and show the UI window
    window = Animation_Playback_Speed()    
    window.show()