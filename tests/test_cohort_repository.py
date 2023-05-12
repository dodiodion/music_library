from lib.cohort_repository import *
from lib.student import *
from lib.cohort import *
"""
Find a cohort using its id, 
and return the cohort with all the students that are in this cohort
"""
def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, "Summer 2021", "12-06-2021", [
        Student(1, "Bob Builder", 1), 
        Student(2, "Vladimir Putin", 1)])