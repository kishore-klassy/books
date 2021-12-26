import falcon
from books_resource import BooksResource

app = application = falcon.App()

books = BooksResource()
app.add_route('/books', books)