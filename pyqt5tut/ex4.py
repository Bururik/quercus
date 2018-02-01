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
		btn.clicked.connect(self.close_application)
		# btn.resize(btn.sizeHint())
		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)
		self.show()

	def close_application(self):
		print("Whoooooop!")
		sys.exit()
		# self.setWindowTitle("Please....Kill me")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

