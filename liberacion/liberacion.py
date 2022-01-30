from PyQt5 import QtWidgets
from ui import *
import sys


app = QtWidgets.QApplication(sys.argv)
window = LoginWindow()
app.exec()
