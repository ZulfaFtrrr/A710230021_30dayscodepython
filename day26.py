import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class Orang:
    def __init__(self, nama, makanan_kesukaan, minuman_kesukaan, hobi):
        self.nama = nama
        self.makanan_kesukaan = makanan_kesukaan
        self.minuman_kesukaan = minuman_kesukaan
        self.hobi = hobi

    def perkenalan(self):
        return (f"Halo, nama saya {self.nama}.\n"
                f"Hobi saya adalah {self.hobi}.\n"
                f"Saya suka makan {self.makanan_kesukaan}.\n"
                f"Minuman kesukaan saya adalah {self.minuman_kesukaan}.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        orang1 = Orang("Joni", "pizza", "kopi", "bersepeda")
        orang2 = Orang("Jaja", "sushi", "teh", "membaca")

        layout = QVBoxLayout()

        label_orang1 = QLabel(orang1.perkenalan(), self)
        label_orang2 = QLabel(orang2.perkenalan(), self)

        layout.addWidget(label_orang1)
        layout.addWidget(label_orang2)

        self.setLayout(layout)
        self.setWindowTitle('Perkenalan Orang')
        self.show()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
