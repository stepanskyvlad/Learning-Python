""" Overloading a Circuit Breaker """


class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0  # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('Connection will exceed capacity')
        elif self.load + amps < 0:
            raise Exception('Connection will cause negative load')
        else:
            self.load += amps


# create a 20A circuit breaker
cb = CircuitBreaker(20)

# connect a valid load
print("First connection")
print(cb.load)
try:
    cb.connect(12)
except Exception as e:
    print(e)
print(cb.load)

# connect an oversized load
print('\nSecond connection:')
print(cb.load)
try:
    cb.connect(30)
except Exception as e:
    print(e)
print(cb.load)

# connect a negative load
print('\nThird connection:')
print(cb.load)
try:
    cb.connect(-30)
except Exception as e:
    print(e)
print(cb.load)

print('\nForth connection:')
print(cb.load)
try:
    cb.connect(9)
except Exception as e:
    print(e)
print(cb.load)

# OUTPUT:
# First connection
# 0
# 12
#
# Second connection:
# 12
# Connection will exceed capacity
# 12
#
# Third connection:
# 12
# Connection will cause negative load
# 12
#
# Forth connection:
# 12
# Connection will exceed capacity
# 12
