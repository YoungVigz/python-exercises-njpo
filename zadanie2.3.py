from collections import namedtuple, defaultdict

Book = namedtuple('Book', ['title', 'genre', 'author', 'isbn'])

def add_book(collection, title, genre, author, isbn):
    book = Book(title, genre, author, isbn)
    collection.append(book)

def display_collection(collection):
    for book in collection:
        print("Tytuł:", book.title)
        print("Gatunek:", book.genre)
        print("Autor:", book.author)
        print("ISBN:", book.isbn)
        print()

def calculate_statistics(collection):
    genre_stats = defaultdict(int)
    author_stats = defaultdict(int)
    for book in collection:
        genre_stats[book.genre] += 1
        author_stats[book.author] += 1
    return genre_stats, author_stats

books_collection = []

add_book(books_collection, "Harry Potter and the Philosopher's Stone", "Fantasy", "J.K. Rowling", "978-0747532743")
add_book(books_collection, "To Kill a Mockingbird", "Fiction", "Harper Lee", "978-0061120084")
add_book(books_collection, "1984", "Dystopian", "George Orwell", "978-0451524935")

print("Zawartość kolekcji książek:")
display_collection(books_collection)

genre_stats, author_stats = calculate_statistics(books_collection)

print("Statystyki gatunków:")
for a, k in genre_stats.items():
    print(a, ": ", k)

print()
print("Statystyki autorów:")
for a, k in author_stats.items():
    print(a, ": ", k)