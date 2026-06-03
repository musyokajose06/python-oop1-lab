#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    title = input("Enter book title: ")

    try:
        page_count = int(input("Enter page count: "))
    except ValueError:
        page_count = input("Enter page count: ")

    book = Book(title, page_count)

    print(f"Title: {book.title}")
    if hasattr(book, "_page_count"):
        print(f"Pages: {book.page_count}")

    book.turn_page()