import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class AttendanceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Attendance App')
        self.setGeometry(100, 100, 400, 300)

        # Widgets
        self.label_name = QLabel('Nama:', self)
        self.edit_name = QLineEdit(self)
        self.btn_add = QPushButton('Tambah Kehadiran', self)
        self.btn_add.clicked.connect(self.add_attendance)
        
        self.list_attendance = QListWidget(self)

        # Layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_name)
        vbox.addWidget(self.edit_name)
        vbox.addWidget(self.btn_add)
        vbox.addWidget(self.list_attendance)

        self.setLayout(vbox)

    def add_attendance(self):
        name = self.edit_name.text().strip()
        if name:
            self.list_attendance.addItem(name)
            self.edit_name.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Silakan masukkan nama terlebih dahulu.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AttendanceApp()
    ex.show()
    sys.exit(app.exec_())
