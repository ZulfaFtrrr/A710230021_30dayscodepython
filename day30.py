import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout

class BiodataApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Biodata Form PyQt5 App")
        self.setGeometry(100, 100, 600, 400)

        # Create layout
        self.layout = QVBoxLayout()

        # Create and add widgets to layout
        self.name_label = QLabel('Name:', self)
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel('Age:', self)
        self.layout.addWidget(self.age_label)

        self.age_input = QLineEdit(self)
        self.layout.addWidget(self.age_input)

        self.gender_label = QLabel('Gender:', self)
        self.layout.addWidget(self.gender_label)

        self.gender_combo = QComboBox(self)
        self.gender_combo.addItems(['Male', 'Female', 'Other'])
        self.layout.addWidget(self.gender_combo)

        self.food_label = QLabel('Favorite Food:', self)
        self.layout.addWidget(self.food_label)

        self.food_input = QLineEdit(self)
        self.layout.addWidget(self.food_input)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.add_data)
        self.layout.addWidget(self.submit_button)

        # Create table to display data
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Name', 'Age', 'Gender', 'Favorite Food'])
        self.layout.addWidget(self.table)

        # Create search and delete layout
        self.search_delete_layout = QHBoxLayout()

        # Create search input and button
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search by Name")
        self.search_delete_layout.addWidget(self.search_input)

        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.search_data)
        self.search_delete_layout.addWidget(self.search_button)

        # Create delete input and button
        self.delete_input = QLineEdit(self)
        self.delete_input.setPlaceholderText("Delete by Name")
        self.search_delete_layout.addWidget(self.delete_input)

        self.delete_button = QPushButton('Delete', self)
        self.delete_button.clicked.connect(self.delete_data)
        self.search_delete_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.search_delete_layout)

        # Set layout to the window
        self.setLayout(self.layout)

    def add_data(self):
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_combo.currentText()
        favorite_food = self.food_input.text()

        if name and age and favorite_food:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(age))
            self.table.setItem(row_position, 2, QTableWidgetItem(gender))
            self.table.setItem(row_position, 3, QTableWidgetItem(favorite_food))

            self.name_input.clear()
            self.age_input.clear()
            self.food_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please fill in all the fields.")

    def search_data(self):
        search_name = self.search_input.text().strip()
        if not search_name:
            QMessageBox.warning(self, "Search Error", "Please enter a name to search.")
            return

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)  # Column 0 is the 'Name' column
            if item and item.text().lower() == search_name.lower():
                self.table.selectRow(row)
                return

        QMessageBox.information(self, "Search Result", f"No entry found for '{search_name}'.")

    def delete_data(self):
        delete_name = self.delete_input.text().strip()
        if not delete_name:
            QMessageBox.warning(self, "Delete Error", "Please enter a name to delete.")
            return

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)  # Column 0 is the 'Name' column
            if item and item.text().lower() == delete_name.lower():
                self.table.removeRow(row)
                QMessageBox.information(self, "Delete Result", f"Entry for '{delete_name}' deleted.")
                return

        QMessageBox.information(self, "Delete Result", f"No entry found for '{delete_name}'.")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create an instance of the application window
    window = BiodataApp()
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
