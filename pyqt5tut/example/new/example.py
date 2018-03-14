#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.

Requirements:
    - Python 2 or Python 3
    - PyQt4, PyQt5 or PySide
    - QtPy or PyQtGraph (if necessary)

Running:

python example.py --qt_from=pyside (or any other available)

To see all options for starting this example, run:

python example --help

.. note.. :: qdarkstyle does not have to be installed to run the example.

"""

import logging
import sys
import argparse

import qdarkstyle

# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qt_from', default='pyqt5',
                        choices=['pyqt', 'pyqt5', 'pyside', 'qtpy', 'pyqtgraph'],
                        help="Choose which wrapper/framework is to be used to run the example.", type=str)
    parser.add_argument('--no_dark', action='store_true',
                        help="Exihibts the original (without qdarkstyle) window.")

    # parsing arguments from command line
    args = parser.parse_args()

    # set log for debug
    logging.basicConfig(level=logging.DEBUG)
    
    if args.qt_from == 'pyqt5':
        # using PyQt5 wrapper
        from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
        from PyQt5.QtCore import QTimer, Qt
        # import examples UI according to wrapper
        from ui.mw_views_widgets_containers_pyqt5_ui import Ui_MainWindow as ui_main
        from ui.dw_buttons_pyqt5_ui import Ui_DockWidget as ui_buttons
        from ui.dw_displays_pyqt5_ui import Ui_DockWidget as ui_displays
        from ui.dw_inputs_fields_pyqt5_ui import Ui_DockWidget as ui_inputs
        from ui.dw_inputs_no_fields_pyqt5_ui import Ui_DockWidget as ui_inputs_no_fields
        # getting style
        style = qdarkstyle.load_stylesheet_pyqt5()

    if args.no_dark:
        style = ''

    # create the application
    app = QApplication(sys.argv)

    # setup stylesheet
    app.setStyleSheet(style)

    # create main window
    window = QMainWindow()
    ui = ui_main()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle Example - Using " + args.qt_from)

    # # create docks for buttons
    # dw_buttons = QDockWidget()
    # ui_buttons = ui_buttons()
    # ui_buttons.setupUi(dw_buttons)
    # window.addDockWidget(Qt.RightDockWidgetArea, dw_buttons)

    # # create docks for displays
    # dw_displays = QDockWidget()
    # ui_displays = ui_displays()
    # ui_displays.setupUi(dw_displays)
    # window.addDockWidget(Qt.RightDockWidgetArea, dw_displays)

    # # create docks for inputs - fields
    # dw_inputs = QDockWidget()
    # ui_inputs = ui_inputs()
    # ui_inputs.setupUi(dw_inputs)
    # window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs)

    # # create docks for inputs - no fields
    # dw_inputs_no_field = QDockWidget()
    # ui_inputs_no_field = ui_inputs_no_fields()
    # ui_inputs_no_field.setupUi(dw_inputs_no_field)
    # window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_no_field)

    # # tabify docks
    # window.tabifyDockWidget(dw_buttons, dw_displays)
    # window.tabifyDockWidget(dw_displays, dw_inputs)
    # window.tabifyDockWidget(dw_inputs, dw_inputs_no_field)

    # run
    # window.showMaximized()
    window.show()
    app.exec_()

if __name__ == "__main__":
    sys.exit(main())
