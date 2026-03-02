import pandas

COURSE = "Course"
GRADE = "Grade" 
REASON = "Reason"
SURNAME = "Surname"
OTHERNAMES = "Other Names"

def total_number_of_students()-> int:
  """"""
  count_series = students_data.count()
  return count_series["Matric No"]

def number_of_students_per_department(department:str):
  """"""
  department_series = students_data[COURSE]
  print(f"The number of students in {department} is {department_series.value_counts()[department]}")

def number_of_students_per_grade(grade:str):
  """"""
  grade_series = students_data[GRADE]
  print(f"The number of students with {grade} is {grade_series.value_counts()[grade]}")

def number_of_students_per_reason(reason:str):
  """"""
  reason_series = students_data[REASON]
  print(f"The number of students with '{reason}' issue is {reason_series.value_counts()[reason]}")

def students_belonging_to_a_specific_department(department:str):
  """"""
  students_data_belongiging_to_dept = students_data[students_data[COURSE] == department]
  students_name_series = students_data_belongiging_to_dept[SURNAME] + " " + students_data_belongiging_to_dept[OTHERNAMES]
  print(f"There are {len(students_name_series)} students in {department}\n")
  print("\n".join(students_name_series.to_list()))

def students_with_a_specific_issue(issue:str):
  """"""
  students_data_with_the_issue = students_data[students_data[REASON] == issue]
  students_name_series = students_data_with_the_issue[SURNAME] + " " + students_data_with_the_issue[OTHERNAMES]
  print(f"There are {len(students_name_series)} students with a '{issue}' issue\n")
  print("\n".join(students_name_series.to_list()))


print("START\n")
students_data = pandas.read_csv("students_data_950_rows.csv")
# ----------- TOTAL NUMBER OF STUDENTS ---------- #
print(f"The total number of students is {total_number_of_students()}")
print("\n")
# ----------- NUMBER OF STUDENTS PER DEPARMENT ---------- #
departments = set(students_data[COURSE].to_list())
for department in departments:
  number_of_students_per_department(department)
print("\n")
# ----------- NUMBER OF STUDENTS PER GRADE ---------- #
grades = set(students_data[GRADE].to_list())
for grade in grades:
  number_of_students_per_grade(grade)
print("\n")
# ----------- NUMBER OF STUDENTS PER REASON ---------- #
reasons = set(students_data[REASON].to_list())
for reason in reasons:
  number_of_students_per_reason(reason)
print("\n")
# ----------- STUDENTS BELONGING TO A SPECIFIC DEPARTMENT ---------- #
print(f"Recorded Departments: {", ".join(departments)}\n")
department = input("From the departments above, which will you like to get it's students data?: ").title()
print(f"Below are the name of students in {department}\n")
students_belonging_to_a_specific_department(department)
print("\n")
# ----------- STUDENTS WITH A SPECIFIC ISSUE ---------- #
print(f"Recorded Issues: {", ".join(reasons)}\n")
issue = input("From the issues above, which will you like to get it's students data?: ").title()
print(f"Below are the name of students with '{issue}' issue\n")
students_with_a_specific_issue(issue)
print("\n")


