# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dtm_tx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 579)
        MainWindow.setMaximumSize(QSize(16777215, 720))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input_frame = QFrame(self.centralwidget)
        self.input_frame.setObjectName("input_frame")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.input_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.input_frame)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label)

        self.port_select = QComboBox(self.input_frame)
        self.port_select.setObjectName("port_select")

        self.verticalLayout.addWidget(self.port_select)

        self.label_2 = QLabel(self.input_frame)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.baud_rate_select = QSpinBox(self.input_frame)
        self.baud_rate_select.setObjectName("baud_rate_select")
        self.baud_rate_select.setMaximum(10000000)

        self.verticalLayout.addWidget(self.baud_rate_select)

        self.label_3 = QLabel(self.input_frame)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.phy_select = QComboBox(self.input_frame)
        self.phy_select.setObjectName("phy_select")

        self.verticalLayout.addWidget(self.phy_select)

        self.packet_type_label = QLabel(self.input_frame)
        self.packet_type_label.setObjectName("packet_type_label")
        self.packet_type_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.packet_type_label)

        self.packet_type_select = QComboBox(self.input_frame)
        self.packet_type_select.setObjectName("packet_type_select")

        self.verticalLayout.addWidget(self.packet_type_select)

        self.label_4 = QLabel(self.input_frame)
        self.label_4.setObjectName("label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_4)

        self.power_select = QComboBox(self.input_frame)
        self.power_select.setObjectName("power_select")

        self.verticalLayout.addWidget(self.power_select)

        self.channel_label = QLabel(self.input_frame)
        self.channel_label.setObjectName("channel_label")
        self.channel_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.channel_label)

        self.channel_select = QSlider(self.input_frame)
        self.channel_select.setObjectName("channel_select")
        self.channel_select.setMaximum(39)
        self.channel_select.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.channel_select)

        self.packet_len_label = QLabel(self.input_frame)
        self.packet_len_label.setObjectName("packet_len_label")
        self.packet_len_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.packet_len_label)

        self.packet_len_select = QSlider(self.input_frame)
        self.packet_len_select.setObjectName("packet_len_select")
        self.packet_len_select.setMaximum(255)
        self.packet_len_select.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.packet_len_select)

        self.verticalLayout_3.addWidget(self.input_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_stop_btn = QPushButton(self.frame)
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.start_stop_btn.setMaximumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.start_stop_btn)

        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "DTM_TX", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "Port", None))
        self.port_select.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Baud", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "PHY", None))
        self.packet_type_label.setText(
            QCoreApplication.translate("MainWindow", "Packet Type", None)
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Power", None))
        self.channel_label.setText(
            QCoreApplication.translate("MainWindow", "Channel", None)
        )
        self.packet_len_label.setText(
            QCoreApplication.translate("MainWindow", "Packet Length", None)
        )
        self.start_stop_btn.setText(
            QCoreApplication.translate("MainWindow", "START", None)
        )

    # retranslateUi
