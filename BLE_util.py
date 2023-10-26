

MAX_CHANNEL = 39
MIN_CHANNEL = 0
AVAILABLE_TX_POWERS = ['-15dbm', '-10dbm',
                       '-5dbm', '0dbm', '2dbm', '4dbm', '6dbm']


def channel_to_freq(channel):
    return 2.402e9 * (channel + 1)
