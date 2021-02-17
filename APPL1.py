import json
from difflib import get_close_matches


content = json.load(open(r'C:\Users\Leau\PycharmProjects\Udemy\APP1 English Thesaurus\data.json', 'r'))


def print_content(x):
    for a in content[x]:
        print(a)


def ask_for_answer(question):
    answer = input('Did you mean %s? Yes or No :' % get_close_matches(question, content.keys())[0]).lower()
    if answer == 'yes':
        return get_close_matches(question, content.keys())[0]
    if answer == 'no':
        return 'Please try again'


def match_word(wrong_input):
    if ask_for_answer(wrong_input) == get_close_matches(wrong_input, content.keys())[0]:
        print_content(get_close_matches(wrong_input, content.keys())[0])
    else:
        print('Please try again.')
    return ()


def check_word_case(words):
    if words in content.keys():
        print_content(words)
    else:
        match_word(words)


word = input('enter word: ')

check_word_case(word)

# END
