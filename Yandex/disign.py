import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QButtonGroup


class Ui_FlagMaker(object):
    def setupUi(self, FlagMaker):
        FlagMaker.setObjectName("FlagMaker")
        FlagMaker.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=FlagMaker)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 170, 347, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 2, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 2, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 2, 2, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 3, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 3, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.make_flag = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.make_flag.setObjectName("make_flag")
        self.gridLayout.addWidget(self.make_flag, 4, 2, 1, 1)
        self.result = QtWidgets.QLabel(self)
        self.result.setObjectName("result")
        self.result.move(300, 400)
        self.result.resize(1000, 20)
        self.result.hide()
        # добавлен код руками
        self.color_group_1 = QButtonGroup(self)
        self.color_group_1.addButton(self.radioButton)
        self.color_group_1.addButton(self.radioButton_4)
        self.color_group_1.addButton(self.radioButton_7)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_2.addButton(self.radioButton_2)
        self.color_group_2.addButton(self.radioButton_5)
        self.color_group_2.addButton(self.radioButton_8)
        self.color_group_3 = QButtonGroup(self)
        self.color_group_3.addButton(self.radioButton_3)
        self.color_group_3.addButton(self.radioButton_6)
        self.color_group_3.addButton(self.radioButton_9)

        FlagMaker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=FlagMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        FlagMaker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=FlagMaker)
        self.statusbar.setObjectName("statusbar")
        FlagMaker.setStatusBar(self.statusbar)

        self.retranslateUi(FlagMaker)
        QtCore.QMetaObject.connectSlotsByName(FlagMaker)

    def retranslateUi(self, FlagMaker):
        _translate = QtCore.QCoreApplication.translate
        FlagMaker.setWindowTitle(_translate("FlagMaker", "MainWindow"))
        self.radioButton_5.setText(_translate("FlagMaker", "Красный"))
        self.radioButton_4.setText(_translate("FlagMaker", "Красный"))
        self.radioButton_6.setText(_translate("FlagMaker", "Красный"))
        self.radioButton_8.setText(_translate("FlagMaker", "Зеленый"))
        self.label_2.setText(_translate("FlagMaker", "Цвет №2"))
        self.label_3.setText(_translate("FlagMaker", "Цвет №3"))
        self.radioButton_3.setText(_translate("FlagMaker", "Синий"))
        self.radioButton_9.setText(_translate("FlagMaker", "Зеленый"))
        self.radioButton_2.setText(_translate("FlagMaker", "Синий"))
        self.label.setText(_translate("FlagMaker", "Цвет №1"))
        self.radioButton_7.setText(_translate("FlagMaker", "Зеленый"))
        self.radioButton.setText(_translate("FlagMaker", "Синий"))
        self.make_flag.setText(_translate("FlagMaker", "Сделать флаг"))
        self.result.setText(_translate("FlagMaker", "TextLabel"))
        

class FlagMaker(QMainWindow, Ui_FlagMaker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.make_flag.clicked.connect(self.run)

    def run(self):
        try:
            color1 = self.color_group_1.checkedButton().text()
            color2 = self.color_group_2.checkedButton().text()
            color3 = self.color_group_3.checkedButton().text()
            self.result.setText(f"Цвета: {color1}, {color2} и {color3}")
            self.result.show()
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())