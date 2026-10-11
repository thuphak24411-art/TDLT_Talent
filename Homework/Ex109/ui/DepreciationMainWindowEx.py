from PyQt6.QtWidgets import QMessageBox
from Homework.Ex109.my_module import calc_depreciation
from Homework.Ex109.ui.DepreciationMainWindow import Ui_MainWindow

class DepreciationMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.process_depreciation)
    def process_depreciation(self):
        try:
            p=float(self.purchasePriceLineEdit.text())
            trans_free=float(self.transportationFeeLineEdit.text())
            install_fee=float(self.installationFeeLineEdit.text())
            years=int(self.yearsOfDepreciationLineEdit.text())
            original_price, annual_rate, monthly_rate = calc_depreciation(p, trans_free, install_fee, years)
            self.originalPriceLineEdit.setText(str(original_price))
            self.annualDepreciationRateLineEdit.setText(str(annual_rate))
            self.monthlyDepreciationRateLineEdit.setText(str(monthly_rate))
        except Exception as error:
            errBox = QMessageBox()
            errBox.setWindowTitle("Error")
            errBox.setText(str(error))
            errBox.setIcon(QMessageBox.Icon.Critical)
            errBox.exec()