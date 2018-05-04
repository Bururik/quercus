import sys
import qdarkstyle
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('PyQt Tutorial')
        self.setWindowIcon(QtGui.QIcon('logo1.png'))

        #================Saving State==================#
        self.settings = QtCore.QSettings("plank", __file__)
        # del self.settings
        self.resize(self.settings.value("size"))
        self.move(self.settings.value("pos"))
        self.settings.value("style")
        #==============================================#

        #=========Menu Bar & Status Bar================#
        extractAction = QtWidgets.QAction('&GET TO THE CHOPPA!!', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtWidgets.QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QtWidgets.QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtWidgets.QAction('&Save File', self)
        saveFile.setShortcut('Ctrl+s')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)


        self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)


        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)
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

        #=============Tool bar button==================#
        extractAction = QtWidgets.QAction(QtGui.QIcon('UNSC_Logo.png'),'Flee the scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)
        # self.toolBar.hide()
        self.toolBar.addSeparator()

        # this thing takes away the toolbar toggle
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        #==============================================#

        #=================Font Widget===================#
        fontChoice = QtWidgets.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        '''This second instance of 'Font' can separate the 
        other toolbar choice to their own individual
        modular toolbars'''
        # self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontChoice)
        #==============================================#

        #===============Color Picker===================#
        color = QtGui.QColor(0,0,0)

        fontColor = QtWidgets.QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)
        #==============================================#

        #===========Resize Toggle Check Box============#
        self.checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        self.checkBox.move(300,50)
        if self.settings.value("style") == 'true':
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.checkBox.toggle()
        else: 
            app.setStyleSheet('')
        self.checkBox.stateChanged.connect(self.enlarge_window)
        print(self.settings.value("style"))
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
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista') # This is the default in my windows machine
        comboBox.addItem('Fusion')
        comboBox.addItem('windowsxp')
        comboBox.addItem('Macintosh')


        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)
        #==============================================#

        #===============Calendar=======================#
        cal = QtWidgets.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)
        #==============================================#

        self.show()

    def file_open(self):
        name,_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name,_ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}' % color.name())

    def editor(self):
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

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
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            app.setStyleSheet('')

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self,'Execute!', 'Kill All the Humans?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print('Extermination commencing...\nHave a nice day! ;)')
            sys.exit()
        else:
            pass

    def closeEvent(self, e):
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("style", self.checkBox.isChecked())
        e.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    
