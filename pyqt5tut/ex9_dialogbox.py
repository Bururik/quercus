import time
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

		checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
		checkBox.move(100,25)
		# checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)

		self.progress = QtWidgets.QProgressDialog(self)
		self.progress.setGeometry(200,80,250,20)

		self.btn = QtWidgets.QPushButton('Download', self)
		self.btn.move(200,120)
		# self.btn.clicked.connect(self.download)
		self.btn.clicked.connect(self.dialog)
		self.progress.hide()
		self.show()


	def dialog(self):
		self.progress.setWindowTitle('ProgressDialog')
		self.progress.setLabelText('ProgressDialog to indicate the status of a process...')

		'''This gives the minimum length of time for a diolog box to appear
		although the title and progression of the bar do now appear'''
		# self.progress.setMinimumDuration(800)

		# self.progress.setCancelButton(None)
		# self.progress.setRange(0, 100)
		# self.progress.canceled.connect(self.close)

# NOTE:the following two for loops do essentially the same thing
		for count in range(self.progress.minimum(), self.progress.maximum() + 1):
			self.progress.setValue(count)
			'''important for the progress bar to 
			progress are the following two methods
			more research is needed to determine
			their functions'''
			QtWidgets.qApp.processEvents()
			time.sleep(0.05)

		# for count in range(0,100):
		# 	self.progress.setValue(count)
		# 	QtWidgets.qApp.processEvents()
		# 	time.sleep(0.05)


		self.progress.show()
		''' without this second method we will simply 
		generate another empty 'download' window'''
		self.progress.hide()

	def download(self):
		count = 0
		
		while count < 100:
			count +=0.001
			self.progress.setValue(33)



	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(50,50,500,300)

	def close_application(self):
		choice = QtWidgets.QMessageBox.question(self,'Execute!', 'Kill All the Humans?\n poopoopoooooo\n dieeeeeee',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			print('Extermination commencing...\nHave a nice day! ;)')
			sys.exit()
		else:
			pass



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

