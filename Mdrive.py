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
    except:
        prnt("Ошибка, проверьте правильность данных.")
ui.pushButton.clicked.connect( connections )

# Функция для занесения данных в textEdit
def prnt(s):
    ui.textEdit.insertPlainText(s)

# Отправление запроса двигателю.
def send():
    try:
        prnt("Запрос отправлен \n")
        prnt(drive(ui.lineEdit_5.text(), ui.lineEdit.text()))
    except:
        prnt("\nПроверьте правильность команды. \n")
ui.pushButton_2.clicked.connect( send )


# Запрос двигателю
def drive(name, cmd, speed = '', timeout = 0.03):
        try:
            s.send("\n".encode("utf-8") + name.encode("utf-8") + cmd.encode("utf-8") + speed.encode("utf-8") + "\n".encode("utf-8"))
            this.socket.setSoTimeout(timeOut)
            time.sleep(timeout)
            otvet = s.recv(1024)
            return otvet
        except:
            return "\nУстройство не подключено\n"


#Движение по оси -x
def left():
    drive("X", " SL -", ui.lineEdit_4.text())
ui.pushButton_4.clicked.connect( left )

#Движение по оси +y
def up():
    drive("Y", " SL ", ui.lineEdit_4.text())
ui.pushButton_5.clicked.connect( up )

#Движение по оси +x
def right():
    drive("X", " SL ", ui.lineEdit_4.text())
ui.pushButton_7.clicked.connect( right )

#Движение по оси -y
def down():
    drive("Y", " SL -", ui.lideEdit_4.text())
ui.pushButton_8.clicked.connect( down )

# Остановка двигателя
def STOPX():
    drive("X", " SL", ui.lineEdit_4)
ui.pushButton_6.clicked.connect( STOPX )

# Остановка двигателя
def STOPY():
    drive("Y", " SL 0", ui.lideEdit_4)
ui.pushButton_9.clicked.connect( STOPY )

def exit():
    try:
        s.close()
    except:
        prnt("\nВы не подключены к устройству\n")
#Отключение от сокета
def EXIT():
    exit(prnt("\nВы отключились от устройства. \n"))
ui.pushButton_3.clicked.connect( EXIT )

app.exec()
