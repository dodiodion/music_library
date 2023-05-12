from lib.cohort import *
"""
Given a cohort,
we want to instantiate an Cohort object with id, cohort_name and starting_date
"""
def test_cohort_init():
    cohort = Cohort(1, "Test Cohort name", "12-05-2021")
    assert cohort.id == 1
    assert cohort.cohort_name == "Test Cohort name"
    assert cohort.starting_date == "12-05-2021"

"""
We can format cohorts to strings nicely
"""
def test_cohorts_format_nicely():
    cohort = Cohort(1, "Test Cohort name", "12-05-2021")
    assert str(cohort) == "Cohort(1, Test Cohort name, 12-05-2021)"

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test Cohort name", "12-05-2021")
    cohort2 = Cohort(1, "Test Cohort name", "12-05-2021")
    assert cohort1 == cohort2
