import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget(0 , 0, 500, 300)
window.setWindowTitle('tuts!')

window.show()

