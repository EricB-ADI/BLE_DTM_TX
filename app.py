

import sys
import hci_util
import BLE_hci
# from BLE_hci import BLE_hci, Namespace
import BLE_util

from PySide6.QtWidgets import (
    
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QComboBox,
    QSpinBox,
    QMessageBox
)

class Window(QWidget):
    def __init__(self) -> None:
        super(Window,self).__init__()

        self.ports = hci_util.serial_ports()
        self.serialPortBox = QComboBox()
        self.baud_rate = QSpinBox()
        self.txPhysBox = QComboBox()
        self.tx_powers = QComboBox()
        self.channelSelect = QSpinBox()
        self.start_stop_btn = QPushButton('START')
        
        
        self.serialPortBox.insertItems(0, self.ports)
        self.txPhysBox.insertItems(0, list(BLE_hci.TX_PHY_OPTIONS.keys()))
        self.tx_powers.insertItems(0, list(BLE_util.AVAILABLE_TX_POWERS))
        self.tx_powers.setCurrentIndex(len(BLE_util.AVAILABLE_TX_POWERS) - 1)
        self.channelSelect.setRange(BLE_util.MIN_CHANNEL, BLE_util.MAX_CHANNEL)
        self.baud_rate.setRange(9600, 1_000_000)
        self.baud_rate.setValue(115200)
        self.start_stop_btn.clicked.connect(self.dtm_btn_click)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.serialPortBox)
        layout.addWidget(self.baud_rate)
        layout.addWidget(self.txPhysBox)
        layout.addWidget(self.tx_powers)
        layout.addWidget(self.channelSelect)
        layout.addWidget(self.start_stop_btn)
        self.selected_port = ''

    def dtm_btn_click(self):
        
        port = self.serialPortBox.currentText()
        baud_rate = self.baud_rate.value()
        
        hci = BLE_hci.BLE_hci(BLE_hci.Namespace(
            serialPort=port,
            monPort='',
            baud=baud_rate
        ))

        
        try:
            hci.resetFunc(None)
        except:
            msg_box = QMessageBox()
            msg_box.setText("Failed to reset Device!")
            msg_box.exec()
            return


        if self.start_stop_btn.text() == 'START':
            tx_power = int(self.tx_powers.currentText().split('dbm')[0])
            channel = int(self.channelSelect.value())
            phy = BLE_hci.TX_PHY_OPTIONS[self.txPhysBox.currentText()]
            packet_len = 100
            try:
                hci.txPowerFunc(BLE_hci.Namespace(power=tx_power, handle="0"))
                hci.txTestFunc(BLE_hci.Namespace(channel=channel, phy=phy,payload=0,packetLength=packet_len))
            except:
                pass


            self.start_stop_btn.setText('STOP')
            self.disable_inputs()
        else:

            try:
                hci.endTestFunc(None)
            except:
                msg_box = QMessageBox()
                msg_box.setText("Failed to reset Device!")
                msg_box.exec()
            
            self.enable_inputs()
            self.start_stop_btn.setText('START')

    def disable_inputs(self):
        self.serialPortBox.setDisabled(True) 
        self.baud_rate.setDisabled(True) 
        self.txPhysBox.setDisabled(True) 
        self.tx_powers.setDisabled(True) 
        self.channelSelect.setDisabled(True) 
        
    
    def enable_inputs(self):
        self.serialPortBox.setDisabled(False) 
        self.baud_rate.setDisabled(False) 
        self.txPhysBox.setDisabled(False) 
        self.tx_powers.setDisabled(False) 
        self.channelSelect.setDisabled(False) 
        

if __name__ == '__main__':            
    app = QApplication([])
    window = Window()
    window.setWindowTitle("DTM TX")
    window.show()
    sys.exit(app.exec())

