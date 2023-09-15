wikipedia = {"Географія":
         {"Геологія": ("Жорж-Луї Леклерк де Бюффон", "Кліффорд Фрондел"),
          "Землезнавство": ("Фасянь", "Дубіс Лідія Францівна"), },
             "Політика":
         {"Політична психологія": ("О. Майборода", "Филиппов А.В."),
          "Політична соціологія": ("Бацевич Ф. С.", "Є.Захаров"), },
            }


def choice_of_category(dictionary):
    for category in dictionary:
        print("        {0}".format(category))


print("Виберіть категорію:")
choice_of_category(wikipedia)
chapter = str(input().capitalize())

print('Виберіть підкатегорію')
choice_of_category(wikipedia[chapter])
subchapter = str(input().capitalize())

for name in range(0, len(wikipedia[chapter][subchapter])):
    print("{}".format(wikipedia[chapter][subchapter][name]))
