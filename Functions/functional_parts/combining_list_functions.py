from functools import reduce


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


def is_not_developer(employee):
    return employee['job_title'] != 'developer'


developers = list(filter(is_developer, employees))
non_developers = list(filter(is_not_developer, employees))


def get_salary(employee):
    return employee['salary']


developers_salaries = list(map(get_salary, developers))
non_developers_salaries = list(map(get_salary, non_developers))


def get_sum(acc, x):
    return acc + x


total_developer_salaries = reduce(get_sum, developers_salaries)
average_developer_salary = total_developer_salaries / len(developers_salaries)

total_non_developer_salaries = reduce(get_sum, non_developers_salaries)
average_non_developer_salary = total_non_developer_salaries / len(non_developers_salaries)

print(average_developer_salary)
print(average_non_developer_salary)
