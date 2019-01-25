import time
from mymq import MsgTransfer
import network
from boot import do_connect
import gc
from motor import seta, setb


def on_message(topic, msg):
    if b'up' == msg:
        # up
        seta(100)
        setb(100)
    elif b'left' == msg:
        # left
        seta(100)
        setb(-100)
    elif b'stop' == msg:
        # stop
        seta(0)
        setb(0)
    elif b'down' == msg:
        # down
        seta(-100)
        setb(-100)
    elif b'right' == msg:
        # right
        seta(-100)
        setb(100)
    elif b'leftup' == msg:
        # left up
        seta(100)
        setb(50)
    elif b'rightup' == msg:
        # right up
        seta(50)
        setb(100)
    elif b'leftdown' == msg:
        # left down
        seta(-100)
        setb(-50)
    elif b'rightdown' == msg:
        # right down
        seta(-50)
        setb(-100)


sta_if = network.WLAN(network.STA_IF)
while not sta_if.isconnected():
    do_connect()

mqtt = MsgTransfer(host=sta_if.ifconfig()[2],
                   mainTopic='button-car',
                   on_message=on_message)

while not mqtt.is_connect:
    mqtt = MsgTransfer(host=sta_if.ifconfig()[2],
                       mainTopic='button-car',
                       on_message=on_message)
    gc.collect()
gc.collect()
# '192.168.137.1', '192.168.137.1'

while True:
    mqtt.loop()



