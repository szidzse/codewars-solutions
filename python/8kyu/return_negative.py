# Return Negative
def make_negative(number):
    return number if number < 0 else -number

print(make_negative(2))

def make_negative2(number):
    return -abs(number)

print(make_negative2(-10))
