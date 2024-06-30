import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class Tiket:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah

    def harga(self):
        raise NotImplementedError("Method harga() harus diimplementasikan di subclass")

class TiketBiasa(Tiket):
    def harga(self):
        return self.jumlah * 30000

class TiketVIP(Tiket):
    def harga(self):
        return self.jumlah * 65000

class TiketGold(Tiket):
    def harga(self):
        return self.jumlah * 100000

class TicketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ticket Pricing')
        self.layout = QVBoxLayout()

        # ComboBox for selecting ticket type
        self.jenisLabel = QLabel('Masukkan jenis tiket:')
        self.layout.addWidget(self.jenisLabel)
        
        self.jenisComboBox = QComboBox(self)
        self.jenisComboBox.addItem("biasa")
        self.jenisComboBox.addItem("vip")
        self.jenisComboBox.addItem("gold")
        self.layout.addWidget(self.jenisComboBox)

        # LineEdit for entering the quantity of tickets
        self.jumlahLabel = QLabel('Masukkan jumlah tiket:')
        self.layout.addWidget(self.jumlahLabel)

        self.jumlahLineEdit = QLineEdit(self)
        self.layout.addWidget(self.jumlahLineEdit)

        # Button to calculate the price
        self.calcButton = QPushButton('Calculate', self)
        self.calcButton.clicked.connect(self.calculatePrice)
        self.layout.addWidget(self.calcButton)

        # Label to display the total price
        self.resultLabel = QLabel('Total Harga Tiket: ')
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

    def calculatePrice(self):
        jenis_tiket = self.jenisComboBox.currentText()
        try:
            jumlah_tiket = int(self.jumlahLineEdit.text())
        except ValueError:
            self.resultLabel.setText("Jumlah tiket harus berupa angka.")
            return

        if jenis_tiket == "biasa":
            tiket = TiketBiasa(jenis_tiket, jumlah_tiket)
        elif jenis_tiket == "vip":
            tiket = TiketVIP(jenis_tiket, jumlah_tiket)
        elif jenis_tiket == "gold":
            tiket = TiketGold(jenis_tiket, jumlah_tiket)
        else:
            self.resultLabel.setText("Jenis tiket tidak valid")
            return

        total_harga = tiket.harga()
        self.resultLabel.setText(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ticketApp = TicketApp()
    ticketApp.show()
    sys.exit(app.exec_())
