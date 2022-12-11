# Python's Dynamic Classes #1

class ClassNameError(Exception):
    pass


def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ClassNameError("Invalid class name")


# another solution
def class_name_changer_1(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name
