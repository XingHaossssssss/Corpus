import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from ui_text import *
from homeui import *
# from translatetext import *
from translate import *


class home(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(home, self).__init__()
        self.setupUi(self)

        # 左边按钮
        self.btnl1 = self.pushButton_cor
        self.btnl2 = self.pushButton_tran
        self.btnl3 = self.pushButton_anlysis
        self.btnl4 = self.pushButton_info
        self.btnl5 = self.pushButton_settings
        # 设置点击按钮属性
        self.btnl1.clicked.connect(self.display)
        self.btnl2.clicked.connect(self.display)
        self.btnl3.clicked.connect(self.display)
        self.btnl4.clicked.connect(self.display)
        self.btnl5.clicked.connect(self.display)

        # 词汇翻译
        # 翻译按钮
        self.btn_tran = self.pushButton_8
        self.tedit_content = self.textEdit
        self.tedit_tran = self.textEdit_2
        self.btn_tran.clicked.connect(self.trans)


    def display(self):
        sender = self.sender()
        if sender.text() == '语料库':
            self.stackedWidget.setCurrentIndex(0)
        elif sender.text() == '词汇翻译':
            self.stackedWidget.setCurrentIndex(1)
        elif sender.text() == '数据分析':
            self.stackedWidget.setCurrentIndex(2)
        elif sender.text() == '个人中心':
            self.stackedWidget.setCurrentIndex(3)
        elif sender.text() == '设置':
            self.stackedWidget.setCurrentIndex(4)

    def trans(self):
        word = self.tedit_content.toPlainText()
        result = fanyi_youdao(word)
        self.tedit_tran.setPlainText(result)









def home_run():
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    Ui = home()
    # 将窗口控件显示在屏幕上
    Ui.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

home_run()