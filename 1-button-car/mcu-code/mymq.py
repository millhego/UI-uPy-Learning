import time
from umqtt import simple as mqtt
#import _thread


class MsgTransfer():
    def __init__(self, host='127.0.0.1', port=1883,
                 username='admin', password='public', mainTopic='', on_message=None):
        client_id = 'MCU_' + ''.join(map(str, time.localtime()))
        self.send_topic = '/'.join([mainTopic, 'MCU_data'])
        self.client = mqtt.MQTTClient(client_id, host, port, username, password)  # ClientId不能重复，所以使用当前时间
        self.client.set_callback(on_message)
        self.client.on_connect = self.on_connect
        for i in range(10):
            try:
                self.client.connect()
                self.is_connect = True
                break
            except KeyboardInterrupt:
                raise
            except BaseException as e:
                self.is_connect = False
                print('mqtt connect error', e)
                time.sleep(1)
        if i == 9:
            return
        self.client.subscribe('/'.join([mainTopic, 'UI_data']))
        #_thread.start_new_thread(self.loop, ())

    def on_message(self, topic, msg):
        print(msg.topic, msg.payload)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def send(self, data):
        self.client.publish(self.send_topic, data)

    def loop(self):
        self.client.check_msg()

