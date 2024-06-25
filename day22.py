import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class Student:
    def __init__(self, name, nim, prodi, semester):
        self.name = name
        self.nim = nim
        self.prodi = prodi
        self.semester = semester

    def __str__(self):
        return f"Nama: {self.name}, NIM: {self.nim}, Prodi: {self.prodi}, Semester: {self.semester}"

class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student: {student.name}")

    def display_students(self):
        student_list = "Daftar Mahasiswa:\n"
        for student in self.students:
            student_list += str(student) + "\n"
        return student_list

    def find_student_by_nim(self, nim):
        for student in self.students:
            if student.nim == nim:
                return student
        return None

    def __str__(self):
        return f"University has {len(self.students)} students."


class UniversityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.university = University()

    def initUI(self):
        self.setWindowTitle("University Application")

        self.layout = QVBoxLayout()

        # Input fields
        self.name_label = QLabel("Nama:")
        self.name_input = QLineEdit()

        self.nim_label = QLabel("NIM:")
        self.nim_input = QLineEdit()

        self.prodi_label = QLabel("Prodi:")
        self.prodi_input = QLineEdit()

        self.semester_label = QLabel("Semester:")
        self.semester_input = QLineEdit()

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.nim_label)
        self.layout.addWidget(self.nim_input)
        self.layout.addWidget(self.prodi_label)
        self.layout.addWidget(self.prodi_input)
        self.layout.addWidget(self.semester_label)
        self.layout.addWidget(self.semester_input)

        # Buttons
        self.add_button = QPushButton("Add Student")
        self.display_button = QPushButton("Display Students")
        self.search_button = QPushButton("Search by NIM")
        self.search_input = QLineEdit()
        self.result_area = QTextEdit()

        self.add_button.clicked.connect(self.add_student)
        self.display_button.clicked.connect(self.display_students)
        self.search_button.clicked.connect(self.search_student)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.display_button)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.result_area)

        self.setLayout(self.layout)

    def add_student(self):
        name = self.name_input.text()
        nim = self.nim_input.text()
        prodi = self.prodi_input.text()
        semester = int(self.semester_input.text())

        student = Student(name, nim, prodi, semester)
        self.university.add_student(student)

        self.result_area.setText(f"Added student: {name}")

    def display_students(self):
        students = self.university.display_students()
        self.result_area.setText(students)

    def search_student(self):
        nim = self.search_input.text()
        student = self.university.find_student_by_nim(nim)
        if student:
            self.result_area.setText(f"Mahasiswa dengan NIM {nim} ditemukan:\n{student}")
        else:
            self.result_area.setText(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UniversityApp()
    ex.show()
    sys.exit(app.exec_())
