from Chapter5.ex73.libs.my_module import calculate
from Chapter5.ex73.ui.MyMainWindow import Ui_MainWindow

class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.quadracticEquation)
    def quadracticEquation(self):
        a=float(self.aLineEdit.text())
        b=float(self.bLineEdit.text())
        c=float(self.cLineEdit.text())
        self.resultLineEdit.setText(calculate(a,b,c))
