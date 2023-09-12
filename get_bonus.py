def display_bonus(salary):
    print(f'Salary with bonus: {salary}')


salary = int(input('Enter salary: '))
years_of_service = float(input('Enter years of service: '))
running_time = 1
n = 1
if 5 <= years_of_service < 10:
    running_time += 1
    if n != 0:
        running_time += 1
    salary *= 0.05
    display_bonus(salary)
elif 10 <= years_of_service < 15:
    running_time += 1
    if n != 0:
        running_time += 1
    salary *= 1
    display_bonus(salary)
elif 15 <= years_of_service < 20:
    running_time += 1
    if n != 0:
        running_time += 1
    salary *= 1.5
    display_bonus(salary)
elif years_of_service >= 20:
    running_time += 1
    if n != 0:
        running_time += 1
    salary *= 2
    display_bonus(salary)
else:
    print('Not Eligible for Bonus!')
print(f'Running Time Complexity: {running_time}(n)')

                                    # Running Time Complexity: O(1)
