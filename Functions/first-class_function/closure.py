def create_printer():
    my_favorite_number = 42

    # def printer has access to my_favorite_number
    def printer():
        print(f"My favorite numbers is {my_favorite_number}")

    return printer


my_printer = create_printer()
my_printer()
# print(my_favorite_number) <-- NameError: name 'my_favorite_number' is not defined


def create_counter():
    count = 0

    def get_count():
        return count

    def increment():
        # "nonlocal" just tells Python that the "count" we're using here is the same variable as the one in the other
        # scope. Otherwise, Python would think that we were trying to define a local variable with the same name
        # inside my_increment.
        nonlocal count
        count += 1

    return get_count, increment


my_get_count, my_increment = create_counter()
print(my_get_count())
my_increment()
my_increment()
print(my_get_count())
my_increment()
my_increment()
my_increment()
print(my_get_count())
