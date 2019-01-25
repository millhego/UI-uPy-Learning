
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import network
import ntptime
import time
from machine import RTC
import gc

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect("DESKTOP", "12344321")  # Connect to an AP
        time.sleep(5)
        if not sta_if.isconnected():
            sta_if.active(False)
            print("WLAN connect error")
            return

        import webrepl
        webrepl.start()

        for i in range(10):
            try:
                ntptime.settime()
                RTC().init(
                    time.localtime(time.time() + 8 * 3600)[:3] + time.localtime(time.time() + 8 * 3600)[-2:-1] + time.localtime(
                        time.time() + 8 * 3600)[3:-2] + RTC().datetime()[-1:])
                break
            except KeyboardInterrupt:
                raise
            except BaseException as e:
                print("ntp retry", e)


do_connect()
gc.collect()
