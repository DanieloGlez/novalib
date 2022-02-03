import sys, os, util
from PyQt5 import QtCore, QtWidgets, uic
from service import UsuarioService


class Controller:
    def __init__(self):
        pass

    def show_main_window(self):
        self.main_window = MainContainer()
        self.main_window.show()


class MainContainer(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainContainer, self).__init__()
        uic.loadUi(os.path.join('design', 'main_container.ui'), self)

        # login
        self.acceder_pushbutton.clicked.connect(self.open_main_menu)
        # dynamic_container
        self.pager_stackedwidget.addWidget(LiberacionContainer())
        self.pager_stackedwidget.addWidget(ReportesContainer())
        self.pager_stackedwidget.addWidget(AdministracionContainer())
        self.pager_stackedwidget.addWidget(AjustesContainer())
        # main_menu/side_control 
        self.informacion_pushbutton.clicked.connect(self.open_informacion)
        self.liberacion_pushbutton.clicked.connect(self.open_liberacion)
        self.reportes_pushbutton.clicked.connect(self.open_reportes)
        self.administracion_pushbutton.clicked.connect(self.open_administracion)
        self.ajustes_pushbutton.clicked.connect(self.open_ajustes)

        self.show()

    def open_main_menu(self):
        alias = self.alias_lineedit.text()
        contrasena = self.contrasena_lineedit.text()

        if alias and contrasena:
            usuario = UsuarioService.get_by_alias(alias)
            if usuario:
                if usuario.contrasena == contrasena:
                    util.active_user = usuario
                    self.maincontainer_stackedwidget.setCurrentIndex(1)
                else:
                    print('Incorrect password')
            else:
                print('User not found')
        else:
            print('Empty fields')

    def open_informacion(self):
        self.tittle_label.setText('Información')
        self.pager_stackedwidget.setCurrentIndex(0)

    def open_liberacion(self):
        self.tittle_label.setText('Liberación de Lotes')
        self.pager_stackedwidget.setCurrentIndex(1)

    def open_reportes(self):
        self.tittle_label.setText('Reportes')
        self.pager_stackedwidget.setCurrentIndex(2)

    def open_administracion(self):
        self.tittle_label.setText('Administración de Datos')
        self.pager_stackedwidget.setCurrentIndex(3)

    def open_ajustes(self):
        self.tittle_label.setText('Ajustes')
        self.pager_stackedwidget.setCurrentIndex(4)
    

class LiberacionContainer(QtWidgets.QFrame):
    def __init__(self):
        super(LiberacionContainer, self).__init__()
        uic.loadUi(os.path.join('design', 'liberacion_container.ui'), self)


class ReportesContainer(QtWidgets.QFrame):
    def __init__(self):
        super(ReportesContainer, self).__init__()
        uic.loadUi(os.path.join('design', 'reportes_container.ui'), self)


class AdministracionContainer(QtWidgets.QFrame):
    def __init__(self):
        super(AdministracionContainer, self).__init__()
        uic.loadUi(os.path.join('design', 'administracion_container.ui'), self)


class AjustesContainer(QtWidgets.QFrame):
    def __init__(self):
        super(AjustesContainer, self).__init__()
        uic.loadUi(os.path.join('design', 'ajustes_container.ui'), self)
