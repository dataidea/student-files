class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.lent_books = []

    def addBook(self, book):
        self.books.append(book)

    def addManyBooks(self, books):
        self.books.extend(books)

    def displayBooks(self):
        for book in self.books:
            print(book)

    def lendBook(self, title, person):
        for book in self.books:
            if book.title == title:
                if book.title not in self.lent_books:
                    person.borrowed_books.append(book)
                    self.lent_books.append(book.title)
                    return
                else:
                    print(title + ' is not availabe')
                    return
        print('There no such book in the library') 

    def __str__(self):
        return str(self.name)


class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.available = True

    def __str__(self):
        return str(self.title)


class Person:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def displayBooks(self):
        for book in self.borrowed_books:
            print(book)

    def __str__(self):
        return str(self.name)

# our people
viola = Person(name='Viola')
shafara = Person(name='Shafara')

# our books
books = [
    Book(title='Song of Lawino', author='Danny'),
    Book(title='Da Vinci Code', author='Dan Brown'),
    Book(title='Harry Potter', author='JK Rowling')
] 

# our libraries
city_library = Library(name='City Library')

city_library.addManyBooks(books)

city_library.lendBook('Harry Potter', viola)

city_library.lendBook('Da Vinci Code', shafara)


print(viola.displayBooks())




