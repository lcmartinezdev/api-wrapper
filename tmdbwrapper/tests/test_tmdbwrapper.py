from pytest import fixture

from gutendex import Book
import vcr


@fixture
def book_keys():
    # Responsible only for returning the test data
    return [
        "id",
        "title",
        "authors",
        "translators",
        "subjects",
        "bookshelves",
        "languages",
        "copyright",
        "media_type",
        "formats",
        "download_count",
    ]


@vcr.use_cassette("gutendex/tests/test_gutendex/book-info.yml")
def test_book_info(book_keys):
    book_instance = Book(1396)
    response = book_instance.info()

    assert isinstance(response, dict)
    assert response["id"] == 1396, "The ID should be in the response"
    assert set(book_keys).issubset(
        response.keys()
    ), "All keys should be in the response"


@vcr.use_cassette("gutendex/tests/test_gutendex/book-list.yml")
def test_book_list():
    response = Book.list()

    assert isinstance(response, dict)
    assert isinstance(response.get("results"), list)
