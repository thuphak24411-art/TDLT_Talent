from PyQt6.QtWidgets import QMessageBox
from Homework.Ex109.my_module import calc_depreciation
from Homework.Ex130.my_module import view_details
from Homework.Ex130.ui.DepreciationAddMainWindow import Ui_MainWindow

class DepreciationAddMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.process_depreciation)
        self.pushButtonViewDetails.clicked.connect(self.view_details)
    def process_depreciation(self):
        try:
            p=float(self.purchasePriceLineEdit.text())
            trans_free=float(self.transportationFeeLineEdit.text())
            install_fee=float(self.installationFeeLineEdit.text())
            self.years=int(self.yearsOfDepreciationLineEdit.text())
            self.original_price, self.annual_rate, monthly_rate = calc_depreciation(p, trans_free, install_fee, self.years)

            self.originalPriceLineEdit.setText(str(self.original_price))
            self.annualDepreciationRateLineEdit.setText(str(self.annual_rate))
            self.monthlyDepreciationRateLineEdit.setText(str(monthly_rate))
        except Exception as error:
            errBox = QMessageBox()
            errBox.setWindowTitle("Error")
            errBox.setText(str(error))
            errBox.setIcon(QMessageBox.Icon.Critical)
            errBox.exec()
    def view_details(self):
            details=view_details(self.original_price, self.annual_rate, self.years)
            self.listWidget.addItems(details)
