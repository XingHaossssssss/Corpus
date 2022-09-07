import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from homeui import *
import translate


class home(QMainWindow, Ui_homeui):
    def __init__(self):
        super(home, self).__init__()
        self.setupUi(self)
        self.PushButton_1.clicked.connect(self.but_click)

    def but_click(self):
        search_str = self.lineEdit_1.text()
        translate_result = translate.fanyi1(search_str)
        self.textEdit_1.setText(translate_result)






def home_run():
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    Ui = home()
    # 将窗口控件显示在屏幕上
    Ui.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

#home_run()