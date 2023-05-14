# Kata name: Mexican Wave
# Link: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people: str) -> list:
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            people_list = list(people)
            people_list[i] = people_list[i].upper()
            changed_people = "".join(people_list)
            result.append(changed_people)

    return result


if __name__ == "__main__":
    print(wave("codewars"))
