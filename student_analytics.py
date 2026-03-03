import constants

class StudentAnalytics:
  """"""
  def __init__(self,data_frame) -> None:
    self.df = data_frame

  def total_number_of_students(self)-> int:
    """Return the total number of students in the file."""
    count_series = self.df.count()
    return count_series["Matric No"]
  
  def number_of_students_per_department(self,department:str)-> None:
    """Prints the number of students in a department.
    
    Parameter:
      - department: The dapartment's number of students printed on the console.
    """
    department_series = self.df[constants.COURSE]
    print(f"The number of students in {department} is {department_series.value_counts()[department]}")

  def number_of_students_per_grade(self,grade:str)-> None:
    """Prints the number of students with a grade (First, Second, or third class).
    
    Parameter:
      - grade: The number of students with this grade is printed on the console.
    """
    grade_series = self.df[constants.GRADE]
    print(f"The number of students with {grade} is {grade_series.value_counts()[grade]}")

  def number_of_students_per_reason(self,reason:str)-> None:
    """Prints the number of students with a reason.
    
    Parameter:
      - reason: The number of students with this reason is printed on the console.
    """
    reason_series = self.df[constants.REASON]
    print(f"The number of students with '{reason}' issue is {reason_series.value_counts()[reason]}")

  def print_students(self,filtered_df, context_label,)-> None:
    """Prints student names

    Parameters:
      - filtered_df: The filtered Dataframe containing student records.
      - context_label: Describes the filtering context (e.g., department or issue).

    Behavior:
      - Prints the total number of students, and each student's name in the order (SURNAME OTHERNAMES) on a new line.
      - Prints out a "does not exist" message, if the Dataframe is empty.
    """
    students_name_series = filtered_df[constants.SURNAME] + " " + filtered_df[constants.OTHERNAMES]

    if filtered_df.empty:
        print(f"{context_label.capitalize()} does not exist.")
    else:
        print(f"Below are the name of students {context_label}\n")
        print(f"There are {len(students_name_series)} students {context_label}\n")
        print("\n".join(students_name_series.to_list()))

  def students_with_a_specific_issue(self,issue_name:str)-> None:
    """Prints every student's name with an issue.
    
    Parameter:
      - issue: The issue whose students data is displayed.
    """
    filtered_df = self.df[
          self.df[constants.REASON].str.lower() == issue_name.lower()
      ]
    self.print_students(filtered_df, f"with '{issue_name}' issue")

  def students_belonging_to_a_specific_department(self,department_name:str)-> None:
    """Prints every student's name belonging to a department.
    
    Parameter:
      - department: The department whose students data is displayed.
    """
    filtered_df = self.df[self.df[constants.COURSE] == department_name]
    self.print_students(filtered_df, f"in {department_name}")