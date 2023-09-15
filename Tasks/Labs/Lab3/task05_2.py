# 1.Ввести послідовність символів.
# 2.Вказати ті слова, які містять хоча б одну букву k.
# I must use bytes according to the task
def get_string():
    byte_string = bytearray(input("Enter the string: "), 'utf8')
    return byte_string


def solve_task(byte_string):
    word_list = byte_string.split(b' ')
    words = [word for word in word_list if b'k' in word.lower()]
    return words


def decode_and_print(words):
    print("This words contain the letter \"k\"")
    for word in words:
        print(word.decode("utf8"))


if __name__ == "__main__":
    my_string = get_string()
    required_words = solve_task(my_string)
    decode_and_print(required_words)
