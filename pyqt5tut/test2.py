from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Example(QMainWindow):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self._show_progress()

    def _show_progress(self):
        self._progress = QProgressDialog('msg', None, 0, 0, self)
        self._progress.setWindowTitle('Please wait...')
        self._progress.setWindowModality(Qt.WindowModal)
        self._progress.show()

def main():
    app = QApplication(sys.argv)
    cb_app = Example()
    cb_app.show()
    app.exec_()

if __name__ == '__main__':
    main()