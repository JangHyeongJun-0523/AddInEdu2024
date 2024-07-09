import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QRegExp
import socket

from_class = uic.loadUiType("09_TCP_SocketClientGUI.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]25[0-5])"
        ipRegex = QRegExp("^" + range + "\\." + range + "\\." + \
                          range + "\\." + range + "$")
        
        self.ipEdit.setValidator(QRegExpValidator(ipRegex, self))
        self.portEdit.setValidator(QIntValidator())
        self.setWindowTitle("TCP Client")
        self.ConnectBtn.clicked.connect(self.connect)

    def connect(self):
        ip = self. ipEdit.text()
        port = self.portEdit.text()
        
        self.sock = socket.socket()
        self.sock.connect((ip, int(port)))
        self.sock.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())