# Who has the most money?
# https://www.codewars.com/kata/528d36d7cc451cd7e4000339
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    sum_of_money = []
    for student in students:
        each_student = (student.name, (student.fives*5 + student.tens*10 + student.twenties*20))
        sum_of_money.append(each_student)

    if len(sum_of_money) == 1:
        return sum_of_money[0][0]
    elif len(set(i[1] for i in sum_of_money)) == 1:
        return "all"
    else:
        return max(sum_of_money, key=lambda x: x[1])[0]


if __name__ == "__main__":
    phil = Student("Phil", 2, 2, 1)
    cam = Student("Cameron", 2, 2, 0)
    geoff = Student("Geoff", 0, 3, 0)

    print(most_money([cam, geoff, phil]))  # Phill
    print(most_money([cam, geoff]))  # all
    print(most_money([geoff]))  # Geoff


# other solutions
def most_money(students):
    total = []
    for student in students:
        total.append((student.fives * 5) + (student.tens * 10) + (student.twenties * 20))

    if min(total) == max(total) and len(students) > 1:
        return "all"
    else:
        return students[total.index(max(total))].name
