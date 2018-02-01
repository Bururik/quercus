import sys
import os
from PyQt5 import QtWidgets, QtGui

# app = QtWidgets.QApplication(sys.argv)

# window = QtWidgets.QWidget()

# window.setGeometry(500,0,500,300)
# window.setWindowTitle('tuts!!!')

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle('PyQt Tutorial')
		self.setWindowIcon(QtGui.QIcon('logo1.png'))
		self.show()

app = QtWidgets.QApplication(sys.argv)

GUI = Window()

sys.exit(app.exec_())
