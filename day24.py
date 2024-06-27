import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class KuadratCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hitung Kuadrat')

        self.layout = QVBoxLayout()

        self.label = QLabel('Masukkan bilangan bulat:')
        self.layout.addWidget(self.label)

        self.inputField = QLineEdit(self)
        self.layout.addWidget(self.inputField)

        self.calcButton = QPushButton('Hitung Kuadrat', self)
        self.calcButton.clicked.connect(self.calculateSquare)
        self.layout.addWidget(self.calcButton)

        self.resultLabel = QLabel('')
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

    def calculateSquare(self):
        try:
            bilangan = int(self.inputField.text())
            hasil = bilangan ** 2
            self.resultLabel.setText(f'Hasil kuadrat dari {bilangan} adalah: {hasil}')
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Input yang dimasukkan tidak valid! Masukkan bilangan bulat.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = KuadratCalculator()
    calculator.show()
    sys.exit(app.exec_())
