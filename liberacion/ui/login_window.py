from PyQt5 import QtWidgets, uic
from service import UsuarioService


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('design/login_window.ui', self)

        # connect events
        self.acceder_pushbutton.clicked.connect(self.access)

        self.show()

    def access(self):
        alias = self.alias_lineedit.text()
        contrasena = self.contrasena_lineedit.text()

        if alias and contrasena:
            usuario = UsuarioService.get_by_alias(alias)
            if usuario:
                if usuario.contrasena == contrasena:
                    print('Go to Main Menu ...')
                else:
                    print('Incorrect password')
            else:
                print('User not found')
        else:
            print('Empty fields')