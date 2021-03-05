from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: blacks;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 510, 120, 30))
        self.pushButton.setStyleSheet("background-color:#FF0000;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 510, 120, 30))
        self.pushButton_2.setStyleSheet("background-color:#FF0000;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 560, 120, 30))
        self.pushButton_3.setStyleSheet("background-color:#FF0000;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 510, 100, 40))
        self.pushButton_4.setStyleSheet("background-color:#FF0000;\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.pushButton_4.setObjectName("pushButton_4")

#        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
#        self.pushButton_5.setGeometry(QtCore.QRect(500, 510, 40, 40))
#        self.pushButton_5.setStyleSheet("background-color:#FF0000;\n"
#"font: 75 14pt \"Comic Sans MS\";")
#        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 510, 90, 40))
        self.pushButton_6.setStyleSheet("background-color:#FF0000;\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.pushButton_6.setObjectName("pushButton_6")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 400, 500, 35))
        self.lineEdit.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 450, 200, 35))
        self.lineEdit_2.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_2.setPlaceholderText("IP")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 450, 100, 35))
        self.lineEdit_3.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_3.setPlaceholderText("Port")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 450, 120, 35))
        self.lineEdit_4.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_4.setPlaceholderText("Speed")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 580, 360))
        self.textEdit.setStyleSheet("background: white; font-size: 25px;")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mdrive"))
        self.pushButton.setText(_translate("Dialog", "Connection"))
        self.pushButton_2.setText(_translate("Dialog", "Send"))
        self.pushButton_3.setText(_translate("Dialog", "EXIT"))
        self.pushButton_4.setText(_translate("Dialog", "START"))
        #self.pushButton_5.setText(_translate("Dialog", ">"))
        self.pushButton_6.setText(_translate("Dialog", "STOP"))
