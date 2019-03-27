import sys
import socket
from PySide.QtCore import *
from PySide.QtGui import *

class Connect:
    def __init__(self,g):
        self.host="localhost"
        self.port=4990
        conn=socket.socket()
        conn.connect((self.host,self.port))
        file=open(str(g.file_path[0]))
        stream=file.read(1024)
        while(stream):
            conn.send(stream)
            stream=file.read(1024)
        conn.close()
class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.file_path="/home/"
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Client")
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.file_button=QPushButton(self)
        self.file_button.setText("Select File")
        self.file_button.resize(150,50)
        self.file_button.move(300,250)
        self.file_button.clicked.connect(self.selectFile)
        self.upload_button=QPushButton(self)
        self.upload_button.setText("Upload")
        self.upload_button.resize(150,50)
        self.upload_button.move(300,50)
        self.upload_button.clicked.connect(self.upload)
        self.path=QLabel(self)
        self.path.setText(self.file_path)
        self.path.resize(200,20)
        self.path.move(50,275)
        self.status=QLabel(self)
        self.status.setText("")
        self.status.resize(200,20)
        self.status.move(50,50)
        self.file_button.show()
        self.upload_button.show()
        self.status.show()
        self.path.show()
        self.show()
    def selectFile(self):
        self.file_path=QFileDialog.getOpenFileName(self,"Select File","/home/")
        self.path.setText(str(self.file_path[0]))
        self.status.setText("Selected")
    def upload(self):
        self.status.setText("Uploading")
        self.c=Connect(self)
app = QApplication(sys.argv)
gui=GUI()
sys.exit(app.exec_())
