from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 650)
        Dialog.setStyleSheet("background-color: green;")

# Подключение к устройству (connection)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 570, 120, 35))
        self.pushButton.setStyleSheet("background-color:#A62D00;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")

# Отправление запроса (Send)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 520, 120, 35))
        self.pushButton_2.setStyleSheet("background-color:#BF5730;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton_2.setObjectName("pushButton_2")

# Отключение от устройства (EXIT)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 570, 120, 35))
        self.pushButton_3.setStyleSheet("background-color:#A62D00;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton_3.setObjectName("pushButton_3")

# Направление вверх (👆)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 400, 40, 40))
        self.pushButton_4.setStyleSheet("background-color:#BF5730;\n"
"font: 75 15pt \"Comic Sans MS\";")
        self.pushButton_4.setObjectName("pushButton_4")

# Направление вправо (👉)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 450, 40, 40))
        self.pushButton_5.setStyleSheet("background-color:#BF5730;\n"
"font: 75 15pt \"Comic Sans MS\";")
        self.pushButton_5.setObjectName("pushButton_5")

# Остановка движения (█)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 450, 40, 20))
        self.pushButton_6.setStyleSheet("background-color:#BF5730;\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.pushButton_6.setObjectName("pushButton_6")

# Движение влево (👈)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 450, 40, 40))
        self.pushButton_7.setStyleSheet("background-color:#BF5730;\n"
"font: 75 15pt \"Comic Sans MS\";")
        self.pushButton_7.setObjectName("pushButton_5")

# Движение вниз (👇)
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 500, 40, 40))
        self.pushButton_8.setStyleSheet("background-color:#BF5730;\n"
"font: 75 15pt \"Comic Sans MS\";")
        self.pushButton_8.setObjectName("pushButton_5")

# Остановка движения (█)
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 470, 40, 20))
        self.pushButton_9.setStyleSheet("background-color:#BF5730;\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.pushButton_9.setObjectName("pushButton_6")

#
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.insertPlainText("Порт")
        self.textEdit.setGeometry(QtCore.QRect(10, 400, 70, 30))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.insertPlainText("Адрес")
        self.textEdit_2.setGeometry(QtCore.QRect(10, 440, 70, 30))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.insertPlainText("Имя")
        self.textEdit_3.setGeometry(QtCore.QRect(10, 480, 70, 30))
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.insertPlainText("Запрос")
        self.textEdit_4.setGeometry(QtCore.QRect(10, 520, 70, 35))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.insertPlainText("PY")
        self.textEdit.setGeometry(QtCore.QRect(260, 400, 30, 30))
        self.textEdit.setObjectName("textEdit")

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(295, 405, 20, 20))
        self.checkBox.setObjectName("checkBox")

#        self.comboBox = QtWidgets.QComboBox(Dialog)
#        self.comboBox.setGeometry(QtCore.QRect(510, 450, 70, 35))
#        self.comboBox.setStyleSheet("background-color: white;")
#        self.comboBox.setObjectName("white")
#        self.comboBox.addItem("")
#        self.comboBox.addItem("")

# Поле для заполнения запроса
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(95, 520, 155, 35))
        self.lineEdit.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit.setPlaceholderText("#X PR AL")
        self.lineEdit.setObjectName("lineEdit")

# Поле для ip
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(95, 440, 155, 35))
        self.lineEdit_2.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_2.setPlaceholderText("192.168.0.7")
        self.lineEdit_2.setObjectName("lineEdit_2")

# Поле для port'a
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(95, 400, 155, 35))
        self.lineEdit_3.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_3.setPlaceholderText("5000")
        self.lineEdit_3.setObjectName("lineEdit_3")

# Поле для скорости
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 520, 120, 35))
        self.lineEdit_4.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_4.setPlaceholderText("Speed")
        self.lineEdit_4.setObjectName("lineEdit_4")

# Поле для заполнения запроса
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(95, 480, 155, 35))
        self.lineEdit_5.setStyleSheet("background-color: white; font-size: 25px;")
        self.lineEdit_5.setPlaceholderText("X")
        self.lineEdit_5.setObjectName("lineEdit")

# Поле вывода
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 580, 360))
        self.textEdit.setStyleSheet("background: white; font-size: 25px;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mdrive"))
        self.pushButton.setText(_translate("Dialog", "Connection"))
        self.pushButton_2.setText(_translate("Dialog", "Send"))
        self.pushButton_3.setText(_translate("Dialog", "EXIT"))
        self.pushButton_4.setText(_translate("Dialog", "👆"))
        self.pushButton_5.setText(_translate("Dialog", "👉"))
        self.pushButton_6.setText(_translate("Dialog", "█"))
        self.pushButton_7.setText(_translate("Dialog", "👈"))
        self.pushButton_8.setText(_translate("Dialog", "👇"))
        self.pushButton_9.setText(_translate("Dialog", "█"))

#        self.comboBox.setItemText(0, _translate("Dialog", "X"))
#        self.comboBox.setItemText(1, _translate("Dialog", "Y"))
