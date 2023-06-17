class Student:
    def __init__(self, name, lastname, birthdate):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate

class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def lookup_by_lastname(self, lastname):
        found_students = []
        for student in self.students:
            if student.lastname == lastname:
                found_students.append(student)
        return found_students

    def lookup_by_birthdate(self, birthdate):
        found_students = []
        for student in self.students:
            if student.birthdate == birthdate:
                found_students.append(student)
        return found_students

    def sort_by_lastname(self):
        self.students.sort(key=lambda student: student.lastname)

    def sort_by_birthdate(self):
        self.students.sort(key=lambda student: student.birthdate)

    def get_student_count(self):
        return len(self.students)


student1 = Student("Egor", "German", "2000.12.12")
student2 = Student("Andrew", "Rizoboyev", "1999.05.21")
student3 = Student("Yan", "Lugovoy", "2009.12.24")


group = StudentGroup()


group.add_student(student1)
group.add_student(student2)
group.add_student(student3)


found_students = group.lookup_by_lastname("German")
for student in found_students:
    print(f"Found student: {student.name} {student.lastname}")

f_students = group.lookup_by_lastname("1999.05.21")
for student in f_students:
    print(f"Found student: {student.name} {student.lastname}")

group.sort_by_lastname()

for student in group.students:
    print(f"Student: {student.name} {student.lastname} {student.birthdate}")

print(f'Amount of students: {group.get_student_count()}')



