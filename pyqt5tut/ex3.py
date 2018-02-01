import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle('PyQt Tutorial')
		self.setWindowIcon(QtGui.QIcon('logo1.png'))
		self.home()

	def home(self):
		btn = QtWidgets.QPushButton("Quit", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(100,100)
		btn.move(100,100)
		self.show()

def main():
	app = QtWidgets.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

main()
