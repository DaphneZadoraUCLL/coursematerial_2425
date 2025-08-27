def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    grades = [grade1, grade2, grade3, grade4, grade5]
    
    skipped_tests = 0
    tests_taken = 0
    total_grade = 0

    for g in grades:
        if g is None:
            skipped_tests += 1
        else:
            tests_taken += 1
            total_grade += g

    if skipped_tests >= 2:
        return False

    average_grade = total_grade / tests_taken
    if average_grade >= 12:
        return True
    else:
        return False