def avg(a, b, c, /):  # "/ - make arguments positional-only which are before '/'"
    return (a + b + c) / 3


print(avg(1, 2, 3))
# print(avg(a=1, b=2, c=3))-> TypeError: avg() got some positional-only arguments passed as keyword arguments: 'a, b, c'


def assert_equal(left, right, /, fail_massage=''):  # last argument is after '/', so we can write key-word for this
    return (left == right, fail_massage)


assert_equal(1, 1)
assert_equal(1, 1, fail_massage='left not equals right')
# assert_equal(left=1, right=2) -> error


def copy_file(*, source, destination, overwrite=False):  # after "*" we must write key-only arguments
    print(f"copying {source} to {destination} with overwrite={overwrite}")


copy_file(source="file1.txt", destination="file2.txt", overwrite=True)


def copy_file(source, destination, /, *, overwrite=False):
    print(f"copying {source} to {destination} with overwrite={overwrite}")


copy_file("file1.txt", "file2.txt", overwrite=True)
