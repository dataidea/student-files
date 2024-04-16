#Adjust accordingly

def basicCalculator(*numbers, operation=''):
    if operation == '':
        raise ValueError('operation must be specified')

    if operation == '+':
        return sum(numbers)
    
    if operation == '-':
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        return result
    
    if operation == '/':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
        return result
    
    if operation == '*':
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
        return result
    

def calculateCGPA(marks:list=[], grades:list=[], credit_units:list=[]):
    if len(marks) == 0 or len(grades) == 0 or len(credit_units) == 0:
        raise ValueError('all marks, grades, and credit_units must be provided.')

    grader = {'A+': 5, 'A': 5, 'B+': 4.5, 'B': 4,
              'C+': 3.5, 'C': 3, 'D+': 2.5, 'D': 2,
              'E': 1.5, 'E-': 1, 'F': 0}
    
    CUs_sum = sum(credit_units)
    grade_CUs_sum = 0
    for counter in range(len(marks)):
        # grade_CUs_sum += grader[grade[counter]] * credit_units[counter]
        grade_CUs_sum += basicCalculator(grader[grades[counter]], credit_units[counter], operation='*')

    # CGPA = grade_CUs_sum / CUs_sum
    CGPA = basicCalculator(grade_CUs_sum, CUs_sum, operation='/')

    with open(file='functions_result.docx', mode='w') as result:
        result.write(f'CGPA - {CGPA}')


    return CGPA

calculateCGPA(marks=[95, 50], grades=['A+', 'D'], credit_units=[4, 4])
