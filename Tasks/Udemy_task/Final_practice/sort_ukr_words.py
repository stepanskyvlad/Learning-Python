ukr_alphabet_dict = {'а': '01', 'б': '02', 'в': '03', 'г': '04', 'ґ': '05', 'д': '06', 'е': '07', 'є': '08', 'ж': '09',
                     'з': '10', 'и': '11', 'і': '12', 'ї': '13', 'й': '14', 'к': '15', 'л': '16', 'м': '17', 'н': '18',
                     'о': '19', 'п': '20', 'р': '21', 'с': '22', 'т': '23', 'у': '24', 'ф': '25', 'х': '26', 'ц': '27',
                     'ч': '28', 'ш': '29', 'щ': '30', 'ь': '30', 'ю': '32', 'я': '33'}


def sort_rule(word):
    numeric = ''
    for letter in word.lower():
        if letter in ukr_alphabet_dict:
            numeric += str(ukr_alphabet_dict[letter])
        else:
            numeric += '34'
    return numeric


with open('UkrWords.txt', 'r', encoding='utf-8-sig') as file:
    unsorted_list = [word.strip() for word in file.readlines()]

sorted_list = sorted(unsorted_list, key=sort_rule)

with open('SortedUkrWords.txt', 'w', encoding='utf-8-sig') as write_file:
    for word in sorted_list:
        write_file.write(f"{word}\n")
