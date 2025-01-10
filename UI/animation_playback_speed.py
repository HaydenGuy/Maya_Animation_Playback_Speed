# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation_playback_speed.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_animation_playback_speed(object):
    def setupUi(self, animation_playback_speed):
        if not animation_playback_speed.objectName():
            animation_playback_speed.setObjectName(u"animation_playback_speed")
        animation_playback_speed.resize(800, 600)
        self.centralwidget = QWidget(animation_playback_speed)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout.addWidget(self.radioButton_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        animation_playback_speed.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(animation_playback_speed)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        animation_playback_speed.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(animation_playback_speed)
        self.statusbar.setObjectName(u"statusbar")
        animation_playback_speed.setStatusBar(self.statusbar)

        self.retranslateUi(animation_playback_speed)

        QMetaObject.connectSlotsByName(animation_playback_speed)
    # setupUi

    def retranslateUi(self, animation_playback_speed):
        animation_playback_speed.setWindowTitle(QCoreApplication.translate("animation_playback_speed", u"MainWindow", None))
        self.radioButton_2.setText(QCoreApplication.translate("animation_playback_speed", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("animation_playback_speed", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("animation_playback_speed", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("animation_playback_speed", u"RadioButton", None))
    # retranslateUi

