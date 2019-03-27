import sys
import socket
import threading
from PySide.QtCore import *
from PySide.QtGui import *
class Connect():
    def __init__(self,g):
        self.host="localhost"
        self.port=4990
        self.file_out=open(g.output_path+"/test.p","w+")
        thread=threading.Thread(target=self.serverWork,args=())
        thread.start()
    def serverWork(self):
        self.conn=socket.socket()
        self.conn.bind((self.host,self.port))
        self.conn.listen(5)
        print("Server is working")
        while True:
            stream,ip=self.conn.accept()
            print ip
            while True:

                data=stream.recv(1024)
                while(data):
                    self.file_out.write(data)
                    data=stream.recv(1024)
                self.file_out.close()
            stream.close()
        s.close()

class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.output_path="/home/"
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Server")
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.directory_button=QPushButton(self)
        self.directory_button.setText("Select Directory")
        self.directory_button.resize(150,50)
        self.directory_button.move(300,250)
        self.directory_button.clicked.connect(self.setDirectory)
        self.path=QLabel(self)
        self.path.setText(self.output_path)
        self.path.resize(200,20)
        self.path.move(50,275)
        self.directory_button.show()
        self.path.show()
        self.show()
    def setDirectory(self):
        self.output_path=QFileDialog.getExistingDirectory(self,"Select Directory","/home/",QFileDialog.ShowDirsOnly)
        self.path.setText(self.output_path)
        s=Connect(self)
app = QApplication(sys.argv)
gui=GUI()
sys.exit(app.exec_())
