import pandas

COURSE = "Course"
GRADE = "Grade" 
REASON = "Reason"
SURNAME = "Surname"
OTHERNAMES = "Other Names"

def total_number_of_students()-> int:
  """Return the total number of students in the file."""
  count_series = students_data.count()
  return count_series["Matric No"]

def number_of_students_per_department(department:str):
  """Prints on the console the number of students in a department.
  
  parameter:
    - department: The dapartment's number of students printed on the console.
  """
  department_series = students_data[COURSE]
  print(f"The number of students in {department} is {department_series.value_counts()[department]}")

def number_of_students_per_grade(grade:str):
  """Prints on the console the number of students with a grade (First, Second, or third class).
  
  parameter:
    - grade: The number of students with this grade is printed on the console.
  """
  grade_series = students_data[GRADE]
  print(f"The number of students with {grade} is {grade_series.value_counts()[grade]}")

def number_of_students_per_reason(reason:str):
  """Prints on the console the number of students with a reason.
  
  parameter:
    - reason: The number of students with this reason is printed on the console.
  """
  reason_series = students_data[REASON]
  print(f"The number of students with '{reason}' issue is {reason_series.value_counts()[reason]}")

def students_belonging_to_a_specific_department(department:str):
  """Prints on the console every student's name belonging to a department.
  
  parameters:
    - department: The department whose students data is displayed.

  Prints out the total number of students in the dapartment, and
  prints out the name's in the format (SURNAME OTHERNAMES) of each students in the department, each on a new line.
  If the department `department` does not exist, it prints out a "Department `department` does not exist".
  """
  students_data_belongiging_to_dept = students_data[students_data[COURSE] == department]
  students_name_series = students_data_belongiging_to_dept[SURNAME] + " " + students_data_belongiging_to_dept[OTHERNAMES]
  if len(students_name_series) > 0:
    print(f"Below are the name of students in {department}\n")
    print(f"There are {len(students_name_series)} students in {department}\n")
    print("\n".join(students_name_series.to_list()))
  else:
    print(f"Department '{department}' does not exist.")

def students_with_a_specific_issue(issue:str):
  """Prints on the console every student's name with an issue.
  
  parameters:
    - issue: The issue whose students data is displayed.

  Prints out the total number of students with this issue, and
  prints out the name's in the format (SURNAME OTHERNAMES) of each students with the issue, each on a new line.
  If the issue `issue` does not exist, it prints out a "Issue `issue` does not exist".
  """
  students_data_with_the_issue = students_data[students_data[REASON].str.lower() == issue.lower()]
  students_name_series = students_data_with_the_issue[SURNAME] + " " + students_data_with_the_issue[OTHERNAMES]
  if len(students_name_series) > 0:
    print(f"Below are the name of students with '{issue}' issue\n")
    print(f"There are {len(students_name_series)} students with a '{issue}' issue\n")
    print("\n".join(students_name_series.to_list()))
  else:
    print(f"Issue '{issue}' does not exist.")


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
students_belonging_to_a_specific_department(department)
print("\n")
# ----------- STUDENTS WITH A SPECIFIC ISSUE ---------- #
print(f"Recorded Issues: {", ".join(reasons)}\n")
issue = input("From the issues above, which will you like to get it's students data?: ").title()
students_with_a_specific_issue(issue)
print("\n")


