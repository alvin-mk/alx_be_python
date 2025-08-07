#  Test Book class
from book_class import Book

#  Test Library System
from library_system import Book as LibBook, EBook, PrintBook, Library

#  Test Polymorphism
from polymorphism_demo import Rectangle, Circle

def test_book_class():
    print("=== Task 0: Book Class ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)              # Uses __str__
    print(repr(my_book))        # Uses __repr__
    del my_book                 # Triggers __del__


def test_library_system():
    print("\n=== Task 1: Library System ===")
    my_library = Library()

    classic = LibBook("Pride and Prejudice", "Jane Austen")
    digital = EBook("Snow Crash", "Neal Stephenson", 500)
    paper = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic)
    my_library.add_book(digital)
    my_library.add_book(paper)

    my_library.list_books()


def test_polymorphism():
    print("\n=== Task 2: Polymorphism Demo ===")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    test_book_class()
    test_library_system()
    test_polymorphism()
