import re

REGEX_FORBIDDEN_SET = [
    'Глава \d.*',
    'Том \d.*',
    'Книга \d.*',
    'Часть \d.*',
]


def remove_special_chars(word):
    if isinstance(word, str):
        temp = word.replace("\r\n", "")
        result = ""
        for char in temp:
            if char.isalnum() or char in '" -,"`.!?»':
                result += char
        return result
    else:
        return str(word)


def replace_from_set(string: str, regex_set=None):
    if regex_set is None:
        regex_set = REGEX_FORBIDDEN_SET
    for regex_search_term in regex_set:
        string = re.sub(regex_search_term, "", string, flags=re.IGNORECASE)
    return string


def filter_book_name(book_name: str):
    book_name = remove_special_chars(book_name)
    # Get rid of parts/series etc.
    book_name = replace_from_set(book_name)
    book_name = "".join(
        filter(lambda char: char.isalpha() or char in ' ,-"\'!.?0123456789', book_name))
    book_name = re.sub(' +', ' ', book_name)
    return book_name.rstrip().removesuffix(",")


def filter_query(query):
    query = " ".join(query.split())
    query = ''.join(filter(lambda char: str.isdigit(char)
                                        or str.isalpha(char) or char == " ", query))
    return query
