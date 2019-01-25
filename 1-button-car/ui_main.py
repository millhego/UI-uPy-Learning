import sys
import time
from threading import Thread
import os

from DirBtn import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import paho.mqtt.client as mqtt


class MsgTransfer:
    """
    mqtt通信用
    UI订阅主topic/MCU_data
    MCU订阅主topic/UI_data
    """
    def __init__(self, host='127.0.0.1', port=11883,
                 username='admin', password='public', mainTopic='', on_message=None, client_id=None):
        """

        :param host: 主机
        :param port: 端口号
        :param username: 用户名
        :param password: 密码
        :param mainTopic: 主topic。共两个topic:主topic/UI_data, 主topic/MCU_data,
        :param on_message: 处理信息的程序
        """
        client_id = client_id or time.strftime('UI_%Y%m%d%H%M%S', time.localtime(time.time()))
        self.send_topic = '-'.join([mainTopic, 'UI_data'])
        sub_topic = '-'.join([mainTopic, 'MCU_data'])
        self.client = mqtt.Client(client_id)  # ClientId不能重复，所以使用当前时间
        self.client.username_pw_set(username, password)  # 必须设置，否则会返回「Connecte
        self.client.on_message = on_message or self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(host, port, 60)
        self.client.subscribe(sub_topic)
        Thread(target=self.client.loop_forever, daemon=True).start()

    def on_message(self, client, userdata, msg):
        """
        默认的处理mqtt订阅消息处理函数
        :param client:
        :param userdata:
        :param msg:
        :return:
        """
        print(msg.topic, msg.payload)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def send(self, data):
        """
        发布数据,
        :param data: 字符串str或json格式数据
        :return:
        """
        self.client.publish(self.send_topic, data)


class MainWin(QMainWindow, Ui_MainWindow):
    """
    主窗体逻辑
    """
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.msgTransfer = MsgTransfer(mainTopic='button-car',)
        self.pushButton.pressed.connect(self.up)
        self.pushButton_2.pressed.connect(self.down)
        self.pushButton_3.pressed.connect(self.left)
        self.pushButton_4.pressed.connect(self.right)
        self.pushButton_5.pressed.connect(self.leftup)
        self.pushButton_6.pressed.connect(self.rightup)
        self.pushButton_7.pressed.connect(self.leftdown)
        self.pushButton_8.pressed.connect(self.rightdown)
        self.pushButton.released.connect(self.stop)
        self.pushButton_2.released.connect(self.stop)
        self.pushButton_3.released.connect(self.stop)
        self.pushButton_4.released.connect(self.stop)
        self.pushButton_5.released.connect(self.stop)
        self.pushButton_6.released.connect(self.stop)
        self.pushButton_7.released.connect(self.stop)
        self.pushButton_8.released.connect(self.stop)

    def up(self):
        print("up")
        self.msgTransfer.send("up")

    def down(self):
        print("down")
        self.msgTransfer.send("down")

    def left(self):
        print("left")
        self.msgTransfer.send("left")

    def right(self):
        print("right")
        self.msgTransfer.send("right")

    def leftup(self):
        print("leftup")
        self.msgTransfer.send("leftup")

    def rightup(self):
        print("rightup")
        self.msgTransfer.send("rightup")

    def leftdown(self):
        print('leftdown')
        self.msgTransfer.send("leftdown")

    def rightdown(self):
        print('rightdown')
        self.msgTransfer.send("rightdown")

    def stop(self):
        print("stop")
        self.msgTransfer.send("stop")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin()
    mainWin.show()
    sys.exit(app.exec_())
