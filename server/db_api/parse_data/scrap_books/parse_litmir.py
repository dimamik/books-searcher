import logging
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

from process_data.process_data import convert_csv_to_json, combine_csv

START_PAGE = 4500
MAX_PAGES = 6000


def find_description(book):
    description = book.find("div", {'itemprop': 'description'})
    description = description.find("div", class_="BBHtmlCodeInner")

    description = description.find_all("p")
    if len(description) > 1:
        description = description[1]
    elif len(description) == 0:
        return ""
    else:
        description = description[0]

    return description.text


def get_book_points(book):
    book_points = "0"
    try:
        book_points = book.find("span", class_="orange_desc").text
    except Exception as e:
        pass
    return book_points


def get_books_from_page(page_number=1):
    df_temp = pd.DataFrame(columns=['book_name', 'book_author',
                                    'book_description', 'book_genre', 'book_points'])
    url = f'https://www.litmir.me/bs?rs=5%7C1%7C0&o=100&p={page_number}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    books = soup.find_all("table", class_="island")
    for book in books:
        try:
            book_description = find_description(book)
            book_name = book.find("span", {'itemprop': 'name'}).text
            book_genre = book.find("span", {'itemprop': 'genre'}).text
            book_points = get_book_points(book)
            book_author = book.find("span", {'itemprop': 'author'})
            if book_author != None:
                book_author = book_author.text
            else:
                book_author = ""
            df_temp = df_temp.append(
                pd.DataFrame({"book_name": [book_name], "book_genre": [book_genre], "book_author": [book_author],
                              "book_points": [book_points],
                              "book_description": [book_description]}), ignore_index=True)
        except Exception as e:
            print("Error in there", e)
    return df_temp


def parse_litmir(last_page=MAX_PAGES):
    Path("scrap/out/").mkdir(parents=True, exist_ok=True)
    res = pd.DataFrame(columns=['book_name', 'book_author',
                                'book_description', 'book_genre', 'book_points'])
    for i in range(START_PAGE, last_page):
        res = res.append(get_books_from_page(i))
        logging.info(f'Page {i} is complete\n')
        if res is None:
            continue
        if (i % 100 == 0):
            res.to_csv(f'scrap/out/{i}.csv', index=False)
            res = pd.DataFrame(columns=['book_name', 'book_author',
                                        'book_description', 'book_genre', 'book_points'])
            logging.info(
                f'Pages {i - 100} to {i} are converted to csv and located in out/{i}.csv \n')


# Generates json out of scarped pages to load into elasticsearch db
# last_page should be divided by 100

def make_readable_json():
    parse_litmir(last_page=4500)
    combine_csv()
    convert_csv_to_json(r'data/data.csv', r'data/data.json')
    logging.info("Json is build successfully")


if __name__ == "__main__":
    parse_litmir()
