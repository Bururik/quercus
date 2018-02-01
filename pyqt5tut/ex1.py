import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setGeometry(500,0,500,300)
window.setWindowTitle('tuts!!!')

window.show()
sys.exit(app.exec_())
