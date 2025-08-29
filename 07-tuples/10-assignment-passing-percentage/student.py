def passing_percentage(grades):
    passed = 0

    for grade in grades:
        if grade >= 10:
            passed += 1
    percentage = passed / len(grades) * 100
    return percentage
