import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QButtonGroup, QFileDialog
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor
from ui import Ui_PIL20
from PyQt6.QtCore import QPoint


class MyPillow(QMainWindow, Ui_PIL20):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        filename = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.orig_image = QImage(filename)
        self.curr_image = QImage(filename)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
        self.label.setPixmap(self.pixmap)
        self.degree = 0

        # Создаем кнопки
        self.channelButtons = QButtonGroup(self)
        self.channelButtons.addButton(self.pushButton)
        self.channelButtons.addButton(self.pushButton_2)
        self.channelButtons.addButton(self.pushButton_3)
        self.channelButtons.addButton(self.pushButton_4)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.change_color)
        self.rotateButtons = QButtonGroup(self)
        self.rotateButtons.addButton(self.pushButton_5)
        self.rotateButtons.addButton(self.pushButton_6)
        for button in self.rotateButtons.buttons():
            button.clicked.connect(self.rotate)


    def change_color(self):
        self.curr_image = self.orig_image.copy()
        x, y = self.curr_image.size().width(), self.curr_image.size().height()

        for i in range(x):
            for j in range(y):
                r, g, b, _ = self.curr_image.pixelColor(i, j).getRgb()
                if (self.sender().text() == 'R'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(r, 0, 0))
                elif (self.sender().text() == 'G'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(0, g, 0))
                elif (self.sender().text() == 'B'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(0, 0, b))
                else:
                    pass

        self.help_rotate(self.degree)
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.pixmap = self.pixmap.scaled(self.label.width(), 
                                         self.label.height())
        self.label.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.pushButton_6:
            self.degree += 90
            degree = 90
        else:
            self.degree -= 90
            degree = -90
        self.degree %= 360
        self.help_rotate(self.degree)

        t = QTransform().rotate(degree)
        self.curr_image = self.curr_image.transformed(t)

        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
        self.label.setPixmap(self.pixmap)

    def help_rotate(self, new_degree):
        t = QTransform().rotate(new_degree)
        self.curr_image = self.curr_image.transformed(t)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
