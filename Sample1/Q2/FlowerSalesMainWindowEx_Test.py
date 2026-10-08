import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from Sample_Midterm.Midterm1.Q2UI.FlowerSalesMainWindowEx import FlowerSalesMainWindowEx

app=QApplication(sys.argv)
myui=FlowerSalesMainWindowEx()
myui.setupUi(QMainWindow())
myui.showWindow()
app.exec()