import sys
from math import factorial

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Yandex/upload.ui', self)

        # Кнопки с цифрами и знаками
        self.btn0.clicked.connect(self.add)
        self.btn1.clicked.connect(self.add)
        self.btn2.clicked.connect(self.add)
        self.btn3.clicked.connect(self.add)
        self.btn4.clicked.connect(self.add)
        self.btn5.clicked.connect(self.add)
        self.btn6.clicked.connect(self.add)
        self.btn7.clicked.connect(self.add)
        self.btn8.clicked.connect(self.add)
        self.btn9.clicked.connect(self.add)
        self.btn_dot.clicked.connect(self.add)

        # Кнопки операций
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_div.clicked.connect(self.div)
        self.btn_eq.clicked.connect(self.eq)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_pow.clicked.connect(self.powi)

        # Кнопки резких операций
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        # Скрытые и почти скрытые данные данные
        self.num_1 = ''
        self.num_2 = ''
        self.oper1 = 0
        self.oper2 = 0
        self.operator = ''
        self.second = False
    
    def add(self):
        btn_s = self.sender()
        if not self.second:
            self.num_1 += btn_s.text()
            self.table.display(self.num_1)
        else:
            self.num_2 += btn_s.text()
            self.table.display(self.num_2)
    
    def sqrt(self):
        if not self.second:
            self.num_1 = str(float(self.num_1) ** 0.5)
            self.table.display(self.num_1)
        else:
            self.num_2 = str(float(self.num_2) ** 0.5)
            self.table.display(self.num_2)
    
    def fact(self):
        if not self.second:
            self.num_1 = str(factorial(int(self.num_1)))
            self.table.display(self.num_1)
        else:
            self.num_2 = str(factorial(int(self.num_2)))
            self.table.display(self.num_2)
    
    def powi(self):
        self.oper1 = float(self.num_1)
        self.second = True
        self.num_1 = ''
        self.operator = '**'
    
    def plus(self):
        self.oper1 = float(self.num_1)
        self.second = True
        self.num_1 = ''
        self.operator = '+'
    
    def minus(self):
        self.oper1 = float(self.num_1)
        self.second = True
        self.num_1 = ''
        self.operator = '-'

    def mult(self):
        self.oper1 = float(self.num_1)
        self.second = True
        self.num_1 = ''
        self.operator = '*'

    def div(self):
        self.oper1 = float(self.num_1)
        self.second = True
        self.num_1 = ''
        self.operator = '/'
    
    def eq(self):
        try:
            self.oper2 = float(self.num_2)
            self.num_2 = ''
            if self.operator == '+':
                self.num_1 = self.oper1 + self.oper2
            elif self.operator == '-':
                self.num_1 = self.oper1 - self.oper2
            elif self.operator == '*':
                self.num_1 = self.oper1 * self.oper2
            elif self.operator == '/':
                self.num_1 = self.oper1 / self.oper2
            elif self.operator == '**':
                self.num_1 = self.oper1 ** self.oper2
            self.second = False
            self.table.display(self.num_1)
        except ZeroDivisionError:
            self.num_1 = 'ERROR'
            self.second = False
            self.table.display(self.num_1)
            self.num_1 = ''
        except ValueError:
            self.num_1 = 'ERROR'
            self.second = False
            self.table.display(self.num_1)
            self.num_1 = ''
        
    def clear(self):
        self.num_1 = ''
        self.num_2 = ''
        self.oper1 = ''
        self.oper2 = ''
        self.operator = ''
        self.second = False
        self.table.display('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())