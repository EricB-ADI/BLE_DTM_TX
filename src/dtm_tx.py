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
        self.ui.baud_rate_select.setValue(hci_util.DEFAULT_BAUDRATE)
        self.ui.start_stop_btn.clicked.connect(self.dtm_btn_click)
        self.inputs_disabled = False

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
            msg_box = QMessageBox()
            msg_box.setText("Failed to reset Device!")
            msg_box.exec()
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
                pass

            self.ui.start_stop_btn.setText('STOP')

        else:

            try:
                hci.endTestFunc(None)
            except:
                msg_box = QMessageBox()
                msg_box.setText("Failed to reset Device!")
                msg_box.exec()

            self.enable_inputs()
            self.ui.start_stop_btn.setText('START')

    def disable_inputs(self):
        self.ui.input_frame.setDisabled(True)
        self.inputs_disabled = True

    def enable_inputs(self):
        self.ui.input_frame.setDisabled(False)
        self.inputs_disabled = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
