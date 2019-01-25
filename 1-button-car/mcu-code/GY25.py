from machine import UART, Timer
import struct

baudrate = 115200
rx = 16
tx = 17
sample_freq = 100
uart = UART(1, baudrate, rx=rx, tx=tx)
uart.write(bytearray([0xa5, 0x52]))
stat = 0

tim = Timer(-1)
yaw, pitch, roll = 0, 0, 0


def tim_irq(t):
    global yaw, pitch, roll
    if uart.any():
        data = uart.read()
        if len(data) > 7 and data[0] == 0xaa:
            head, yaw, pitch, roll, end = struct.unpack('>BhhhB', data)
            yaw, pitch, roll,  = yaw/100, pitch/100, roll/100


tim.init(period=10, mode=Timer.PERIODIC, callback=tim_irq)
