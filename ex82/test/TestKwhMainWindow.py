import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Chapter5.ex82.ui.KwhMainWindowEx import KwhMainWindowEx

app=QApplication(sys.argv)
myui=KwhMainWindowEx()
myui.setupUi(QMainWindow())
myui.showWindow()
app.exec()