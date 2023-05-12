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