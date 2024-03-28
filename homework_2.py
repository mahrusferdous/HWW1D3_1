# Library system enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_books(new_book):
    if new_book not in library:
        library.append(new_book)
        
add_books(("Harry Potter", "J.K. Rowling"))
add_books(("1984", "George Orwell"))

print(library)
    