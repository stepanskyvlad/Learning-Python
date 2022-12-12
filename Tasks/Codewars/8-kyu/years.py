# Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat_years, dog_years = 0, 0
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    else:
        cat_years = 24 + 4 * (human_years-2)
        dog_years = 24 + 5 * (human_years-2)
    return [human_years, cat_years, dog_years]


# other solutions
def human_years_cat_years_dog_years_1(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]


print(human_years_cat_years_dog_years(15))
