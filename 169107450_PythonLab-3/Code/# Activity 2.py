# Activity 2

Grade = float(input("Enter your grade percentage: "))
# Rounding the grade to the nearest whole number
Grade_Number = round(Grade,0)
# Converting numeric grade to letter grade
if Grade_Number >= 90:
    Grade_Letter = 'A+'
elif Grade_Number >= 80:
    Grade_Letter = 'A'
elif Grade_Number >= 70:
    Grade_Letter = 'B'
elif Grade_Number >= 60:
    Grade_Letter = 'C'
elif Grade_Number >= 50:
    Grade_Letter = 'D'
else:
    Grade_Letter = 'F'
# Printing the Results
print(f"Your grade is: {Grade_Letter}")
