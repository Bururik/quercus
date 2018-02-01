import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget, QPushButton, QComboBox, QRadioButton, \
QVBoxLayout, QCheckBox, QHBoxLayout, QGroupBox, QDialog
from PyQt5.QtGui import QIcon

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 500
        self.title = 'Chip2 Torque Data'
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.main_layout = QVBoxLayout()

        xselect=QRadioButton("X",self)
        xselect.setChecked(True)
        # xselect.move(340,400)
        self.main_layout.addWidget(xselect)

        zselect=QRadioButton("Z",self)
        # zselect.move(380,400)
        self.main_layout.addWidget(zselect)

        sselect=QRadioButton("SP1",self)
        # sselect.move(420,400)
        self.main_layout.addWidget(sselect)



        pass_list=QComboBox(self)
        pass_list.addItems(sheets_idealcut)
        self.main_layout.addWidget(pass_list)
        #pass_list.move(340,300)
        rawdata_check=QCheckBox("Raw Data",self)
        rawdata_check.setChecked(True)
        self.main_layout.addWidget(rawdata_check)
        #rawdata_check.move(340,200)
        mvgavg_check=QCheckBox("Moving average",self)
        mvgavg_check.setChecked(True)
        #mvgavg_check.move(380,200)
        mvgstd_check=QCheckBox("Moving stdev",self)
        mvgstd_check.setChecked(True)
        #mvgstd_check.move(420,200)

        self.check_group = QHBoxLayout()
        self.check_group.addWidget(mvgavg_check)
        self.check_group.addWidget(mvgstd_check)
        self.check_group.stretch(1)

        self.main_layout.addLayout(self.check_group)
        self.setLayout(self.main_layout)
        self.show()

if __name__ == '__main__':
    sheets_idealcut=['pass2','pass3','pass4','pass5']

    app = QApplication.instance()
    if app is None:
         app = QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    ex = App()
    #ex.show()
    app.exec_()