import pandas
import constants
from student_analytics import StudentAnalytics

print("START\n")
students_data = pandas.read_csv("students_data_950_rows.csv")
student_analytics = StudentAnalytics(students_data)
# ----------- TOTAL NUMBER OF STUDENTS ---------- #
print(f"The total number of students is {student_analytics.total_number_of_students()}")
print("\n")
# ----------- NUMBER OF STUDENTS PER DEPARMENT ---------- #
departments = set(students_data[constants.COURSE].to_list())
for department in departments:
  student_analytics.number_of_students_per_department(department)
print("\n")
# ----------- NUMBER OF STUDENTS PER GRADE ---------- #
grades = set(students_data[constants.GRADE].to_list())
for grade in grades:
  student_analytics.number_of_students_per_grade(grade)
print("\n")
# ----------- NUMBER OF STUDENTS PER REASON ---------- #
reasons = set(students_data[constants.REASON].to_list())
for reason in reasons:
  student_analytics.number_of_students_per_reason(reason)
print("\n")
# ----------- STUDENTS BELONGING TO A SPECIFIC DEPARTMENT ---------- #
print(f"Recorded Departments: {", ".join(departments)}\n")
department = input("From the departments above, which will you like to get it's students data?: ").title()
student_analytics.students_belonging_to_a_specific_department(department)
print("\n")
# ----------- STUDENTS WITH A SPECIFIC ISSUE ---------- #
print(f"Recorded Issues: {", ".join(reasons)}\n")
issue = input("From the issues above, which will you like to get it's students data?: ").title()
student_analytics.students_with_a_specific_issue(issue)
print("\n")


