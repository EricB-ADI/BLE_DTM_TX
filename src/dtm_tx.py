"""
Main Application for DTM Testsing
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow


import hci_util
import BLE_hci
import BLE_util


class MainWindow(QMainWindow):
    """
    App Main Window
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.win = Ui_MainWindow()
        self.win.setupUi(self)

        self.refresh_port_select()
        self.win.baud_rate_select.setValue(hci_util.DEFAULT_BAUDRATE)

        self.win.phy_select.insertItems(0, BLE_util.AVAILABLE_PHYS)
        self.win.packet_type_select.insertItems(
            0, BLE_util.TX_PACKET_TYPE_OPTIONS)
        self.win.power_select.insertItems(0, BLE_util.AVAILABLE_TX_POWERS)
        self.win.power_select.setCurrentIndex(
            len(BLE_util.AVAILABLE_TX_POWERS) - 1)

        self.win.channel_select.valueChanged.connect(self.slider_value_changed)
        self.win.packet_len_select.valueChanged.connect(
            self.slider_value_changed)
        self.win.start_stop_btn.clicked.connect(self.dtm_btn_click)

        self.set_channel_label(0)
        self.set_packet_len_label(0)

        self.dtm_test_started = False

    def refresh_port_select(self):
        """
        Refreshes available ports in port selector
        """
        self.win.port_select.clear()
        self.win.port_select.insertItems(0, hci_util.serial_ports())

    def set_channel_label(self, channel):
        """
        Sets the label to show the channel
        """
        self.win.channel_label.setText(f'Channel {channel}')

    def set_packet_len_label(self, packet_len):
        """
        Sets the label to show the packet length
        """
        self.win.packet_len_label.setText(f'Packet Length {packet_len}')

    def slider_value_changed(self):
        """
        Updates Labels whenever slider values are moved
        """
        self.set_channel_label(self.win.channel_select.value())
        self.set_packet_len_label(self.win.packet_len_select.value())

    def dtm_btn_click(self):
        """
            Starts or Stops DTM test 
        """
        port = self.win.port_select.currentText()
        baud_rate = self.win.baud_rate_select.value()

        hci = BLE_hci.BLE_hci(BLE_hci.Namespace(
            serialPort=port,
            monPort='',
            baud=baud_rate
        ))

        try:
            hci.resetFunc(None)
        except:
            self.show_basic_msg_box('Failed to reset devices!')

        if not self.dtm_test_started:
            tx_power = int(self.win.power_select.currentText().split('dbm')[0])
            channel = int(self.win.channel_select.value())
            payload = BLE_hci.TX_PACKET_TYPES[self.win.packet_type_select.currentText(
            )]
            phy = BLE_hci.TX_PHY_TYPES[self.win.phy_select.currentText()]
            packet_len = self.win.packet_len_select.value()

            try:
                hci.txPowerFunc(BLE_hci.Namespace(power=tx_power, handle="0"))
                hci.txTestFunc(BLE_hci.Namespace(
                    channel=channel, phy=phy, payload=payload, packetLength=packet_len))
                self.disable_inputs()
                self.win.start_stop_btn.setText('STOP')
                self.dtm_test_started = True
            except:
                self.show_basic_msg_box('Failed to start test')

        else:
            self.enable_inputs()
            self.dtm_test_started = False
            self.win.start_stop_btn.setText('START')
            try:
                hci.endTestFunc(None)
            except:
                self.show_basic_msg_box('Failed to end test!')

    def show_basic_msg_box(self, msg):
        """
            Display a basic message box with a given message
        """
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec()

    def disable_inputs(self):
        """
            Disable all inputs used for DTM testing 
            to prevent alterations before stopping the test
        """
        self.win.input_frame.setDisabled(True)

    def enable_inputs(self):
        """
        Enable all DTM inputs
        """
        self.win.input_frame.setDisabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
