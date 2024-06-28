import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calculator')

        # Main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        # Buttons
        buttons_layout = QGridLayout()
        main_layout.addLayout(buttons_layout)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_button_click)
            buttons_layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
