# Grade Calculator
# Get marks from user
subjects = ['Math' , 'English' , 'Science' , 'History']
total = 0
for subject in subjects:
    mark = float(input(f'Enter marks for {subject}:'))
    total += mark
average = total / len(subjects)
# Determine grade
if average>= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade =  'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'
# Output results
print(f'\nTotal Marks: {total}')
print(f'Average: {average: .2f}')
print(f'Grade: {grade}')
