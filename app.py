

import sys
import hci_util
import BLE_hci
import BLE_util

from PySide6.QtWidgets import (
    
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QComboBox,
    QSpinBox,

)

class Window(QWidget):
    def __init__(self) -> None:
        super(Window,self).__init__()

        self.ports = hci_util.serial_ports()
        self.serialPortBox = QComboBox()
        self.txPhysBox = QComboBox()
        self.tx_powers = QComboBox()
        self.serialPortBox.insertItems(0, self.ports)
        self.txPhysBox.insertItems(0, list(BLE_hci.TX_PHY_OPTIONS.keys()))
        self.tx_powers.insertItems(0, list(BLE_util.AVAILABLE_TX_POWERS))
        self.tx_powers.setCurrentIndex(len(BLE_util.AVAILABLE_TX_POWERS) - 1)

        self.channelSelect = QSpinBox()
        self.channelSelect.setRange(BLE_util.MIN_CHANNEL, BLE_util.MAX_CHANNEL)
        self.start_stop_btn = QPushButton('START')
        self.start_stop_btn.clicked.connect(self.dtm_btn_click)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.serialPortBox)
        layout.addWidget(self.txPhysBox)
        layout.addWidget(self.tx_powers)
        layout.addWidget(self.channelSelect)
        layout.addWidget(self.start_stop_btn)


    def dtm_btn_click(self):
        if self.start_stop_btn.text() == 'START':
            self.start_stop_btn.setText('STOP')
        else:
            self.start_stop_btn.setText('START')


if __name__ == '__main__':            
    app = QApplication([])
    window = Window()
    window.setWindowTitle("DTM TX")
    window.show()
    sys.exit(app.exec())

