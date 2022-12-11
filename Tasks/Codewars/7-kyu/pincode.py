# Kata name: Regex validate PIN code

def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


# other solution
def validate_pin_1(pin):
    return len(pin) in (4, 6) and pin.isdigit()  # So len(pin) in (4,6) is equivalent to len(pin) == 4 or len(pin) == 6


print(validate_pin("-1111"))
