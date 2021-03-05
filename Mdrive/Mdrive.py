import sys
import socket
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from MdriveGUI import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#ip = ui.lineEdit_2.text()
#port = ui.lineEdit_3.text()

#Подключение к двигателю
def connections():
    try:
        global s
        s = socket.socket(socket.AF_INET)
        s.connect(('192.168.0.7', 5000))
        s.setblocking(False)
        prnt("Подключились к сокету.")
    except:
        prnt("Ошибка, проверьте правильность данных.")
ui.pushButton.clicked.connect( connections )

# Функция для занесения данных в textEdit
def prnt(s):
    ui.textEdit.insertPlainText(s)

# Отправление запроса двигателю.
def send():
    try:
        text = ui.lineEdit.text()
        s.send("\n".encode("utf-8") + text.encode("utf-8") + "\n".encode("utf-8"))
        time.sleep(0.5)
        data = s.recv(1024)
        prnt ( "\n" + str(data) + "\n")
        prnt("\nЗапрос отправлен \n")
    except:
        prnt("\nПроверьте правильность команды \n")

ui.pushButton_2.clicked.connect( send )

#Движение двигателя влево
def left():
    Speed = ui.lineEdit_4.text()
    s.send('\nX SL '.encode("utf-8") + Speed.encode("utf-8") + '\n'.encode("utf-8"))
    prnt("\nДвижение началось\n")

ui.pushButton_4.clicked.connect( left )

#Движение двигателя вправо
#def right():
#    Speed = ui.lineEdit_4.text()
#    s.send('\nX SL'.encode("utf-8") + Speed.encode("utf-8") + '\n'.encode("utf-8"))
#    prnt("\nДвижение против часовой стрелки\n")

#ui.pushButton_5.clicked.connect( right )

def STOP():
    s.send(b'\nX SL 0\n')
    prnt("\nДвижение остановилось\n")

ui.pushButton_6.clicked.connect( STOP )

#Отключение от сокета
def EXIT():
    s.close()
    prnt("\nВы отключились от устройства. \n")

ui.pushButton_3.clicked.connect( EXIT )

app.exec()
