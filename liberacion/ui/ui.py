import sys
from PyQt5 import QtCore, QtWidgets, uic
from service import UsuarioService


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_main_menu.connect(self.show_main_menu)
        self.login.show()

    def show_main_menu(self):
        self.main_menu = MainMenu()
        self.main_menu.switch_liberacion.connect(self.show_liberacion_menu)
        self.main_menu.switch_administracion.connect(self.show_administracion_menu)
        self.main_menu.switch_ajustes.connect(self.show_ajustes_menu)

        self.main_menu.show()

    def show_liberacion_menu(self):
        self.liberacion_menu = LiberacionMenu()
        self.liberacion_menu.switch_back.connect(self.show_main_menu)
        self.liberacion_menu.show()        


    def show_administracion_menu(self):
        self.administracion_menu = AdministracionMenu()
        self.administracion_menu.switch_back.connect(self.show_main_menu)
        self.administracion_menu.show()
    

    def show_ajustes_menu(self):
        self.ajustes_menu = AjustesMenu()
        self.ajustes_menu.switch_back.connect(self.show_main_menu)
        self.main_menu.close()
        self.ajustes_menu.show()


class LoginWindow(QtWidgets.QMainWindow):
    switch_main_menu = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('design/login.ui', self)

        # connect events
        self.acceder_pushbutton.clicked.connect(self.open_main_menu)

        self.show()

    def open_main_menu(self):
        alias = self.alias_lineedit.text()
        contrasena = self.contrasena_lineedit.text()

        if alias and contrasena:
            usuario = UsuarioService.get_by_alias(alias)
            if usuario:
                if usuario.contrasena == contrasena:
                    self.switch_main_menu.emit()
                    self.close()
                else:
                    print('Incorrect password')
            else:
                print('User not found')
        else:
            print('Empty fields')

    
class MainMenu(QtWidgets.QMainWindow):
    switch_liberacion = QtCore.pyqtSignal()
    switch_administracion = QtCore.pyqtSignal()
    switch_ajustes = QtCore.pyqtSignal()
    
    def __init__(self):
        super(MainMenu, self).__init__()
        uic.loadUi('design/main_menu.ui', self)

        # connect events
        self.liberacion_pushbutton.clicked.connect(self.open_liberacion)
        self.administracion_pushbutton.clicked.connect(self.open_administracion)
        self.ajustes_pushbutton.clicked.connect(self.open_ajustes)
        self.salir_pushbutton.clicked.connect(self.exit)

        self.show()

    def open_liberacion(self):
        self.switch_liberacion.emit()
        self.close()

    def open_administracion(self):
        self.switch_administracion.emit()
        self.close()

    def open_ajustes(self):
        self.switch_ajustes.emit()
        self.close()

    def exit(self):
        sys.exit()


class LiberacionMenu(QtWidgets.QMainWindow):
    switch_back = QtCore.pyqtSignal()

    def __init__(self):
        super(LiberacionMenu, self).__init__()
        uic.loadUi('design/liberacion_menu.ui', self)

        # connect events
        self.atras_pushbutton.clicked.connect(self.go_back)

        self.show()

    def go_back(self):
        self.switch_back.emit()
        self.close()


class AdministracionMenu(QtWidgets.QMainWindow):
    switch_back = QtCore.pyqtSignal()

    def __init__(self):
        super(AdministracionMenu, self).__init__()
        uic.loadUi('design/administracion_menu.ui', self)

        # connect events
        self.atras_pushbutton.clicked.connect(self.go_back)

        self.show()

    def go_back(self):
        self.switch_back.emit()
        self.close()


class AjustesMenu(QtWidgets.QMainWindow):
    switch_back = QtCore.pyqtSignal()

    def __init__(self):
        super(AjustesMenu, self).__init__()
        uic.loadUi('design/ajustes_menu.ui', self)

        # connect events
        self.atras_pushbutton.clicked.connect(self.go_back)

        self.show()

    def go_back(self):
        self.switch_back.emit()
        self.close()