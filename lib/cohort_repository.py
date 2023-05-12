from lib.student import Student
from lib.cohort import Cohort
class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            "SELECT cohorts.id AS cohort_id, cohorts.cohort_name AS cohort_name, cohorts.starting_date AS cohort_starting_date , students.id AS student_id, students.student_name AS student_name " \
            "FROM cohorts JOIN students ON cohort_id = students.cohort_id " \
            "WHERE cohorts.id =%s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["cohort_starting_date"], students)
