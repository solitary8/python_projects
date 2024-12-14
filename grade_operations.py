def passing_grades(grades):
    return [grade for grade in grades if grade >= 50]

def average_grades(grades):
    if grades:
        return sum(grades) / len(grades)
    return 0 

def failing_grades(grades):
    return [grade for grade in grades if grade < 50]     
