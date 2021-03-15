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

#Подключение к двигателю
def connections():
    try:
        global s
        #ip = ui.lineEdit_2.text()
        #port = ui.lineEdit_3.text()
        s = socket.socket(socket.AF_INET)
        s.settimeout(1)
        s.connect(('192.168.0.7', 5000))

        s.setblocking(True)
        prnt("Подключились к сокету")
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
        name = ui.lineEdit_5.text()
        s.send("\n".encode("utf-8") + name.encode("utf-8") + text.encode("utf-8") + "\n".encode("utf-8"))
        this.socket.setSoTimeout(timeOut)
        time.sleep(0.5)
        data = s.recv(1024)
        prnt ( "\n" + str(data.decode()) + "\n")
        prnt("Запрос отправлен \n")
    except:
        prnt("\nПроверьте правильность команды. \n")

ui.pushButton_2.clicked.connect( send )

#Движение по оси -x
def left():
    try:
        global Speed
        Speed = ui.lineEdit_4.text()
        s.send("\n".encode("utf-8") + "X SL -".encode("utf-8") + Speed.encode("utf-8") + "\n".encode("utf-8"))
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение началось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_4.clicked.connect( left )

#Движение по оси +y
def up():
    try:
        s.send("\n".encode("utf-8") + "Y SL ".encode("utf-8") + Speed.encode("utf-8") + "\n".encode("utf-8"))
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение началось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_5.clicked.connect( up )

#Движение по оси +x
def right():
    try:
        s.send("\n".encode("utf-8") + "X SL ".encode("utf-8") + Speed.encode("utf-8") + "\n".encode("utf-8"))
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение началось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_7.clicked.connect( right )

#Движение по оси -y
def down():
    try:
        s.send("\n".encode("utf-8") + "Y SL -".encode("utf-8") + Speed.encode("utf-8") + "\n".encode("utf-8"))
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение началось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_8.clicked.connect( down )

# Остановка двигателя
def STOPX():
    try:
        s.send(b"\nX SL 0\n")
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение остановилось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_6.clicked.connect( STOPX )

# Остановка двигателя
def STOPY():
    try:
        s.send(b"\nY SL 0\n")
        otvet = s.recv(1024)
        prnt ( "\n" + str(otvet) + "\n")
        prnt("\nДвижение остановилось\n")
    except:
        prnt("\nУстройство не подключено\n")

ui.pushButton_9.clicked.connect( STOPY )

#Отключение от сокета
def EXIT():
    try:
        s.close()
        prnt("\nВы отключились от устройства. \n")
    except:
        prnt("\nВы не подключены к устройству\n")
ui.pushButton_3.clicked.connect( EXIT )

app.exec()
