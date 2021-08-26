import logging
import re

REGEX_FORBIDDEN_SET = [
    'Глава \d.*',
    'Том \d.*',
    'Книга \d.*',
    'Часть \d.*',
]


def replace_from_set(string: str, regex_set: [str] = REGEX_FORBIDDEN_SET):
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


if __name__ == '__main__':
    with open('out.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            temp = line
            line = line.split(',')
            if (len(line) != 3):
                line = [line[0], ''.join(
                    line[1:len(line) - 1]), line[len(line) - 1]]
            try:
                line[2] = line[2].split('=')[1]
                line[2] = "".join(filter(str.isdigit, line[2]))
                # print(line[2],line[0])
                print(line[1])
            except:
                logging.error("Exception!! " + temp)
