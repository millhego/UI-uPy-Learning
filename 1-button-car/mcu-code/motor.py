from machine import PWM, Pin

pwma = PWM(Pin(22), freq=1000)
pwmb = PWM(Pin(4), freq=1000)
ain2 = Pin(1, Pin.OUT)
ain1 = Pin(3, Pin.OUT)
bin1 = Pin(21, Pin.OUT)
bin2 = Pin(0, Pin.OUT)

def seta(value):
    if value > 0:
        ain1(1)
        ain2(0)
    elif value < 0:
        ain1(0)
        ain2(1)
        value = - value
    else:
        ain1(0)
        ain2(0)
    pwma.duty(value * 1023 // 100)


def setb(value):
    if value > 0:
        bin1(1)
        bin2(0)
    elif value < 0:
        bin1(0)
        bin2(1)
        value = - value
    else:
        bin1(0)
        bin2(0)
    pwmb.duty(value * 1023 // 100)


