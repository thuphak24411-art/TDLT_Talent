import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Homework.Ex109.ui.DepreciationMainWindowEx import DepreciationMainWindowEx

app=QApplication(sys.argv)
myui=DepreciationMainWindowEx()
myui.setupUi(QMainWindow())
myui.showWindow()
app.exec()