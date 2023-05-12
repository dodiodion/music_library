from lib.student import *
"""
Given a student,
we want to instantiate an Student object with id, student_name and cohort_id
"""
def test_student_init():
    student = Student(1, "Test Student name", 1)
    assert student.id == 1
    assert student.student_name == "Test Student name"
    assert student.cohort_id == 1

"""
We can format students to strings nicely
"""
def test_cohorts_format_nicely():
    student = Student(1, "Test Student name", 1)
    assert str(student) == "Student(1, Test Student name, 1)"

"""
We can compare two identical students
And have them be equal
"""
def test_students_are_equal():
    student1 = Student(1, "Test Student name", 1)
    student2 = Student(1, "Test Student name", 1)
    assert student1 == student2