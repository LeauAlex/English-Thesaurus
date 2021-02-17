import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
    user='ardit700_student',
    password='ardit700_student',
    host='108.167.140.122',
    database='ardit700_pm1database'
)
cursor = con.cursor()
w = input('Enter word: ')
querrt = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % w)
results = cursor.fetchall()


def ask_for_answer(question):
    answer = input('Did you mean %s? Yes or No :' %get_close_matches(question, results[0]))
    if answer == 'yes':
        return get_close_matches(question, results)
    if answer == 'no':
        return 'Please try again'


def match_word(wrong_input):
    if ask_for_answer(wrong_input) == get_close_matches(wrong_input, results)[0]:
        print(get_close_matches(wrong_input, results))
    else:
        print('Please try again.')
    return ()


def check_word_case(words):
    x = []
    for word in words:
        x.append(word)
    if not words:
        match_word(words)
    return x


def from_list_to_print(lst):
    for x in check_word_case(lst):
        print(x)



print(from_list_to_print(w))

# match_word(words)
