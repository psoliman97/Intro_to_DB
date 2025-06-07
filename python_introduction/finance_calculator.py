income = int(input('Enter your monthly income:'))
expenses = int(input('Enter your total monthly expenses:'))
monthly_saving = income - expenses
project_saving = ( monthly_saving * 12 +(monthly_saving * 12 * 0.05))
print ('Your monthly savings are', monthly_saving)
print ('Projected savings after one year, with interest, is:', project_saving)
