def fizz_buzz(value):
    if is_multiple(value, 3) and is_multiple(value, 5):
        return "FizzBuzz"
    if is_multiple(value, 3):
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return value % mod == 0


def check_fizzbuzz(value, expected_value):
    ret_val = fizz_buzz(value)
    assert ret_val == expected_value


def test_returns_1_with_1_passed_in():
    check_fizzbuzz(1, "1")


def test_returns_2_with_2_passed_in():
    check_fizzbuzz(2, "2")


def test_returns_fizz_with_3_passed_in():
    check_fizzbuzz(3, "Fizz")


def test_returns_buzz_with_5_passed_in():
    check_fizzbuzz(5, "Buzz")


def test_returns_fizz_with_6_passed_in():
    check_fizzbuzz(6, "Fizz")


def test_returns_buzz_with_10_passed_in():
    check_fizzbuzz(10, "Buzz")


def test_returns_fizzbuzz_with_15_passed_in():
    check_fizzbuzz(15, "FizzBuzz")
