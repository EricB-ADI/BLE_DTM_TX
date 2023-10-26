import BLE_hci

MAX_CHANNEL = 39
MIN_CHANNEL = 0
AVAILABLE_TX_POWERS = ['-15dbm', '-10dbm',
                       '-5dbm', '0dbm', '2dbm', '4dbm', '6dbm']
AVAILABLE_PHYS = ['1M', '2M', 'S8', 'S2']
TX_PACKET_TYPE_OPTIONS = list(BLE_hci.TX_PACKET_TYPES.keys())
TX_PHY_TYPE_OPTIONS = list(BLE_hci.TX_PHY_TYPES.keys())


def channel_to_freq(channel):
    return 2.402e9 * (channel + 1)
