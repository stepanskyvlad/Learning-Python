employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]
# the task is calculating how the average salary of the developers in our data set
# compares to the average salary of all the other professions.


def is_developer(employee):
    return employee['job_title'] == 'developer'


def get_salary(employee):
    return employee['salary']


def get_average_salary(salaries):
    return sum(salaries)/len(salaries)


average_developer_salary = get_average_salary([get_salary(x) for x in employees if is_developer(x)])
print(average_developer_salary)

average_non_developer_salary = get_average_salary([get_salary(x) for x in employees if not is_developer(x)])
print(average_non_developer_salary)
