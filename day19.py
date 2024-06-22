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
        print("Daftar Mahasiswa:")
        for student in self.students:
            print(student)

    def find_student_by_nim(self, nim):
        for student in self.students:
            if student.nim == nim:
                return student
        return None

    def __str__(self):
        return f"University has {len(self.students)} students."


# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat instance universitas
    university = University()

    # Menambahkan mahasiswa ke universitas
    student1 = Student("Zulfa", "A710230021", "PTI", 2)
    student2 = Student("Ihya", "A710230038", "PTI", 2)
    student3 = Student("Maya", "A710230009", "PTI", 2)

    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)

    # Menampilkan daftar mahasiswa
    university.display_students()

    # Mencari mahasiswa berdasarkan NIM
    nim_to_search = "A710230038"
    found_student = university.find_student_by_nim(nim_to_search)
    if found_student:
        print(f"\nMahasiswa dengan NIM {nim_to_search} ditemukan:\n{found_student}")
    else:
        print(f"\nMahasiswa dengan NIM {nim_to_search} tidak ditemukan.")
