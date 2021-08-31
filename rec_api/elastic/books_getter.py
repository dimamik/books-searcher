from elastic.instance import es


def get_book_by_id(book_id):
    res = es.get(
        index='books_index',
        id=book_id
    )
    return res
