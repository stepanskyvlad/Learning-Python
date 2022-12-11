# Simple Encryption #1 - Alternating Split
# my solution
def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    length = len(encrypted_text)
    original_list = list(encrypted_text)
    for _ in range(n):
        for index, value in zip(range(0, length, 2), encrypted_text[length // 2:]):
            original_list[index] = value
        for index, value in zip(range(1, length, 2), encrypted_text[:length // 2]):
            original_list[index] = value
        encrypted_text = original_list.copy()
    return "".join(encrypted_text)


def encrypt(text, n):
    if not text or n <= 0:
        return text
    new_text = text
    for _ in range(n):
        new_text = new_text[1::2] + new_text[::2]
    return new_text


# other solutions
def decrypt_1(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt_1(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def decrypt_2(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt_2(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s


print(encrypt("0123456", 2))
print(decrypt("3041526", 2))
