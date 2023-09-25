# 1. import needed QtWidgets classes
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from UI.calculator import Ui_MyMainWindow

# 2. the main app instance for our application.
app = QApplication([])

# 3. Create Qt widget, which will be our main window.
window = QMainWindow()
Main = Ui_MyMainWindow()
Main.setupUi(window)

# 4. show the window
window.show()
app.exec()