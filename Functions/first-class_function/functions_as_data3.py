my_text = '''
Beautiful is better than ugly.   
Explicit is better than implicit.
Simple is better than complex.   
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
def lowercase(text):
    return text.lower()

def remove_punctuation(text):
    punctuations = ['.', '-', ',', '*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def remove_new_lines(text):
    text = text.replace('\n', '')
    return text

def remove_short_words(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

def remove_long_words(text):
    return ' '.join([word for word in text.split() if len(word) < 6 ])


processing_function = [lowercase, remove_punctuation, remove_new_lines, remove_long_words, remove_short_words]

for func in processing_function:
    my_text = func(my_text)

print(my_text)
