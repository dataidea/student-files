#Adjust accordingly

class BasicCalculator:
    @staticmethod
    def add(*numbers):
        return sum(numbers)
    
    @staticmethod
    def subtract(*numbers):
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        return result
    
    @staticmethod
    def divide(*numbers):
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
        return result
    
    @staticmethod
    def multiply(*numbers):
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
        return result
    

# print(BasicCalculator.multiply(3, 4))
    

class CalculateCGPA:
    def __init__(self, marks:list=[], grades:list=[], credit_units:list=[]):

        self.marks = marks
        self.grades = grades
        self.credit_units = credit_units
    
    def calculate(self):
        if len(self.marks) == 0 or len(self.grades) == 0 or len(self.credit_units) == 0:
            raise ValueError('all marks, grades, and credit_units must be provided.')

        grader = {'A+': 5, 'A': 5, 'B+': 4.5, 'B': 4,
              'C+': 3.5, 'C': 3, 'D+': 2.5, 'D': 2,
              'E': 1.5, 'E-': 1, 'F': 0}
        
        CUs_sum = sum(self.credit_units)
        grade_CUs_sum = 0
        for counter in range(len(self.marks)):
            grade_CUs_sum += BasicCalculator.multiply(grader[self.grades[counter]], self.credit_units[counter])

        CGPA = BasicCalculator.divide(grade_CUs_sum, CUs_sum)

        with open(file='classes_result.docx', mode='w') as result:
            result.write(f'CGPA - {CGPA}')

        return CGPA
    
CGPA = CalculateCGPA(marks=[95, 50], grades=['A+', 'D'], credit_units=[4, 4])
CGPA.calculate()