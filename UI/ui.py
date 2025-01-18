# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(94, 321)
        main_window.setMinimumSize(QSize(94, 321))
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.v_layout = QVBoxLayout()
        self.v_layout.setObjectName(u"v_layout")
        self.v_button_layout = QVBoxLayout()
        self.v_button_layout.setObjectName(u"v_button_layout")
        self.button_1x = QRadioButton(self.centralwidget)
        self.button_1x.setObjectName(u"button_1x")

        self.v_button_layout.addWidget(self.button_1x)

        self.button_05x = QRadioButton(self.centralwidget)
        self.button_05x.setObjectName(u"button_05x")

        self.v_button_layout.addWidget(self.button_05x)

        self.button_025x = QRadioButton(self.centralwidget)
        self.button_025x.setObjectName(u"button_025x")

        self.v_button_layout.addWidget(self.button_025x)

        self.button_2x = QRadioButton(self.centralwidget)
        self.button_2x.setObjectName(u"button_2x")

        self.v_button_layout.addWidget(self.button_2x)


        self.v_layout.addLayout(self.v_button_layout)

        self.v_slider_layout = QVBoxLayout()
        self.v_slider_layout.setObjectName(u"v_slider_layout")

        self.v_layout.addLayout(self.v_slider_layout)


        self.horizontalLayout.addLayout(self.v_layout)

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
        main_window.setWindowTitle("")
        self.button_1x.setText(QCoreApplication.translate("main_window", u"1x", None))
        self.button_05x.setText(QCoreApplication.translate("main_window", u"0.5x", None))
        self.button_025x.setText(QCoreApplication.translate("main_window", u"0.25x", None))
        self.button_2x.setText(QCoreApplication.translate("main_window", u"2x", None))
    # retranslateUi

