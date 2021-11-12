from . import session


class Book(object):
    def __init__(self, id) -> None:
        self.id = id

    def info(self):
        path = "https://gutendex.com/books/{}".format(self.id)
        response = session.get(path)
        return response.json()

    @staticmethod
    def list():
        path = "https://gutendex.com/books/"
        response = session.get(path)
        return response.json()
