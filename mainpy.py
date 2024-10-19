import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QInputDialog, QMessageBox)

class SchoolApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("School Registration & Salary Management")
        self.setGeometry(100, 100, 400, 600)
        
        # Set background color
        self.setStyleSheet("background-color: #f0f8ff;")  # Light blue background

        # Create a vertical layout
        layout = QVBoxLayout()

        # Section for Student Registration
        layout.addWidget(QLabel("Register Student"))
        self.student_name_input = QLineEdit(self)
        self.student_name_input.setPlaceholderText("Student Name")
        self.student_name_input.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.student_name_input)

        self.student_age_input = QLineEdit(self)
        self.student_age_input.setPlaceholderText("Student Age")
        self.student_age_input.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.student_age_input)

        self.student_class_input = QLineEdit(self)
        self.student_class_input.setPlaceholderText("Class")
        self.student_class_input.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.student_class_input)

        self.register_student_button = QPushButton("Register Student", self)
        self.register_student_button.setStyleSheet("background-color: #00cc99; color: white;")
        layout.addWidget(self.register_student_button)
        self.register_student_button.clicked.connect(self.register_student)

        # Section for Teacher Salary Management
        layout.addWidget(QLabel("Manage Teacher Salary"))
        self.teacher_name_input = QLineEdit(self)
        self.teacher_name_input.setPlaceholderText("Teacher Name")
        self.teacher_name_input.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.teacher_name_input)

        self.teacher_salary_input = QLineEdit(self)
        self.teacher_salary_input.setPlaceholderText("Teacher Salary")
        self.teacher_salary_input.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.teacher_salary_input)

        self.add_teacher_button = QPushButton("Add Teacher", self)
        self.add_teacher_button.setStyleSheet("background-color: #00cc99; color: white;")
        layout.addWidget(self.add_teacher_button)
        self.add_teacher_button.clicked.connect(self.add_teacher)

        # Buttons for Viewing, Updating, and Deleting Records
        self.view_students_button = QPushButton("View Students", self)
        self.view_students_button.setStyleSheet("background-color: #00ccff; color: white;")
        layout.addWidget(self.view_students_button)
        self.view_students_button.clicked.connect(self.view_students)

        self.view_teachers_button = QPushButton("View Teachers", self)
        self.view_teachers_button.setStyleSheet("background-color: #00ccff; color: white;")
        layout.addWidget(self.view_teachers_button)
        self.view_teachers_button.clicked.connect(self.view_teachers)

        self.update_student_button = QPushButton("Update Student", self)
        self.update_student_button.setStyleSheet("background-color: #ffcc00; color: white;")
        layout.addWidget(self.update_student_button)
        self.update_student_button.clicked.connect(self.update_student)

        self.update_teacher_button = QPushButton("Update Teacher", self)
        self.update_teacher_button.setStyleSheet("background-color: #ffcc00; color: white;")
        layout.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self.update_teacher)

        self.delete_student_button = QPushButton("Delete Student", self)
        self.delete_student_button.setStyleSheet("background-color: #ff6666; color: white;")
        layout.addWidget(self.delete_student_button)
        self.delete_student_button.clicked.connect(self.delete_student)

        self.delete_teacher_button = QPushButton("Delete Teacher", self)
        self.delete_teacher_button.setStyleSheet("background-color: #ff6666; color: white;")
        layout.addWidget(self.delete_teacher_button)
        self.delete_teacher_button.clicked.connect(self.delete_teacher)

        # Output area to show status
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: #ffffff; border: 1px solid #00aaff;")
        layout.addWidget(self.output_area)

        self.setLayout(layout)

    def register_student(self):
        name = self.student_name_input.text()
        age = self.student_age_input.text()
        student_class = self.student_class_input.text()

        if not name or not age or not student_class:
            self.output_area.append("Please fill all fields for student registration.")
            return

        try:
            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (name, age, class) VALUES (?, ?, ?)", 
                           (name, age, student_class))
            connection.commit()
            connection.close()
            self.output_area.append(f"Student '{name}' registered successfully.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def add_teacher(self):
        name = self.teacher_name_input.text()
        salary = self.teacher_salary_input.text()

        if not name or not salary:
            self.output_area.append("Please fill all fields for teacher salary management.")
            return

        try:
            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO teachers (name, salary) VALUES (?, ?)", 
                           (name, salary))
            connection.commit()
            connection.close()
            self.output_area.append(f"Teacher '{name}' added with salary '{salary}'.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def view_students(self):
        try:
            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()
            connection.close()

            self.output_area.clear()
            if records:
                for record in records:
                    self.output_area.append(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Class: {record[3]}")
            else:
                self.output_area.append("No students registered.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def view_teachers(self):
        try:
            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM teachers")
            records = cursor.fetchall()
            connection.close()

            self.output_area.clear()
            if records:
                for record in records:
                    self.output_area.append(f"ID: {record[0]}, Name: {record[1]}, Salary: {record[2]}")
            else:
                self.output_area.append("No teachers registered.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def update_student(self):
        try:
            student_id, ok = QInputDialog.getInt(self, "Update Student", "Enter Student ID:")
            if not ok:
                return

            new_name, ok = QInputDialog.getText(self, "Update Student", "Enter new name:")
            if not ok or not new_name:
                return

            new_age, ok = QInputDialog.getInt(self, "Update Student", "Enter new age:")
            if not ok:
                return

            new_class, ok = QInputDialog.getText(self, "Update Student", "Enter new class:")
            if not ok or not new_class:
                return

            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("UPDATE students SET name=?, age=?, class=? WHERE id=?", 
                           (new_name, new_age, new_class, student_id))
            connection.commit()
            connection.close()
            self.output_area.append(f"Student ID '{student_id}' updated successfully.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def update_teacher(self):
        try:
            teacher_id, ok = QInputDialog.getInt(self, "Update Teacher", "Enter Teacher ID:")
            if not ok:
                return

            new_name, ok = QInputDialog.getText(self, "Update Teacher", "Enter new name:")
            if not ok or not new_name:
                return

            new_salary, ok = QInputDialog.getDouble(self, "Update Teacher", "Enter new salary:")
            if not ok:
                return

            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("UPDATE teachers SET name=?, salary=? WHERE id=?", 
                           (new_name, new_salary, teacher_id))
            connection.commit()
            connection.close()
            self.output_area.append(f"Teacher ID '{teacher_id}' updated successfully.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def delete_student(self):
        try:
            student_id, ok = QInputDialog.getInt(self, "Delete Student", "Enter Student ID:")
            if not ok:
                return

            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            connection.commit()
            connection.close()
            self.output_area.append(f"Student ID '{student_id}' deleted successfully.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def delete_teacher(self):
        try:
            teacher_id, ok = QInputDialog.getInt(self, "Delete Teacher", "Enter Teacher ID:")
            if not ok:
                return

            connection = sqlite3.connect('school.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM teachers WHERE id=?", (teacher_id,))
            connection.commit()
            connection.close()
            self.output_area.append(f"Teacher ID '{teacher_id}' deleted successfully.")
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    school_app = SchoolApp()
    school_app.show()
    sys.exit(app.exec_())
