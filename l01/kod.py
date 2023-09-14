# average salary
employees = [
    ('Eve', 2000),
    ('John', 1500),
    ('Sarah', 1100),
    ('Sarah', 1100),
]

def average_salary(employees):
    # sum_of_salaries = 0
    # for employee in employees:
    #     name, salary = employee
    #     sum_of_salaries += salary
    #
    # return sum_of_salaries / len(employees)
    return sum([salary for name, salary in employees]) / len(employees)

print("average salary is : ", average_salary(employees))