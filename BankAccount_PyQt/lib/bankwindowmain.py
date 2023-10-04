import sys
from PyQt6 import QtWidgets as qtw

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Welcome to Times Bank')
        self.setGeometry(200,200,500,500)
        toolbar = qtw.QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        self.menu()
        # self.setupUINewBankAccount()

    # def setupUINewBankAccount(self)   :
        lineEditFull_name = qtw.QLineEdit()
        lineEditPin_code = qtw.QLineEdit()
        lineEditValue_deposit = qtw.QLineEdit()
        mainLayout = qtw.QFormLayout()
        buttonBox = qtw.QDialogButtonBox()
        mainLayout.addRow('Enter your full name', lineEditFull_name)
        mainLayout.addRow('Enter your PIN code', lineEditPin_code)
        mainLayout.addRow('Enter a value to deposit', lineEditValue_deposit)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        # self.show();

    def  menu (self) :
        menubar = self.menuBar()

        # добавяне на елементи в менюто
        BankAccountMenu = menubar.addMenu('BankAccounts')
        BankAccountMenu.addAction('New Bank Account')
        BankAccountMenu.addAction('Whithdraw Money')
        BankAccountMenu.addAction('Deposit Money')
        BankAccountMenu.addAction('Check Customers & Balance')
        quitAction = BankAccountMenu.addAction('Exit/Quit', self.close)                
        

        

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()
    window.show()

    sys.exit(app.exec())