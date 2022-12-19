# Atividade final de Alex'
import os
import random
from sys import path
import click
import kivy
from kivy.network.urlrequest import UrlRequest

from csv import reader
from PyQt5 import QtCore, QtGui, QtWidgets
from kivy.lang import Builder


class Ui_Atualizar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 551)
        MainWindow.setStyleSheet("background-color: rgb(230, 150, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(65, 105, 255);\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 15px;\n"
                                      "border-color: black;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 15px;\n"
                                    "border-style: outset;\n"
                                    "border-width: 2px;")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 260, 31, 31))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("upload.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 0, 61, 51))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("marcaifms.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "upload"))
        self.lineEdit.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "camera"))

    # INSERINDO A AÇÃO "AO CLIAR NO BOTAO DE UPLOAD, VAI PARA A CÂMERA"

    kivy.require('2.1.0')

    path = "./../../ultimate_TETI/static/upload"

    def build(self):
        return Builder.load_file("tela_chat.kv")

    def new_conversation(self):
        room_key = random.randint(10, 1000)
        os.mkdir(f"{path}/{room_key}")
        self.root.ids['idsala'].text = f'o codigo da sala é {room_key}'

        return

    def join_room(self):
        cod_room = self.ids.root['inpt_codigo_room'].text
        NEWPATH = f'{path}/{cod_room}'
        if os.path.exists(NEWPATH):
            print("existe")
            return {"message": True}
        print("not existe")
        return {"message": False}


'''        
    @click.command()
    def picture():
        click.echo('retranslateUi')
'''

#       return reader("./../../ultimate_TETI/main.py")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Atualizar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())