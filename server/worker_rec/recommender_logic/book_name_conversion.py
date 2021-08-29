import re

REGEX_FORBIDDEN_SET = [
    'Глава \d.*',
    'Том \d.*',
    'Книга \d.*',
    'Часть \d.*',
]


def replace_from_set(string: str, regex_set=None):
    if regex_set is None:
        regex_set = REGEX_FORBIDDEN_SET
    for regex_search_term in regex_set:
        string = re.sub(regex_search_term, "", string)
    return string


def convert_book_name(book_name: str):
    # Get rid of parts/series etc.
    book_name = replace_from_set(book_name)
    book_name = "".join(
        filter(lambda chr: chr.isalpha() or chr in ' 0123456789', book_name))
    book_name = re.sub(' +', ' ', book_name)
    return book_name.rstrip()
