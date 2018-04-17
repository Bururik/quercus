import sys
import qdarkstyle
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle('PyQt Tutorial')
		self.setWindowIcon(QtGui.QIcon('logo1.png'))

		#=========Menu Bar & Status Bar================#
		extractAction = QtWidgets.QAction('&GET TO THE CHOPPA!!', self)
		extractAction.setShortcut('Ctrl+Q')
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		#=============================================#

		self.home()

	def home(self):
		#===========Quit Button========================#
		btn = QtWidgets.QPushButton('Quit', self)
		btn.clicked.connect(self.close_application)
		# btn.resize(btn.sizeHint())
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)
		#=============================================#

		#=======Tool bar button & Font Widget==========#
		extractAction = QtWidgets.QAction(QtGui.QIcon('UNSC_Logo.png'),'Flee the scene', self)
		extractAction.triggered.connect(self.close_application)
		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)

		fontChoice = QtWidgets.QAction('Font', self)
		fontChoice.triggered.connect(self.font_choice)
		'''This second instance of 'Font' can separate the 
		other toolbar choice to their own individual
		modular toolbars'''
		# self.toolBar = self.addToolBar('Font')
		self.toolBar.addAction(fontChoice)
		#==============================================#

		#===========Resize Toggle Check Box============#
		checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
		checkBox.move(100,25)
		#checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)
		#=============================================#

		#=================Progress Bar=================#
		self.progress = QtWidgets.QProgressBar(self)
		self.progress.setGeometry(200,80,250,20)

		self.btn = QtWidgets.QPushButton('Download', self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		#=============================================#

		#==========Drop Down & Styles=======================#
		'''The problem here is that the default selection is 
		not already selected in teh dropdown
		eg. 'fusion' is the default in the current linux
		build but the first one shown is windows, because it
		is the first one in the list'''
		# print(self.style().objectName())
		self.styleChoice = QtWidgets.QLabel(self.style().objectName(),self)

		comboBox = QtWidgets.QComboBox(self)
		# comboBox.addItem('motif')
		comboBox.addItem('Windows')
		# comboBox.addItem('cde')
		# comboBox.addItem('plastique')
		# comboBox.addItem('Cleanlooks')
		# comboBox.addItem('windowsvista')
		comboBox.addItem('fusion')

		comboBox.move(50,250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		#=============================================#

		self.show()

	def font_choice(self):
		font, valid = QtWidgets.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)

	def style_choice(self,text):
		self.styleChoice.setText(text)
		QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))


	def download(self):
		self.completed = 0

		while self.completed < 100:
			self.completed +=0.0001
			self.progress.setValue(self.completed)

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
			app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
		else:
			self.setGeometry(50,50,500,300)
			app.setStyleSheet('')

	def closeEvent(self, event):      # user clicked the x or pressed alt-F4...

		programname = os.path.basename(__file__)
		programbase, ext = os.path.splitext(programname)  # extract basename and ext from filename
		settings = QtCore.QSettings("company", programbase)    
		settings.setValue("geometry", self.saveGeometry())  # save window geometry
		settings.setValue("state", self.saveState(UI_VERSION))   # save settings (UI_VERSION is a constant you should increment when your UI changes significantly to prevent attempts to restore an invalid state.)

		settings.setValue("checkBoxReplace", self.checkBoxReplace.checkState());
		settings.setValue("checkBoxFirst", self.checkBoxFirst.checkState());

		settings.setValue("radioButton1", self.radioButton1.isChecked());

		sys.exit()  # prevents second call

	def close_application(self):
		choice = QtWidgets.QMessageBox.question(self,'Execute!', 'Kill All the Humans?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if choice == QtWidgets.QMessageBox.Yes:
			print('Extermination commencing...\nHave a nice day! ;)')
			sys.exit()
		else:
			pass



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	# app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	GUI = Window()
	sys.exit(app.exec_())

