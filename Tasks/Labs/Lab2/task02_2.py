while True:
    try:
        years = int(input('How many years do you work? Enter a number: '))
        months = int(input('How many months do you work? Enter a number: '))
        days = int(input('How many days do you work? Enter a number: '))
        salary = float(input("Enter your salary: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        if years > 10:
            print("You entered more than 10 years. Try again.")
            continue
        elif months >= 12:
            print("You entered 12 or more than 12 month. Try again.")
            continue
        elif days >= 365:
            print("You entered 365 or more than 365 days. Try again")
            continue
        else:
            if 2 < years < 5:
                premium = salary*0.02
                new_salary = premium+salary
                print(f"Your premium is {premium}, so new salary - {new_salary}")
                break
            elif 5 <= years <= 10:
                premium = salary * 0.05
                new_salary = premium + salary
                print(f"Your premium is {premium}, so new salary - {new_salary}")
                break
