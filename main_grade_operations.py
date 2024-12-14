import grade_operations
import random

grades = [random.randint(1,101) for x in range(10)]

passing_grades = grade_operations.passing_grades(grades)
failing_grades = grade_operations.failing_grades(grades)
average_grade = grade_operations.average_grades(grades)


print(f"Here are the passing grades : {passing_grades},here the failing grades :{failing_grades} and the average grade is {average_grade}")
