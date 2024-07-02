import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox

class FormApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set window title
        self.setWindowTitle("Form PyQt5 App")
        
        # Set window size
        self.setGeometry(100, 100, 400, 300)
        
        # Create layout
        self.layout = QVBoxLayout()
        
        # Create and add widgets to layout
        self.name_label = QLabel('Name:', self)
        self.layout.addWidget(self.name_label)
        
        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)
        
        self.gender_label = QLabel('Gender:', self)
        self.layout.addWidget(self.gender_label)
        
        self.gender_combo = QComboBox(self)
        self.gender_combo.addItems(['Male', 'Female', 'Other'])
        self.layout.addWidget(self.gender_combo)
        
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.show_data)
        self.layout.addWidget(self.submit_button)
        
        # Set layout to the window
        self.setLayout(self.layout)
        
    def show_data(self):
        name = self.name_input.text()
        gender = self.gender_combo.currentText()
        QMessageBox.information(self, "Form Data", f"Name: {name}\nGender: {gender}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Create an instance of the application window
    window = FormApp()
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec_())
