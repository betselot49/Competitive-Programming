def gradingStudents(grades):
    final_grade = []
    for grade in grades:
        if grade < 38:
            final_grade.append(grade)
        else:
            i = 0
            while i < 3:
                if (grade + i) % 5 == 0:
                    final_grade.append(grade + i)
                    break
                else:
                    i += 1
            if i == 3:
                final_grade.append(grade)
    return final_grade
