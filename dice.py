import sys
import os.path
from random import randrange

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap


class DiceWindow(QDialog):
    def __init__(self, parent=None):
        super(DiceWindow, self).__init__(parent)
        self.ui = uic.loadUi(os.path.join('ui', 'dice_roller.ui'), self)
        fnames = ['dice-six-faces-one.svg',
                  'dice-six-faces-two.svg',
                  'dice-six-faces-three.svg',
                  'dice-six-faces-four.svg',
                  'dice-six-faces-five.svg',
                  'dice-six-faces-six.svg']

        self.pics = []
        for fname in fnames:
            self.pics.append(QPixmap(os.path.join('images', fname)))

    @pyqtSlot()
    def on_rollButton_clicked(self):
        d1 = randrange(1, 7)
        d2 = randrange(1, 7)
        self.roll1.setPixmap(self.pics[d1 - 1])
        self.roll2.setPixmap(self.pics[d2 - 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiceWindow()
    ex.show()
    sys.exit(app.exec_())
