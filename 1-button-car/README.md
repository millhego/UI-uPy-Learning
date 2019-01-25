# button-car UI设计

实现一个通过mqtt通信的ui程序,能够按下一个方向的按键则发送该方向的信号,松开则发送停止信号



1、打开qtdesigner

2、创建一个MainWindow

3、添加八个方向按键

4、保存为DirBtn.ui

5、[使用pyuic5生成DirBtn.py](https://blog.csdn.net/px41834/article/details/79383985)

6、新建ui_main.py,编写UI逻辑

7、测试ui能否正常运行、逻辑是否正确

7.5、[无法启动qt5程序解决办法](https://blog.csdn.net/ouening/article/details/81093697 ) 

8、创建数据传输（使用mqtt）类，实现数据通信

9、测试自收自发，确保模块可用

10、修改回正确的收发主题(此次UI数据发送到'button-car/UI_data'主题, 小车发送到'button-car/MCU_data'。 MCU没有发送数据，没有写接收函数)

11、打包成.exe文件

​	一些bug:

 - [成功解决AttributeError: module 'enum' has no attribute 'IntFlag'?](https://blog.csdn.net/qq_41185868/article/details/80599336)

 - ui_main.py运行报错： This application failed to satart because no Qt platform plugin could be initialized......
   方法1:

   将Python36\Lib\site-packages\PyQt5\Qt\plugins\platforms文件夹复制一份到生成的.exe所在文件夹处

   方法2:
   添加这一句

   ```python
   _os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = _os.path.dirname(__file__) + r'\Qt\plugins'
   ```

    到Python36\Lib\site-packages\PyQt5\\\_\_init\_\_.py中,或设为环境变量

- 线程要设为守护线程(daemon=True)

# 小车

制作一个使用mqtt通信的物联网小车代码

1、编写实现mqtt通信模块的代码

​	- mqtt库可以在这找到https://github.com/micropython/micropython-lib

2、测试mqtt通信模块是否可用

3、添加控制电机的代码

4、测试

# 文件

## 第一版

mcu-code/ 

​	umqtt/		——MQTT通信的基础库

​	boot.py		——初始化wifi连接

​	GY25.py		——和GY25(串口陀螺仪模块)数据读取有关的代码

​	main.py		——主程序逻辑

​	motor.py	——和电机控制有关的代码

​	mymq.py 	——和mqtt通信有关的代码

DirBtn.py 		——UI界面的.py代码

DirBtn.ui		——UI界面的.ui代码

package2exe.py	——用于生成ui_main.py的.exe文件

README.md		——你正在看的这玩意

ui_main.py		——UI的主程序逻辑代码

