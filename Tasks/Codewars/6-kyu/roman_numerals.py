# Kata name: Roman Numerals Decoder

# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
def solution(roman):
    value = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result, last = 0, 0
    for char in list(roman)[::-1]:
        if last == 0:
            result += value[char]
        elif last > value[char]:
            result -= value[char]
        else:
            result += value[char]
        last = value[char]
    return result


# another solution
def parse_roman(roman):
    value = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and value[c] < value[roman[i + 1]]:
            result -= value[c]
        else:
            result += value[c]
    return result


def old_solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    result = 0
    symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    count = 0
    while count < len(roman):
        if roman[count] == "C" and count < len(roman) - 1:
            if roman[count + 1] == "M":
                result += 900
                count += 2
            elif roman[count + 1] == "D":
                result += 400
                count += 2
            else:
                result += symbols[roman[count]]
                count += 1
        elif roman[count] == "X" and count < len(roman) - 1:
            if roman[count + 1] == "C":
                result += 90
                count += 2
            elif roman[count + 1] == "L":
                result += 40
                count += 2
            else:
                result += symbols[roman[count]]
                count += 1
        elif roman[count] == "I" and count < len(roman) - 1:
            if roman[count + 1] == 'X':
                result += 9
                count += 2
            elif roman[count + 1] == "V":
                result += 4
                count += 2
            else:
                result += symbols[roman[count]]
                count += 1
        else:
            result += symbols[roman[count]]
            count += 1
    return result


if __name__ == '__main__':
    print(parse_roman("MCMXC"))  # 1990
    print(parse_roman("MMVIII"))  # 2008
    print(parse_roman("MDCLXVI"))  # 1666
