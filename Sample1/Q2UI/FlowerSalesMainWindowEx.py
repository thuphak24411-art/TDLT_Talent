from Sample_Midterm.Midterm1.Q2.Q2 import calc_revenue
from Sample_Midterm.Midterm1.Q2UI.FlowerSalesMainWindow import Ui_MainWindow


class FlowerSalesMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.dalat_quantity=[]
        self.dalat_totalValue=0
        self.sapa_quantity=[]
        self.sapa_totalValue=0
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.process_sales)
    def process_sales(self):
        totalRevenue=0
        quantity = int(self.numberOfBouquetsLineEdit.text())
        price = float(self.priceOfEachBouquetsLineEdit.text())
        discount = float(self.discountRateLineEdit.text()) / 100

        if self.radioButtonDalat.isChecked():
            totalRevenue = calc_revenue(quantity, price, discount)
            self.dalat_quantity.append(quantity)
            self.dalat_totalValue+=totalRevenue
        elif self.radioButtonSapa.isChecked():
            totalRevenue = calc_revenue(quantity,price,discount)
            self.sapa_quantity.append(quantity)
            self.sapa_totalValue+=totalRevenue

        self.totalRevenueLineEdit.setText(str(totalRevenue))

        self.totalQuantityDalatLineEdit.setText(str(len(self.dalat_quantity)))
        self.totalValueDalatLineEdit.setText(str(self.dalat_totalValue))

        self.totalQuantitySapaLineEdit.setText(str(len(self.sapa_quantity)))
        self.totalValueSapaLineEdit.setText(str(self.sapa_totalValue))
