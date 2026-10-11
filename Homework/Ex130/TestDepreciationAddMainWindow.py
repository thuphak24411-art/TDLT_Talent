import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Homework.Ex130.ui.DepreciationAddMainWindowEx import DepreciationAddMainWindowEx

app=QApplication(sys.argv)
myui=DepreciationAddMainWindowEx()
myui.setupUi(QMainWindow())
myui.showWindow()
app.exec()