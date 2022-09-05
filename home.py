import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from homeui import *


class home(QMainWindow, Ui_homeui):
    def __init__(self, parent=None):
        super(home, self).__init__(parent)
        self.setupUi(self)


def home_run():
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    Ui = home()
    # 将窗口控件显示在屏幕上
    Ui.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

# home_run()