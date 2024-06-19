import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Dialogo(QMainWindow):
    # Tipo de cambio al 19 de junio de 2024
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.79  # Tasa de cambio USD a GBP (por ejemplo)
    EURtoGBP = 0.84  # Tasa de cambio EUR a GBP
    PENtoGBP = 0.21  # Tasa de cambio PEN a GBP

    def __init__(self):
        # Cargar el archivo .ui desde la ruta específica
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta, self)

        # Conectar el botón pbTipoCambio a la función calcularConversion
        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        convertido = 0.0
        inicial = 0.0

        # Leer el valor inicial desde el QLineEdit leImporte
        try:
            inicial = float(self.leImporte.text())
        except ValueError:
            # Manejo de errores si el valor no es numérico
            self.lblCambio.setText("Error: Ingresa un número válido")
            return

        # Determinar la moneda de origen y destino según los radio buttons seleccionados
        if self.rbDeEUR.isChecked():
            if self.rbAEUR.isChecked():
                convertido = inicial  # De EUR a EUR
            elif self.rbAGBP.isChecked():
                convertido = inicial * self.EURtoGBP  # De EUR a GBP
            else:
                convertido = inicial * (1 / self.USDtoEUR)  # De EUR a USD
        elif self.rbDePEN.isChecked():
            if self.rbAPEN.isChecked():
                convertido = inicial  # De PEN a PEN
            elif self.rbAGBP.isChecked():
                convertido = inicial * self.PENtoGBP  # De PEN a GBP
            else:
                convertido = inicial * (1 / self.USDtoPEN)  # De PEN a USD
        elif self.rbDeGBP.isChecked():
            if self.rbAEUR.isChecked():
                convertido = inicial / self.EURtoGBP  # De GBP a EUR
            elif self.rbAPEN.isChecked():
                convertido = inicial / self.PENtoGBP  # De GBP a PEN
            else:
                convertido = inicial / self.USDtoGBP  # De GBP a USD
        else:
            # De USD a otra moneda
            if self.rbAUSD.isChecked():
                convertido = inicial  # De USD a USD
            elif self.rbAEUR.isChecked():
                convertido = inicial * self.USDtoEUR  # De USD a EUR
            elif self.rbAPEN.isChecked():
                convertido = inicial * self.USDtoPEN  # De USD a PEN
            else:
                convertido = inicial * self.USDtoGBP  # De USD a GBP

        # Mostrar el resultado formateado en el QLabel lblCambio
        self.lblCambio.setText(f"{convertido:.2f}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    sys.exit(app.exec_())
