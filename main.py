from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import subprocess
import sys
import re

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('layout.ui', self)
		self.show()
		self.buka.clicked.connect(self.getfile)
		self.exe.clicked.connect(self.exect)
		self.lok = ""
	def getfile(self):
		fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 
         '/home',"Python Files (*.py);;All Files (*)")
		setLokasi = self.lokasi.setText(str(fname))
		opn = open(fname,"r")
		baca = opn.read()
		self.kode.setText(baca)
		self.lok += fname
		
	def debg(self,st):
		dbg = self.debug.setText(str(st))
		
	def exect(self):
		self.x = subprocess.run(["2to3","-w",self.lok],capture_output=True)
		self.bersih = str(self.x).replace("CompletedProcess","").replace("(","[").replace(")","]").split(",")
		self.debg(self.bersih[5].replace("stderr=b'","").replace("\\n","\n").replace("']",""))
		opn = open(self.lok,"r")
		baca = opn.read()
		self.kode.setText(baca)
      
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

