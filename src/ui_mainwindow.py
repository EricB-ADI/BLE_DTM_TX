# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dtm_tx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 454)
        MainWindow.setMaximumSize(QSize(16777215, 720))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.input_frame = QFrame(self.centralwidget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.input_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.input_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label)

        self.port_select = QComboBox(self.input_frame)
        self.port_select.setObjectName(u"port_select")

        self.verticalLayout.addWidget(self.port_select)

        self.label_2 = QLabel(self.input_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.baud_rate_select = QSpinBox(self.input_frame)
        self.baud_rate_select.setObjectName(u"baud_rate_select")
        self.baud_rate_select.setMaximum(10000000)

        self.verticalLayout.addWidget(self.baud_rate_select)

        self.label_3 = QLabel(self.input_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.phy_select = QComboBox(self.input_frame)
        self.phy_select.setObjectName(u"phy_select")

        self.verticalLayout.addWidget(self.phy_select)

        self.label_4 = QLabel(self.input_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_4)

        self.power_select = QComboBox(self.input_frame)
        self.power_select.setObjectName(u"power_select")

        self.verticalLayout.addWidget(self.power_select)

        self.label_5 = QLabel(self.input_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_5)

        self.channel_select = QSpinBox(self.input_frame)
        self.channel_select.setObjectName(u"channel_select")

        self.verticalLayout.addWidget(self.channel_select)

        self.label_7 = QLabel(self.input_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_7)

        self.packet_len_select = QSpinBox(self.input_frame)
        self.packet_len_select.setObjectName(u"packet_len_select")

        self.verticalLayout.addWidget(self.packet_len_select)


        self.verticalLayout_3.addWidget(self.input_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_stop_btn = QPushButton(self.frame)
        self.start_stop_btn.setObjectName(u"start_stop_btn")
        self.start_stop_btn.setMaximumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.start_stop_btn)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DTM_TX", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_select.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baud", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PHY", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Packet Length", None))
        self.start_stop_btn.setText(QCoreApplication.translate("MainWindow", u"START", None))
    # retranslateUi

