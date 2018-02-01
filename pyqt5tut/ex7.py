import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle('PyQt Tutorial')
		self.setWindowIcon(QtGui.QIcon('logo1.png'))

		extractAction = QtWidgets.QAction('&GET TO THE CHOPPA!!', self)
		extractAction.setShortcut('Ctrl+Q')
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QtWidgets.QPushButton('Quit', self)
		btn.clicked.connect(self.close_application)
		# btn.resize(btn.sizeHint())
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)

		extractAction = QtWidgets.QAction(QtGui.QIcon('UNSC_Logo.png'),'Flee the scene', self)
		extractAction.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)

		self.show()

	def close_application(self):
		choice = QtWidgets.QMessageBox.question(self,'Execute!', 'Kill All the Humans?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			print('Extermination commencing...\nHave a nice day! ;)')
			sys.exit()
		else:
			pass



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

