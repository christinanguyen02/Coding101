# CS 303E Quiz 5D
# Author: Finn Frankis

# Problem 1: Verbose Vocabulary
def verboseVocabulary(A, B, C):
    common_ab = A & B
    common_bc = B & C
    common_ac = A & C

    largest_length = max(len(common_ab), len(common_bc), len(common_ac))

    if len(common_ab) == largest_length:
        return common_ab
    elif len(common_bc) == largest_length:
        return common_bc
    else:
        return common_ac


# Problem 2: Get Grades
def getGrades(lst):
    averages = {}

    for student_data in lst:
        student_name = student_data[0]

        midterms = student_data[1:4] # discard student name, final exam
        weighted_total = 0
        raw_total = 0
        for midterm in midterms:
            weighted_total += midterm * 0.20
            raw_total += midterm
        
        midterm_average = raw_total / len(midterms)
        final = student_data[4]
        if midterm_average < final:
            weighted_total += final * 0.40 # add final exam
        else:
            weighted_total += midterm_average * 0.40

        averages[student_name] = int(weighted_total)


    return averages