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
  """
  filtered_df = students_data[students_data[COURSE] == department]
  print_students(filtered_df, f"in {department}")

def students_with_a_specific_issue(issue:str):
  """Prints on the console every student's name with an issue.
  
  parameters:
    - issue: The issue whose students data is displayed.
  """
  filtered_df = students_data[
        students_data[REASON].str.lower() == issue.lower()
    ]
  print_students(filtered_df, f"with '{issue}' issue")

def print_students(filtered_df, context_label,):
    """Prints student names on the console

    parameters:
      - filtered_df: The filtered Dataframe containing student records.
      - context_label: Describes the filtering context (e.g., department or issue).

    Behavior:
      - Prints the total number of students, and each student's name in the order (SURNAME OTHERNAMES) on a new line.
      - Prints out a "does not exist" message, if the Dataframe is empty.
    """
    students_name_series = filtered_df[SURNAME] + " " + filtered_df[OTHERNAMES]

    if len(students_name_series) > 0:
        print(f"Below are the name of students {context_label}\n")
        print(f"There are {len(students_name_series)} students {context_label}\n")
        print("\n".join(students_name_series.to_list()))
    else:
        print(f"{context_label.capitalize()} does not exist.")


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


