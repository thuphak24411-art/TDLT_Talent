from PyQt6.QtWidgets import QMessageBox
from Chapter5.ex82.libs.my_module import calc_bill
from Chapter5.ex82.ui.KwhMainWindow import Ui_MainWindow


class KwhMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.process_bill)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonExit.clicked.connect(self.exit)
    def process_bill(self):
        group=""
        try:
            old=float(self.oldKWhLineEdit.text())
            new=float(self.newKWhLineEdit.text())
            if self.radioButtonPrepaid.isChecked():
                group = "prepaid"
            elif self.radioButtonNoPrepaid.isChecked():
                group = "no_prepaid"
            bill = calc_bill(old, new, group)
            self.billVNDLineEdit.setText(str(bill))
        except Exception as error:
            errBox = QMessageBox()
            errBox.setWindowTitle("Error")
            errBox.setText(str(error))
            errBox.setIcon(QMessageBox.Icon.Critical)
            errBox.exec()
    def process_clear(self):
        self.oldKWhLineEdit.setText("")
        self.newKWhLineEdit.setText("")
        self.radioButtonPrepaid.setEnabled(False)
        self.radioButtonPrepaid.setEnabled(False)
        self.billVNDLineEdit.setText("")
        self.oldKWhLineEdit.setFocus()
    def exit(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Muốn thoát hả?")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret = msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)
