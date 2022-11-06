class ClassNameError(Exception):
    pass


class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if new_name.isalnum() and new_name[0].isupper():
            cls.__name__ = new_name
        else:
            raise ClassNameError("Invalid class name")

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"
