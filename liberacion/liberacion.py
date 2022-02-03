import sys
from PyQt5 import QtWidgets
from ui import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
