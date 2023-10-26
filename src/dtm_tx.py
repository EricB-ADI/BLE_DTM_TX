import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow


import hci_util
import BLE_hci
# from BLE_hci import BLE_hci, Namespace
import BLE_util


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ports = hci_util.serial_ports()

        self.ui.port_select.insertItems(0, self.ports)
        self.ui.phy_select.insertItems(0, list(BLE_hci.TX_PHY_OPTIONS.keys()))
        self.ui.power_select.insertItems(0, BLE_util.AVAILABLE_TX_POWERS)
        self.ui.power_select.setCurrentIndex(
            len(BLE_util.AVAILABLE_TX_POWERS) - 1)
        self.ui.channel_select.setRange(
            BLE_util.MIN_CHANNEL, BLE_util.MAX_CHANNEL)

        self.ui.channel_select.valueChanged.connect(self.slider_value_changed)
        self.ui.packet_len_select.valueChanged.connect(
            self.slider_value_changed)

        self.ui.baud_rate_select.setValue(hci_util.DEFAULT_BAUDRATE)

        self.ui.start_stop_btn.clicked.connect(self.dtm_btn_click)

        self.set_channel_label(0)
        self.set_packet_len_label(0)
        

    def set_channel_label(self, channel):
        self.ui.channel_label.setText(f'Channel {channel}')

    def set_packet_len_label(self, packet_len):
        self.ui.packet_len_label.setText(f'Packet Length {packet_len}')

    def slider_value_changed(self):
        self.set_channel_label(self.ui.channel_select.value())
        self.set_packet_len_label(self.ui.packet_len_select.value())

    def dtm_btn_click(self):

        port = self.ui.port_select.currentText()
        baud_rate = self.ui.baud_rate_select.value()

        hci = BLE_hci.BLE_hci(BLE_hci.Namespace(
            serialPort=port,
            monPort='',
            baud=baud_rate
        ))

        try:
            hci.resetFun(None)
        except:
            self.show_basic_msg_box('Failed to reset devices!')
            return

        if self.ui.start_stop_btn.text() == 'START':
            tx_power = int(self.ui.power_select.currentText().split('dbm')[0])
            channel = int(self.ui.channel_select.value())
            phy = BLE_hci.TX_PHY_OPTIONS[self.ui.phy_select.currentText()]
            packet_len = self.ui.packet_len_select
            try:
                hci.txPowerFunc(BLE_hci.Namespace(power=tx_power, handle="0"))
                hci.txTestFunc(BLE_hci.Namespace(
                    channel=channel, phy=phy, payload=0, packetLength=packet_len))
                self.disable_inputs()
            except:
                self.show_basic_msg_box('Failed to start test')
                

            self.ui.start_stop_btn.setText('STOP')

        else:
            self.enable_inputs()

            try:
                hci.endTestFunc(None)
            except:
                self.ui.start_stop_btn.setText('START')
                self.show_basic_msg_box('Failed to end test!')

    def show_basic_msg_box(self, msg):
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec()

    def disable_inputs(self):
        self.ui.input_frame.setDisabled(True)
        

    def enable_inputs(self):
        self.ui.input_frame.setDisabled(False)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
