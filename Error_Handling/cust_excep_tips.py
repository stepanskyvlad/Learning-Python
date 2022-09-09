class CustomException(Exception):
    pass


def cause_error():
    raise CustomException("You called the cause_error function!")


cause_error()
