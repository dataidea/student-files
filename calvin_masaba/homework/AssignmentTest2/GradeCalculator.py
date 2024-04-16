#QUESTION 8

#Function to calculate grades

score = int(input('Enter the score: '))
def calculateGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


print('The score is:', score)
#print('The Grade is: ', calculateGrade(score))

mark = calculateGrade(score)
print(f'The Grade is: {mark}')


#By Calvin Masaba