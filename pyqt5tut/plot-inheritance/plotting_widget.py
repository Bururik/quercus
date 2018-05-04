import sys

import qdarkstyle
import numpy as np 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon


class PlotingWidget(QWidget):
    def __init__(self):
        super(PlotingWidget, self).__init__()
        self.initUI()

    def initUI(self):
        # window geometry
        self.setGeometry(600, 300, 1000, 600)
        self.center()
        self.setWindowTitle('ChemView Plot')

        # layout 
        grid = QGridLayout()
        self.setLayout(grid)

        # temporary plot button
        btn = QPushButton('Display Plot', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.plot)
        grid.addWidget(btn, 2, 0)

        # window layout
        self.figure = plt.figure(figsize=(15,5))
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        grid.addWidget(self.canvas, 1,0,1,2)
        grid.addWidget(self.toolbar, 0,0,1,2)

        self.show()

    def plot(self):
        # NOTE: what does this do?
        plt.cla()
        ax = self.figure.add_subplot(111)
        # ======================= #
        
        # TODO: temporary variables (passed in)
        a_r = (2.25)*(10**(-40))
        b_r = 6.46
        e_r = 34184.0
        # =================== # 

        x = np.linspace(300, 27000, 1000000) # TODO: try not hard coding this....
        var1 = a_r * x**(b_r)
        var2 = np.exp(-(e_r/x))
        y = var1 * var2

        ax.plot(x, y, 'b.-')
        ax.set_title(' E  +  NF3 -> NF2+  +  F  +  2E') # TODO: this also shouldn't be hard coded...

        self.canvas.draw()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    style = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(style)
    w = PlotingWidget()
    app.exec_()

if __name__ == '__main__':
    main()