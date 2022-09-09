def handle_exception(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError as te:
            print(f"There's {te}")
        except ZeroDivisionError as ze:
            print(f"There's {ze}")
        except Exception as e:
            print(f"There's {e}")
    return wrapper


@handle_exception
def cause_error():
    return 1/0


result = cause_error()
print(result)
