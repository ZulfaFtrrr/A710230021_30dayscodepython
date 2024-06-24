import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout

class Karyawan:
    def __init__(self, nama, id_karyawan, jabatan, gaji):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.jabatan = jabatan
        self.gaji = gaji

    def get_info(self):
        return {
            'nama': self.nama,
            'id_karyawan': self.id_karyawan,
            'jabatan': self.jabatan,
            'gaji': self.gaji
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Informasi Karyawan")
        self.setGeometry(100, 100, 400, 300)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.form_layout = QFormLayout()
        
        self.nama_input = QLineEdit()
        self.id_input = QLineEdit()
        self.jabatan_input = QLineEdit()
        self.gaji_input = QLineEdit()
        
        self.form_layout.addRow("Nama:", self.nama_input)
        self.form_layout.addRow("ID Karyawan:", self.id_input)
        self.form_layout.addRow("Jabatan:", self.jabatan_input)
        self.form_layout.addRow("Gaji:", self.gaji_input)
        
        self.layout.addLayout(self.form_layout)
        
        self.submit_button = QPushButton("Tambah Karyawan")
        self.submit_button.clicked.connect(self.tambah_karyawan)
        
        self.layout.addWidget(self.submit_button)
        
        self.info_label = QLabel("")
        self.layout.addWidget(self.info_label)
        
        self.karyawan_list = []

    def tambah_karyawan(self):
        nama = self.nama_input.text()
        id_karyawan = self.id_input.text()
        jabatan = self.jabatan_input.text()
        gaji = self.gaji_input.text()
        
        if nama and id_karyawan and jabatan and gaji:
            karyawan = Karyawan(nama, id_karyawan, jabatan, gaji)
            self.karyawan_list.append(karyawan)
            self.update_info_label()
            self.nama_input.clear()
            self.id_input.clear()
            self.jabatan_input.clear()
            self.gaji_input.clear()
        
    def update_info_label(self):
        info_text = "Daftar Karyawan:\n"
        for karyawan in self.karyawan_list:
            info = karyawan.get_info()
            info_text += (f"Nama       : {info['nama']}\n"
                          f"ID         : {info['id_karyawan']}\n"
                          f"Jabatan    : {info['jabatan']}\n"
                          f"Gaji       : {info['gaji']}\n"
                          f"{'-' * 20}\n")
        self.info_label.setText(info_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
