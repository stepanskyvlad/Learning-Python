# Kata name: Shortest Word

def find_short(s):
    # your code here
    word_list = s.split()
    the_shortest_word = sorted(word_list, key=lambda x: len(x))[0]
    return len(the_shortest_word)  # shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))
