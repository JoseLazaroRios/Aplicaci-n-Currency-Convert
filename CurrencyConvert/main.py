import sys
from PyQt5.QtWidgets import QApplication
from src.logica.CurrencyConvert import Dialogo

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec_()
