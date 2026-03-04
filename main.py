import pandas
import constants
from student_analytics import StudentAnalytics

def run():
  is_running = True

  students_data = pandas.read_csv("students_data_950_rows.csv")
  student_analytics = StudentAnalytics(students_data)
  departments = sorted(set(students_data[constants.COURSE].to_list()))
  grades = sorted(set(students_data[constants.GRADE].to_list()))
  reasons = sorted(set(students_data[constants.REASON].to_list()))

  while is_running:

    print("""
    1. Total students
    2. Number of students per department
    3. Number of students per grade
    4. Number of students per reason
    5. Students belonging to a specific department
    6. Students with a specific issue
    7. Exit
    """)

    try:
      choice = int(input("Pick a number: "))
      print()
    except ValueError:
      print()
      print("Enter a valid number.")
      print()
      continue

    if choice == 1:
    # ----------- TOTAL NUMBER OF STUDENTS ---------- #
      print(f"The total number of students is {student_analytics.total_number_of_students()}")
      print()
    elif choice == 2:
    # ----------- NUMBER OF STUDENTS PER DEPARMENT ---------- #
      for department in departments:
        student_analytics.number_of_students_per_department(department)
      print()
    elif choice == 3:
    # ----------- NUMBER OF STUDENTS PER GRADE ---------- #
      for grade in grades:
        student_analytics.number_of_students_per_grade(grade)
      print()
    elif choice == 4:
    # ----------- NUMBER OF STUDENTS PER REASON ---------- #
      for reason in reasons:
        student_analytics.number_of_students_per_reason(reason)
      print()
    elif choice == 5:
    # ----------- STUDENTS BELONGING TO A SPECIFIC DEPARTMENT ---------- #
      print(f"Recorded Departments: {", ".join(departments)}\n")
      department = input("From the departments above, which would you like to get its students data?: ").title()
      student_analytics.students_belonging_to_a_specific_department(department)
      print()
    elif choice == 6:
      # ----------- STUDENTS WITH A SPECIFIC ISSUE ---------- #
      print(f"Recorded Issues: {", ".join(reasons)}\n")
      issue = input("From the issues above, which would you like to get its students data?: ").title()
      student_analytics.students_with_a_specific_issue(issue)
      print()
    elif choice == 7:
      is_running = False
    elif choice > 7:
      print("Enter any number from 1-7.")
      print()


if __name__ == "__main__":
  run()


