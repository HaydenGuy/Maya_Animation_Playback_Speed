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
    QRadioButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(94, 318)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_1x = QRadioButton(self.centralwidget)
        self.button_1x.setObjectName(u"button_1x")

        self.verticalLayout.addWidget(self.button_1x)

        self.button_05x = QRadioButton(self.centralwidget)
        self.button_05x.setObjectName(u"button_05x")

        self.verticalLayout.addWidget(self.button_05x)

        self.button_025x = QRadioButton(self.centralwidget)
        self.button_025x.setObjectName(u"button_025x")

        self.verticalLayout.addWidget(self.button_025x)

        self.button_2x = QRadioButton(self.centralwidget)
        self.button_2x.setObjectName(u"button_2x")

        self.verticalLayout.addWidget(self.button_2x)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.slider = QSlider(self.centralwidget)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.slider, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 94, 23))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Playback Speed", None))
        self.button_1x.setText(QCoreApplication.translate("main_window", u"1x", None))
        self.button_05x.setText(QCoreApplication.translate("main_window", u"0.5x", None))
        self.button_025x.setText(QCoreApplication.translate("main_window", u"0.25x", None))
        self.button_2x.setText(QCoreApplication.translate("main_window", u"2x", None))
    # retranslateUi

