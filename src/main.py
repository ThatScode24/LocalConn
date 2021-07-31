from PyQt5 import QtCore, QtGui, QtWidgets
import socket

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 280)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.connWindow = QtWidgets.QWidget(MainWindow)
        self.connWindow.setObjectName("connWindow")
        self.NickName = QtWidgets.QPlainTextEdit(self.connWindow)
        self.NickName.setGeometry(QtCore.QRect(50, 90, 161, 31))
        self.NickName.setObjectName("NickName")
        self.Connect = QtWidgets.QPushButton(self.connWindow)
        self.Connect.setGeometry(QtCore.QRect(80, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Connect.setFont(font)
        self.Connect.setObjectName("Connect")
        self.NickName_2 = QtWidgets.QPlainTextEdit(self.connWindow)
        self.NickName_2.setGeometry(QtCore.QRect(50, 30, 161, 31))
        self.NickName_2.setObjectName("NickName_2")
        MainWindow.setCentralWidget(self.connWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #when button is pressed 
        def process_connection():
            nickname = self.NickName.toPlainText()
            ip = self.NickName_2.toPlainText()
            self.NickName_2.clear()
            self.NickName.clear()
            ADDR = (f'{ip}', PORT)
            print(ADDR)
            client.connect(ADDR)
            msg = nickname
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Connect.clicked.connect(process_connection)  #sets connect button action


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Connection", "Connection"))
        self.Connect.setText(_translate("MainWindow", "Connect"))

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
