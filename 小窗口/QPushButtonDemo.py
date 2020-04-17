'''

按钮控件 (QPushuButton)

QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox


'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('Fist Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        layout.addWidget(self.button1)
        layout.addWidget( )

        #在文本前面显示图像

        self.button2 = QPushButton('图像按钮')


        self.setLayout(layout)
    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
